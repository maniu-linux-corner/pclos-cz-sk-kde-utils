Name: gnome-nameday-applet
Summary: Svatkovy Applet pro Gnome
Version: 0.0.1
Release: 1
License: GPL v2
Group: Applications/Gnome
Source0: gnome-nameday.tar.xz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Svatkovy Applet pro Gnome2

%prep
%setup

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin/
mkdir -p $RPM_BUILD_ROOT/usr/lib/bonobo/servers/
cp gnome-nameday-applet.py $RPM_BUILD_ROOT/usr/bin/
cp GNOME_NameDayApplet.server $RPM_BUILD_ROOT/usr/lib/bonobo/servers/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{_bindir}/*
%{_libdir}/bonobo/servers/*

%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 0.0.1-1
- Namedays: Version 0.0.1
