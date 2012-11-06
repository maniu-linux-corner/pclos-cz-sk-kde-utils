%define name	flare
%define version	0.17git
%define release	%mkrel 6
%define	Summary	A RPG clone with Smal code base
%define sdir flare

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://flarerpg.org
Source0:	flare.zip
License:	GPL
Group:		Games/RPG
BuildRequires:	%{_lib}SDL_image-devel %{_lib}SDL_net-devel %{_lib}SDL_mixer1.2-devel %{_lib}SDL-devel %{_lib}SDL_ttf2.0-devel cmake
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
..

%prep
%setup -n %{sdir}

%build
cmake -DCMAKE_INSTALL_PREFIX=/usr -DBINDIR=/usr/bin -DDATADIR=/usr/share/flare .

%make

%install
%define qsdir %{_builddir}/%{sdir}
make install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/applications/flare.desktop
%{_bindir}/flare
%{_datadir}/flare/mods/*
%{_iconsdir}/hicolor/scalable/apps/*

%changelog
* Wed May 28 2012 Mank <mank1@seznam.cz> 0.17-1pclinux2012.2
-	Build for PCLinuxOS
