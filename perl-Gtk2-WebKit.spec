%define modname	Gtk2-WebKit
%define modver	0.09

Summary:	Web content engine library for Gtk2
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	23
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Gtk2/%{modname}-%{modver}.tar.gz
Source1:	perl-Gtk2-WebKit.rpmlintrc
BuildRequires:	perl(ExtUtils::Depends)
BuildRequires:	perl(ExtUtils::PkgConfig)
BuildRequires:	perl(Gtk2)
BuildRequires:	webkitgtk-devel >= 1.2.0-3
# for tests:
BuildRequires:	x11-server-xvfb
BuildRequires:	perl-devel

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE, and
used primarily in Apple's Safari browser. It is made to be embedded in
other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It also
supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and more.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make OTHERLDFLAGS="-Wl,--as-needed"

#%check
#XDISPLAY=$(i=1; while [ -f /tmp/.X$i-lock ]; do i=$(($i+1)); done; echo $i)
#%{_bindir}/Xvfb -screen 0 1600x1200x24 :$XDISPLAY &
#export DISPLAY=:$XDISPLAY
#make test
#kill $(cat /tmp/.X$XDISPLAY-lock)

%install
%make_install

%files
%doc Changes
%{perl_vendorlib}/*
%doc %{_mandir}/man3/*

