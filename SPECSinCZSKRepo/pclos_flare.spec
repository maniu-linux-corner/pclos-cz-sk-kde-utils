%define name	flare
%define version	0.19
%define release	%mkrel 3git
%define	Summary	A RPG clone with Smal code base
%define sdir flare

Summary:	%{Summary}
Name:		%{name}
Version:	%{version}
Release:	%{release}
URL:		http://flarerpg.org
Source0:	flare.tar.xz
Source1:	flare-engine.tar
Source2:	flare.desktop
License:	GPL
Group:		Games/RPG
BuildRequires:	%{_lib}SDL_image-devel %{_lib}SDL_net-devel %{_lib}SDL_mixer1.2-devel %{_lib}SDL-devel %{_lib}SDL_ttf-devel cmake
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
..

%prep
%setup -n %{sdir}

%build
tar -xf %{SOURCE1}
cd flare-engine
cmake -DCMAKE_INSTALL_PREFIX=/usr -DBINDIR=/usr/bin -DDATADIR=/usr/share/flare .
%make
cd ..
cmake -DCMAKE_INSTALL_PREFIX=/usr -DBINDIR=/usr/bin -DDATADIR=/usr/share/flare .
make

%install
%define qsdir %{_builddir}/%{sdir}
cd flare-engine
make install DESTDIR=$RPM_BUILD_ROOT
cd ..
make install DESTDIR=$RPM_BUILD_ROOT
#fix the desktop file
mkdir -p "%{_builddir}%{_datadir}/applications/";
cp "%{SOURCE2}" "%{_builddir}%{_datadir}/applications/";

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_datadir}/applications/flare.desktop
%{_datadir}/flare/*
%{_datadir}/man/*
%{_iconsdir}/hicolor/scalable/apps/*
%{_bindir}/flare


%changelog
* Wed Jun 15 2013 Mank <mank1@seznam.cz> 0.19-2pclos1
-	Build for PCLinuxOS

