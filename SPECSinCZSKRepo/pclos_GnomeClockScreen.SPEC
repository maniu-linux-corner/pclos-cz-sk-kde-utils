Name: gnome-clock-screensaver
Summary: A Screensaver with Analog clock
Version: 1.0.1
Release: 1
License: GPL v3
Group: Applications/Gnome
Source0: gnome-clock-screensaver-1.0.1.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A ScreenSaver with Analog Clock

%prep
%setup

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make

%install
make install
mkdir -p $RPM_BUILD_ROOT/usr/lib/zzzz/
mv -Tf $RPM_BUILD_ROOT/usr/lib/gnome-screensaver $RPM_BUILD_ROOT/usr/lib/zzzz/anclock
mv -f $RPM_BUILD_ROOT/usr/lib/zzzz/ $RPM_BUILD_ROOT/usr/lib/gnome-screensaver/
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/zzzz/
mv -Tf $RPM_BUILD_ROOT/usr/share/applications/screensavers $RPM_BUILD_ROOT/usr/share/applications/zzzz/anclock.desktop
mv -f $RPM_BUILD_ROOT/usr/share/applications/zzzz/ $RPM_BUILD_ROOT/usr/share/applications/screensavers/
rm -rf $RPM_BUILD_ROOT/usr/share/applications/zzzz/
rm -rf $RPM_BUILD_ROOT/usr/lib/zzzz/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
make clean

%files
%defattr(-,root,root)
%{_libdir}/gnome-screensaver/anclock
%{_datadir}/applications/screensavers/anclock.desktop

%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 1.0.1-1
- anclock: Version 1.0.1
