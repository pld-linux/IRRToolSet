Summary:	IRRToolSet is a suite of policy analysis tools
Summary(pl):	IRRToolSet jest zestawem narzêdzi do analizy polityki
Name:		IRRToolSet
Version:	4.7.3
Release:	3
License:	BSD-like
Group:		Networking/Admin
Source0:	ftp://ftp.ripe.net/ripe/tools/IRRToolSet/%{name}-%{version}.tar.gz
# Source0-md5:	fcf8305464c8ae5886c41dcb8d85e53d
Patch0:		%{name}-DESTDIR.patch
Patch1:		%{name}-gcc3.patch
Patch2:		%{name}-flex.patch
URL:		http://www.ripe.net/ripencc/pub-services/db/irrtoolset/index.html
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

%description -l pl
IRRToolSet jest zestawem narzêdzi do analizy polityki.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
