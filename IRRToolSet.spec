Summary:	IRRToolSet is a suite of policy analysis tools
Summary(pl.UTF-8):	IRRToolSet jest zestawem narzędzi do analizy polityki
Name:		IRRToolSet
Version:	4.8.5
Release:	1
License:	BSD-like
Group:		Networking/Admin
Source0:	ftp://ftp.isc.org/isc/IRRToolSet/%{name}-%{version}/IRRToolSet-%{version}.tar.gz
# Source0-md5:	30003e1c0403462d7e0148bca0674062
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-flex.patch
Patch2:		%{name}-gcc3.patch
URL:		http://www.isc.org/sw/IRRToolSet/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	tcl-devel >= 8.3.4-10
BuildRequires:	tk-devel >= 8.3.4-5
BuildRequires:	readline-devel
Provides:	RAToolSet
Obsoletes:	RAToolSet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IRRToolSet is a suite of policy analysis tools. It is implemented in
C++ on a UNIX platform.

%description -l pl.UTF-8
IRRToolSet jest zestawem narzędzi do analizy polityki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
cp -f /usr/share/automake/config.sub .
cp -f /usr/share/automake/config.sub src/Core/.aux
cp -f /usr/share/automake/config.sub src/rpsl
%configure
%{__make}

# extract license
head -n 53 acconfig.h | tail -n 52 > LICENSE

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

#mv $RPM_BUILD_ROOT%{_bindir}/prtraceroute $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README* LICENSE
%attr(755,root,root) %{_bindir}/*
#%attr(4754,root,adm) %{_sbindir}/prtraceroute
%{_mandir}/man1/*
%{_mandir}/man3/*
