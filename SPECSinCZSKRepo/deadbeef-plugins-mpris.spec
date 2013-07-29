Name: deadbeef-mpris
Summary: A dbus-plugin for deadbeef
Version: 2.1.5
Release: 2
License: GPL v2
URL: http://code.google.com/p/deadbeef-mpris-plugin/
Group: Applications/Audio
Source0: deadbeef-MPRIS-plugin-2.1.5.tar.gz
Source1: deadbeef-MPRIS-plugin-2.1.5-glibfix.patch
BuildRequires:	libgtk+2.0_0-devel
BuildRequires: deadbeef-devel
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A dbus-plugin for deadbeef

%prep
%setup -n deadbeef-2.1.5

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
patch -i %{SOURCE1}
./configure --prefix=/usr
make

%install
make DESTDIR="$RPM_BUILD_ROOT" install

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_libdir}/deadbeef/*

%changelog
* Sat Mar 25 2013 Mank <Mank1@seznam.cz> 2.1.5-1
- deadbeef-mpris: Version : 2.1.5
