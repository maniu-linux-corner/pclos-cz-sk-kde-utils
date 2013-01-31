Name: config-cs
Summary: A Live install for cs/sk locales
Version: 1.0.0
Release: 3
License: GPL v2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Obsoletes: config-cs-sk
Obsoletes: config-sk
Source0: config-cs.tar.gz
Source1: en-na-cs.sh
Source2: smb.conf-cs-sk
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
Konfigurační soubory pro úplnou lokalizaci prostředí do češtiny

%prep
%setup -c config-cs

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

cp -r * $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/tmp/
mkdir -p $RPM_BUILD_ROOT/etc/samba
cp %{SOURCE1} $RPM_BUILD_ROOT/tmp/en-na-cs.sh
cp %{SOURCE2} $RPM_BUILD_ROOT/etc/samba/smb.conf

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post
sh /tmp/en-na-cs.sh;
echo "Uživatelé ze Slovenska, nainstalujte si balíček config-sk.";
rm /tmp/en-na-cs.sh

%files
%defattr(-,root,root)
%config(missingok) /tmp/en-na-cs.sh
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

%changelog
* Sat Aug 11 2012 Mank <Mank1@seznam.cz> 1.0.0-1
- 
