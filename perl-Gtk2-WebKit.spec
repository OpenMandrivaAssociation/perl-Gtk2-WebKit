%define upstream_name    Gtk2-WebKit
%define upstream_version 0.09

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:	7

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



%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.90.0-6
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

  + Oden Eriksson <oeriksson@mandriva.com>
    - rebuilt for perl-5.14.2
    - rebuilt for perl-5.14.x

* Mon Jun 20 2011 Funda Wang <fwang@mandriva.org> 0.90.0-3
+ Revision: 686116
- rebuild for new webkit

* Sun Jun 19 2011 Funda Wang <fwang@mandriva.org> 0.90.0-2
+ Revision: 685979
- build with correct flags

* Sat May 14 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.90.0-1
+ Revision: 674661
- update to new version 0.09

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 0.80.0-5
+ Revision: 667191
- mass rebuild

* Sun Apr 03 2011 Funda Wang <fwang@mandriva.org> 0.80.0-4
+ Revision: 650029
- rebuild

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 0.80.0-3mdv2011.0
+ Revision: 564518
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-2mdv2011.0
+ Revision: 555931
- rebuild for perl 5.12

* Wed Jul 14 2010 Jérôme Quelin <jquelin@mandriva.org> 0.80.0-1mdv2011.0
+ Revision: 553131
- update to 0.08

* Wed May 19 2010 Olivier Blin <blino@mandriva.org> 0.70.0-2mdv2010.1
+ Revision: 545319
- rebuild with latest webkit to expose allow-scripts-to-close-windows property (needed by first time wizard)

* Fri Nov 06 2009 Jérôme Quelin <jquelin@mandriva.org> 0.70.0-1mdv2010.1
+ Revision: 461284
- update to 0.07

* Fri Jul 24 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 399303
- update to 0.06
- using %%perl_convert_version
- fixed license field

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2010.0
+ Revision: 392988
- update to new version 0.05

* Thu Mar 12 2009 Frederik Himpe <fhimpe@mandriva.org> 0.04-2mdv2009.1
+ Revision: 354375
- Rebuild for new webkit major

* Tue Dec 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.04-1mdv2009.1
+ Revision: 314750
- update to new version 0.04

* Sun Aug 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.03-1mdv2009.0
+ Revision: 277949
- update to new version 0.03

* Mon Aug 04 2008 Thierry Vignaud <tv@mandriva.org> 0.02-1mdv2009.0
+ Revision: 263326
- BuildRequires webkitgtk-devel
- import perl-Gtk2-WebKit


* Mon Aug 04 2008 Thierry Vignaud <tvignaud@mandriva.com> 0.02-1mdv2009.0
- initial mdv release, generated with cpan2dist


