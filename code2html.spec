%define name code2html
%define version 0.9.1
%define release %mkrel 9

Summary:	Converts a program source code to syntax highlighted HTML
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Source:		ftp://code2html.sourceforge.net/pub/code2html/all/%{name}-%{version}.tar.bz2
URL:		http://www.palfrader.org/code2html/
BuildRoot:	%{_tmppath}/%{name}-buildroot
Buildarch:	noarch

%description
code2html is a perlscript which converts a program source code to syntax
highlighted HTML. It may be called from the command line or as a CGI script.
It can also handle include commands in HTML files.
Currently supports: Ada 95, C, C++, HTML, Java, JavaScript, Makefile,
Pascal, Perl, SQL, AWK, M4, and Groff. 

%prep

%setup -q

%install
rm -rf $RPM_BUILD_ROOT

mkdir -p $RPM_BUILD_ROOT%{_bindir}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
install -m 755 %{name} $RPM_BUILD_ROOT%{_bindir}/
install -m 644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc CREDITS ChangeLog INSTALL LICENSE README
%{_bindir}/*
%{_mandir}/man1/%{name}.1*



%changelog
* Thu Dec 09 2010 Oden Eriksson <oeriksson@mandriva.com> 0.9.1-9mdv2011.0
+ Revision: 617401
- the mass rebuild of 2010.0 packages

* Wed Sep 02 2009 Thierry Vignaud <tv@mandriva.org> 0.9.1-8mdv2010.0
+ Revision: 424908
- rebuild

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-7mdv2009.0
+ Revision: 243587
- rebuild

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.9.1-5mdv2008.1
+ Revision: 136330
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import code2html


* Thu Aug 03 2006 Lenny Cartier <lenny@mandriva.com> 0.9.1-5mdv2007.0
- rebuild

* Fri Apr 22 2005 Lenny Cartier <lenny@mandriva.com> 0.9.1-4mdk
- rebuild

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-3mdk
- rebuild

* Fri Jan 24 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-2mdk
- rebuild

* Mon Jan 14 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.9.1-1mdk
- 0.9.1

* Thu Jun 28 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.9-1mdk
- updated to 0.9

* Mon Jan 08 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.8.12-2mdk 
- new url

* Thu Nov 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.8.12-1mdk
- updated to 0.8.12

* Mon Oct 02 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.8.11-1mdk
	Sun Sep 30 2000 Guillaume Rousse <g.rousse@linux-mandrake.com> 0.8.11-1mdk
	- 0.8.11
	- add URL tag
	- documentation
	- man page

* Tue Aug 29 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.8.0-3mdk
- BM

* Tue Apr 25 2000 Lenny Cartier <lenny@mandrakesoft.com> 0.8.0-2mdk
- fix group

* Wed Aug 18 1999 Thierry Vignaud <tvignaud@mandrakesoft.com>
- initial spec

