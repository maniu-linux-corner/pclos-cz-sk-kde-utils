Name: config-sk
Summary: Lokalizace systému do slovenštiny
Version: 1.0.0
Release: 6
License: GPL v2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Conflicts: config-cs
Source0: config-sk.tar.xz
Source1: en-na-sk.sh
Source2: smb.conf-cs-sk
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Lokalizace systému do slovenštiny

Konfigurační soubory pro úplnou lokalizaci systému do slovenštiny
%prep
%setup -c config-sk

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

cp -r * $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/tmp/
mkdir -p $RPM_BUILD_ROOT/etc/samba
cp %{SOURCE1} $RPM_BUILD_ROOT/tmp/en-na-sk.sh
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/samba/smb.conf

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
sh /tmp/en-na-sk.sh;
rm /tmp/en-na-sk.sh;



%files
%defattr(-,root,root)
%config(missingok) /tmp/en-na-sk.sh
/etc/samba/smb.conf
/etc/rc.d/init.d/repo-mank
 /etc/skel/.config/user-dirs.dirs
 /etc/skel/.config/user-dirs.locale
 /etc/sysconfig/i18n
 /etc/sysconfig/i18n_AL
 /etc/xdg/user-dirs.defaults
 %{_datadir}/applications/clementine.desktop
 %{_datadir}/applications/drakfirewall.desktop
 %{_datadir}/applications/draknetcenter.desktop
 %{_datadir}/applications/localedrake-user.desktop
 %{_datadir}/applications/pclinuxos-drakconf.desktop
 %{_datadir}/applications/synaptic-kde.desktop
 %{_datadir}/applications/synaptic.desktop
 /.directory
  /tmp/smb_charset.sh
   %{_datadir}/desktop-directories/mandriva-system-archiving.directory
   %{_datadir}/desktop-directories/mandriva-system-configuration.directory
   %{_datadir}/desktop-directories/mandriva-system-filetools.directory
   %{_datadir}/desktop-directories/mandriva-system-monitoring.directory
   %{_datadir}/desktop-directories/mandriva-system-terminals.directory
   %{_datadir}/locale/sk/LC_MESSAGES/synaptic.mo


%changelog
* Sat Aug 11 2012 Mank <Mank1@seznam.cz> 1.0.0-1
-
