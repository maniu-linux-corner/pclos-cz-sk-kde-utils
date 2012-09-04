Name: task-LO
Summary: Task for Office Suite (core)
Version: 3.5
Release: 1
License: LGPLv3
URL: http://www.libreoffice.org/
Group: Tasks
Source0: README_en-US.tar
BuildArch: noarch
Requires: libobasis3.5-base
Requires: libobasis3.5-binfilter
Requires: libobasis3.5-calc
Requires: libobasis3.5-core01
Requires: libobasis3.5-core02
Requires: libobasis3.5-core03
Requires: libobasis3.5-core04
Requires: libobasis3.5-core05
Requires: libobasis3.5-core06
Requires: libobasis3.5-core07
Requires: libobasis3.5-draw
Requires: libobasis3.5-en-US-base
Requires: libobasis3.5-en-US-calc
Requires: libobasis3.5-en-US-math
Requires: libobasis3.5-en-US-res
Requires: libobasis3.5-en-US-writer
Requires: libobasis3.5-en-US
Requires: libobasis3.5-extension-beanshell-script-provider
Requires: libobasis3.5-extension-javascript-script-provider
Requires: libobasis3.5-extension-mediawiki-publisher
Requires: libobasis3.5-extension-nlpsolver
Requires: libobasis3.5-extension-pdf-import
Requires: libobasis3.5-extension-presentation-minimizer
Requires: libobasis3.5-extension-presenter-screen
Requires: libobasis3.5-extension-python-script-provider
Requires: libobasis3.5-extension-report-builder
Requires: libobasis3.5-gnome-integration
Requires: libobasis3.5-graphicfilter
Requires: libobasis3.5-images
Requires: libobasis3.5-impress
Requires: libobasis3.5-javafilter
Requires: libobasis3.5-kde-integration
Requires: libobasis3.5-math
Requires: libobasis3.5-ogltrans
Requires: libobasis3.5-onlineupdate
Requires: libobasis3.5-ooofonts
Requires: libobasis3.5-ooolinguistic
Requires: libobasis3.5-postgresql-sdbc
Requires: libobasis3.5-pyuno
Requires: libobasis3.5-writer
Requires: libobasis3.5-xsltfilter
Requires: libreoffice3.5-base
Requires: libreoffice3.5-calc
Requires: libreoffice3.5-dict-en
Requires: libreoffice3.5-dict-es
Requires: libreoffice3.5-dict-fr
Requires: libreoffice3.5-draw
Requires: libreoffice3.5-en-US
Requires: libreoffice3.5-impress
Requires: libreoffice3.5-math
Requires: libreoffice3.5-stdlibs
Requires: libreoffice3.5-ure
Requires: libreoffice3.5-writer
Requires: libreoffice3.5
Requires: libreoffice3.5-mandriva-menus
Requires: task-java

Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
LibreOffice is the power-packed free, libre and open source personal productivity suite for Windows, Macintosh and GNU/Linux, that gives you six feature-rich applications for all your document production and data processing needs: Writer, Calc, Impress, Draw, Math and Base. Support and documentation is free from our large, dedicated community of users, contributors and developers. You, too, can get involved!

%prep
%setup -c

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/doc/task-lo/
cp $RPM_SOURCE_DIR/README_en-US $RPM_BUILD_ROOT/usr/share/doc/task-lo/


%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/usr/share/doc/task-lo/README_en-US


%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 3.5-1
- initial task packages
