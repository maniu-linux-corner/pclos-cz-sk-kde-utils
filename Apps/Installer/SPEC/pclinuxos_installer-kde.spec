Name: installer-kde
Summary: A Installer for CZ&SK Community
Version: 1.0.4
Release: 1
License: GPL v2
URL: https://pclinuxos.cz
BuildArch: noarch
Group: Applications
Source0: installer-kde-%{version}.tar.gz
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A Installer for CZ&SK Community

%prep
%setup

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/
./install.sh $RPM_BUILD_ROOT/usr/

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
%{_bindir}/installer
%{_sbindir}/*
%{_datadir}/*
%{_docdir}/*

%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 1.0.4-1
- Installer (KDE Edition)
