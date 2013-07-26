%define name gnome-bisigi-eco-theme
%define version 1.5.1
%define release %mkrel 1

%define themesdir %{_datadir}/themes
%define iconsdir %{_datadir}/icons
%define wallpapersdir %{_datadir}/backgrounds
%define wallpaperspropdir %{_datadir}/gnome-background-properties
%define docsdir %{_docdir}/%{name}


Summary: 	Bisigi theme
Name:    	%{name}
Version: 	%{version}
Release: 	%{release}
Source1: 	eco-theme.tar.bz2

License: 	GPL
Group: 		Graphical desktop/GNOME
URL:   	   	http://www.bisigi-project.org
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildArch: 	noarch
Requires:	murrine

%description
Eco theme contains a full theme for GNOME based system.
It includes the following components:
   * "Eco" wallpapers
   * GTK+ theme
   * Metacity theme
   * Eco Icons set

%prep

tar --bzip2 -xf %{SOURCE1}

%install

%__rm -rf %{buildroot}
%__install -d %{buildroot}%{themesdir}
%__install -d %{buildroot}%{iconsdir}
%__install -d %{buildroot}%{wallpapersdir}
%__install -d %{buildroot}%{wallpaperspropdir}
%__install -d %{buildroot}%{docsdir}

cd eco-theme/Wallpaper
%__cp -rf *.png %{buildroot}%{wallpapersdir}
%__cp -rf *.xml %{buildroot}%{wallpaperspropdir}
cd ..
%__cp -rf COPYING %{buildroot}%{docsdir}
%__cp -rf credits %{buildroot}%{docsdir}
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
* Fri Feb 11 2011 Cristobal Lopez <lopeztobal@gmail.com> 1.5.1-1mib2010.2
- Update.

* Fri Aug 20 2010 Cristobal Lopez <lopeztobal@gmail.com> 1.4.1-1mib2010.1
- Update.

* Fri Jul 09 2010 Cristobal Lopez <lopeztobal@gmail.com> 1.4.0-1mib2010.1
- Update.
