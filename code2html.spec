%define name code2html
%define version 0.9.1
%define release %mkrel 5

Summary:	Converts a program source code to syntax highlighted HTML
Name:		%{name}
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Development/Other
Source:		ftp://code2html.sourceforge.net/pub/code2html/all/%{name}-%{version}.tar.bz2
URL:		http://www.palfrader.org/code2html/
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

