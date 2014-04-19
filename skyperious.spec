Summary:	Skype SQLite database viewer and merger
Name:		skyperious
Version:	3.1
Release:	0.4
License:	MIT
Group:		Applications
Source0:	https://github.com/suurjaak/Skyperious/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	1a2f6e3b369c435a23ac796915890b60
URL:		https://github.com/suurjaak/Skyperious
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python(sqlite)
Requires:	python-PIL
Requires:	python-dateutil
Requires:	python-pyparsing
Requires:	python-wxPython
Requires:	python-xlsxwriter
Suggests:	python-skype
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
install -d $RPM_BUILD_ROOT{%{_bindir},%{_appdir}}
cp -a src res %{name}.sh $RPM_BUILD_ROOT%{_appdir}
ln -s %{_appdir}/%{name}.sh $RPM_BUILD_ROOT%{_bindir}

%py_ocomp $RPM_BUILD_ROOT%{_appdir}
%py_comp $RPM_BUILD_ROOT%{_appdir}
%py_postclean %{_appdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE.md
%attr(755,root,root) %{_bindir}/skyperious.sh
%dir %{_appdir}
%attr(755,root,root) %{_appdir}/skyperious.sh
%{_appdir}/res
%dir %{_appdir}/src
%dir %{_appdir}/src/third_party
%{_appdir}/src/*.py[co]
%{_appdir}/src/third_party/*.py[co]
