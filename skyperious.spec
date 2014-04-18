Summary:	Skype SQLite database viewer and merger
Name:		skyperious
Version:	3.1
Release:	0.1
License:	MIT
Group:		Applications
Source0:	https://github.com/suurjaak/Skyperious/archive/master/%{name}-%{version}.tar.gz
# Source0-md5:	1a2f6e3b369c435a23ac796915890b60
URL:		https://github.com/suurjaak/Skyperious
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.219
Requires:	python-PIL
Requires:	python-dateutil
Requires:	python-pyparsing
Requires:	python-skype
Requires:	python-wxPython
Requires:	python-xlsxwriter
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%build
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT
%{__python} setup.py install \
	--skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md CHANGELOG.md LICENSE.md

