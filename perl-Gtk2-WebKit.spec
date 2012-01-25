%define upstream_name    Gtk2-WebKit
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	6

Summary:    Web content engine library for Gtk2
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Gtk2/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Gtk2)
BuildRequires: webkitgtk-devel >= 1.2.0-3
# for tests:
BuildRequires: x11-server-xvfb
BuildRequires: perl-devel
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE, and
used primarily in Apple's Safari browser. It is made to be embedded in
other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It also
supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and more.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make OTHERLDFLAGS="-Wl,--as-needed"

#%check
#XDISPLAY=$(i=1; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
#%{_bindir}/Xvfb -screen 0 1600x1200x24 :$XDISPLAY &
#export DISPLAY=:$XDISPLAY
#make test
#kill $(cat /tmp/.X$XDISPLAY-lock)

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes
%{_mandir}/man3/*
%perl_vendorlib/*

