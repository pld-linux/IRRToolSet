Summary:	IRRToolSet is a suite of policy analysis tools
Summary(pl):	IRRToolSet jest zestawem narz�dzi do analizy polityki
Name:		IRRToolSet
Version:	4.8.2
Release:	0.1
License:	BSD-like
Group:		Networking/Admin
Source0:	ftp://ftp.isc.org/isc/IRRToolSet/%{name}-%{version}/IRRToolSet-%{version}.tar.gz
# Source0-md5:	04c24da4f3338a92d60ed055518c26a6
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-flex.patch
Patch2:		%{name}-build-all.patch
Patch3:		NE.cc-20040805.patch
URL:		http://www.isc.org/sw/IRRToolSet/
BuildRequires:	XFree86-devel
BuildRequires:	automake
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	libstdc++-devel
BuildRequires:	tcl-devel >= 8.3.4-10
BuildRequires:	tk-devel >= 8.3.4-5
BuildRequires:	readline-devel
%if %{with gcc32}
BuildRequires:	compat-gcc-32
BuildRequires:	compat-gcc-32-c++
%endif
Provides:	RAToolSet
Obsoletes:	RAToolSet
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
IRRToolSet is a suite of policy analysis tools. It is implemented in
C++ on a UNIX platform.

%description -l pl
IRRToolSet jest zestawem narz�dzi do analizy polityki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1
%patch3 -p1

%build
cp -f /usr/share/automake/config.sub .
%configure2_13
%{__make}

# extract license
head -n 53 acconfig.h | tail -n 52 > LICENSE

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_sbindir}

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT%{_bindir}/prtraceroute $RPM_BUILD_ROOT%{_sbindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README* LICENSE
%attr(755,root,root) %{_bindir}/*
%attr(4754,root,adm) %{_sbindir}/*
%{_mandir}/man1/*
%{_mandir}/man3/*
