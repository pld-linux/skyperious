Summary:	Skype SQLite database viewer and merger
Name:		skyperious
Version:	3.1
Release:	0.7
License:	MIT
Group:		Applications/Databases
Source0:	https://github.com/suurjaak/Skyperious/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	1a2f6e3b369c435a23ac796915890b60
Source1:	https://raw.githubusercontent.com/glensc/Skyperious/desktop/packaging/%{name}.desktop
# Source1-md5:	b6e430c377ca6754c5905fdf94bc1d8e
URL:		https://github.com/suurjaak/Skyperious
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	desktop-file-utils
Requires:	python(sqlite)
Requires:	python-PIL
Requires:	python-dateutil
Requires:	python-pyparsing
Requires:	python-xlsxwriter
Suggests:	python-skype
Suggests:	python-wxPython
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdir	%{_datadir}/%{name}

%description
Skyperious is a Skype database viewer and merger, written in Python.

You can open local Skype SQLite databases and look at their contents:
- search across all messages and contacts
- browse chat history and export as HTML, see chat statistics
- import contacts from a CSV file to your Skype contacts
- view any database table and export their data, fix database
  corruption
- change, add or delete data in any table
- execute direct SQL queries and
- synchronize messages in two Skype databases: keep chat history
  up-to-date on different computers, or restore missing messages from
  older files into the current one

%prep
%setup -qc
mv Skyperious-*/* .

cat <<'EOF' > skyperious.sh
#!/bin/sh
file=$(readlink -f "$0")
dir=$(dirname "$file")
exec %{__python} $dir/src/main.pyc "$@"
EOF

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir},%{_pixmapsdir},%{_desktopdir}}
cp -a src res %{name}.sh $RPM_BUILD_ROOT%{_appdir}
ln -s %{_appdir}/%{name}.sh $RPM_BUILD_ROOT%{_bindir}/%{name}

cp -p res/Icon64x64_32bit.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
cp -p %{SOURCE1} $RPM_BUILD_ROOT%{_desktopdir}

%py_ocomp $RPM_BUILD_ROOT%{_appdir}
%py_comp $RPM_BUILD_ROOT%{_appdir}
%py_postclean %{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_desktop_database

%postun
%update_desktop_database

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE.md
%attr(755,root,root) %{_bindir}/skyperious
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/skyperious.sh
%{_appdir}/res
%dir %{_appdir}/src
%dir %{_appdir}/src/third_party
%{_appdir}/src/*.py[co]
%{_appdir}/src/third_party/*.py[co]
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
