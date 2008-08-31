%define realname   Gtk2-WebKit
%define version    0.03
%define release    %mkrel 1

Name:       perl-%{realname}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Web content engine library for Gtk2
Source:     http://www.cpan.org/modules/by-module/Gtk2/%{realname}-%{version}.tar.gz
Url:        http://search.cpan.org/dist/%{realname}
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires: webkitgtk-devel
BuildRequires: perl-devel
BuildRequires: perl(ExtUtils::Depends)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(Gtk2)
# for tests:
BuildRequires: x11-server-xvfb

%description
WebKit is a web content engine, derived from KHTML and KJS from KDE, and
used primarily in Apple's Safari browser. It is made to be embedded in
other applications, such as mail readers, or web browsers.

It is able to display content such as HTML, SVG, XML, and others. It also
supports DOM, XMLHttpRequest, XSLT, CSS, Javascript/ECMAscript and more.

%prep
%setup -q -n %{realname}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

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
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


