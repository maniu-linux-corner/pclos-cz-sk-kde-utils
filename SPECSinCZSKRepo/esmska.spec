Name: esmska
Summary: A program to send sms
Version: 1.3
Release: 1
License: AGPL
URL: http://code.google.com/p/esmska/wiki/Download?tm=2
Group: Applications/Java
Source0: esmska-%{version}.tar.gz
Source1: esmska.desktop
Requires: java-1.6.0-sun
BuildArch:	noarch
Buildroot: %{_tmppath}/%{name}-%{version}-buildroot
%description
A program to send sms via Gateways

%prep
%setup

%build
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%install

	install -d "$RPM_BUILD_ROOT/usr/share/java/esmska"
	cp -a * "$RPM_BUILD_ROOT/usr/share/java/esmska"

	#.desktop + icon files
	install -D -m644 "%{SOURCE1}" \
		"$RPM_BUILD_ROOT/usr/share/applications/esmska.desktop"
	install -D -m644 "%{_builddir}/esmska-%{version}/icons/esmska.png" \
		"$RPM_BUILD_ROOT/usr/share/pixmaps/esmska.png"

	#executable file
	install -d -m755 "$RPM_BUILD_ROOT/usr/bin"
	ln -s "/usr/share/java/esmska/esmska.sh" \
		"$RPM_BUILD_ROOT/usr/bin/$_name"

	#license
	install -D -m644 %{_builddir}/%{name}-%{version}/license/license.txt \
		$RPM_BUILD_ROOT/usr/share/licenses/$_name/LICENSE
	install -D -m644 %{_builddir}/%{name}-%{version}/license/gnu-agpl.txt \
		$RPM_BUILD_ROOT/usr/share/licenses/$_name/AGPL

	#removing unneeded
	rm $RPM_BUILD_ROOT/usr/share/java/esmska/esmska.exe

%clean
[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%post

%files
%defattr(-,root,root)
/usr/bin/esmska.sh
/usr/share/applications/esmska.desktop
/usr/share/java/esmska/esmska.conf
/usr/share/java/esmska/esmska.jar
/usr/share/java/esmska/esmska.sh
/usr/share/java/esmska/gateways/*
/usr/share/java/esmska/icons/esmska.icns
/usr/share/java/esmska/icons/esmska.ico
/usr/share/java/esmska/icons/esmska.png
/usr/share/java/esmska/icons/esmska.svg
/usr/share/java/esmska/lib/android-vcard-1.2.jar
/usr/share/java/esmska/lib/beansbinding-1.2.1.jar
/usr/share/java/esmska/lib/commons-beanutils-1.8.3.jar
/usr/share/java/esmska/lib/commons-cli-1.2.jar
/usr/share/java/esmska/lib/commons-codec-1.3.jar
/usr/share/java/esmska/lib/commons-collections-3.2.1.jar
/usr/share/java/esmska/lib/commons-httpclient-3.1.jar
/usr/share/java/esmska/lib/commons-io-1.4.jar
/usr/share/java/esmska/lib/commons-lang-2.6.jar
/usr/share/java/esmska/lib/commons-logging-1.1.1.jar
/usr/share/java/esmska/lib/ezmorph-1.0.6.jar
/usr/share/java/esmska/lib/javacsv-2.0.jar
/usr/share/java/esmska/lib/js-1.7R1.jar
/usr/share/java/esmska/lib/js-engine.jar
/usr/share/java/esmska/lib/json-lib-2.4-jdk15.jar
/usr/share/java/esmska/lib/looks-2.1.4.jar
/usr/share/java/esmska/lib/org-openide-awt.jar
/usr/share/java/esmska/lib/org-openide-util.jar
/usr/share/java/esmska/lib/substance-6.1.jar
/usr/share/java/esmska/lib/substance-extras-6.0.jar
/usr/share/java/esmska/lib/substance-swingx-6.0.jar
/usr/share/java/esmska/lib/swingx.jar
/usr/share/java/esmska/lib/trident-1.3.jar
/usr/share/java/esmska/license/gnu-agpl.txt
/usr/share/java/esmska/license/license.txt
/usr/share/java/esmska/readme.txt
/usr/share/licenses/AGPL
/usr/share/licenses/LICENSE
/usr/share/pixmaps/esmska.png

%changelog
* Sat Mar 25 2011 Mank <Mank1@seznam.cz> 0.0.1-1
- esmska: Version: 0.1.2
