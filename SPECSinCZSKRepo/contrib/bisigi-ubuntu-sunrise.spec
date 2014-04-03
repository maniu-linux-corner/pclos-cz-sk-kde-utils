%define name gnome-bisigi-ubuntu-sunrise-theme
%define version 3.0.0
%define release %mkrel 1

%define themesdir %{_datadir}/themes
%define iconsdir %{_datadir}/icons
%define wallpapersdir %{_datadir}/backgrounds
%define wallpaperspropdir %{_datadir}/gnome-background-properties
%define docsdir %{_docdir}/%{name}
%define themeinside ubuntu-sunrise


Summary: 	Bisigi theme
Name:    	%{name}
Version: 	%{version}
Release: 	%{release}
Source1: 	ubuntu-sunrise-theme.tar.gz

License: 	GPL
Group: 		Graphical desktop/GNOME
URL:   	   	http://www.bisigi-project.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires:	murrine

%description
Ubuntu Sunrise theme contains a full theme for GNOME based system.
It includes the following components:
   * "Ubuntu Sunrise" wallpapers
   * GTK+ theme
   * Metacity theme
   * Ubuntu Sunrise Icons set

%prep

tar -xf %{SOURCE1}
cd ubuntu-sunrise-theme/Gtk/
tar -xf %{themeinside}.tar.gz
cd ..
cd Icons
tar --bzip2 -xf %{themeinside}.tar.bz2

%install

%__rm -rf %{buildroot}
%__install -d %{buildroot}%{themesdir}
%__install -d %{buildroot}%{iconsdir}
%__install -d %{buildroot}%{wallpapersdir}
%__install -d %{buildroot}%{wallpaperspropdir}
%__install -d %{buildroot}%{docsdir}
%__install -d %{buildroot}%{emeralddir}

cd ubuntu-sunrise-theme/Wallpaper
%__cp -rf *.jpg %{buildroot}%{wallpapersdir}
%__cp -rf *.xml %{buildroot}%{wallpaperspropdir}
cd ..
%__cp -rf COPYING %{buildroot}%{docsdir}
%__cp -rf credits.txt %{buildroot}%{docsdir}
cd Gtk
%__cp -rf ./* %{buildroot}%{themesdir}
cd ..
cd Icons
%__cp -rf ./* %{buildroot}%{iconsdir}
cd ..
cd ..


%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{docsdir}/* 
%{themesdir}/*
%{iconsdir}/*
%{wallpapersdir}/*
%{wallpaperspropdir}/*

%changelog
* Fri Feb 11 2011 Cristobal Lopez <lopeztobal@gmail.com> 2.4.1-1mib2010.2
- Update.

* Fri Aug 20 2010 Cristobal Lopez <lopeztobal@gmail.com> 2.3.3-1mib2010.1
- Update.

* Sat Jul 10 2010 Cristobal Lopez <lopeztobal@gmail.com> 2.3.2-1mib2010.1
- Update.
