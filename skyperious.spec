Summary:	Skype SQLite database viewer and merger
Name:		skyperious
Version:	3.5
Release:	0.2
License:	MIT
Group:		Applications/Databases
Source0:	https://github.com/suurjaak/Skyperious/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	56a23e2c330a4ac917b915ed5ff8af3d
Patch0:		desktop.patch
URL:		https://github.com/suurjaak/Skyperious
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.713
Requires:	desktop-file-utils
Requires:	python(sqlite)
Requires:	python-PIL
Requires:	python-dateutil
Requires:	python-pyparsing
Suggests:	python-skype
Suggests:	python-wxPython
Suggests:	python-xlsxwriter
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
%setup -qn Skyperious-%{version}
%patch -P0 -p1

%build
%py_build

%install
rm -rf $RPM_BUILD_ROOT
%py_install
%py_postclean

install -d $RPM_BUILD_ROOT{%{_pixmapsdir},%{_desktopdir}}
cp -p res/Icon64x64_32bit.png $RPM_BUILD_ROOT%{_pixmapsdir}/%{name}.png
cp -p dist/%{name}.desktop $RPM_BUILD_ROOT%{_desktopdir}

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
%dir %{py_sitescriptdir}/%{name}
%{py_sitescriptdir}/%{name}/*.py[co]
%{py_sitescriptdir}/%{name}/third_party
%{py_sitescriptdir}/%{name}/skyperious.ini
%{py_sitescriptdir}/Skyperious-%{version}-py*.egg-info
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png

# FIXME: use system fonts
%{py_sitescriptdir}/%{name}/res
