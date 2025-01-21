#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Geo-IPfree
Version  : 1.160000
Release  : 29
URL      : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Geo-IPfree-1.160000.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/A/AT/ATOOMIC/Geo-IPfree-1.160000.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgeo-ipfree-perl/libgeo-ipfree-perl_1.151940-1.debian.tar.xz
Summary  : 'Geo::IPfree - Look up the country of an IPv4 address'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Geo-IPfree-license = %{version}-%{release}
Requires: perl-Geo-IPfree-perl = %{version}-%{release}
BuildRequires : buildreq-cpan

%description
This archive contains the distribution Geo-IPfree,
version 1.160000:
Geo::IPfree - Look up the country of an IPv4 address

%package dev
Summary: dev components for the perl-Geo-IPfree package.
Group: Development
Provides: perl-Geo-IPfree-devel = %{version}-%{release}
Requires: perl-Geo-IPfree = %{version}-%{release}

%description dev
dev components for the perl-Geo-IPfree package.


%package license
Summary: license components for the perl-Geo-IPfree package.
Group: Default

%description license
license components for the perl-Geo-IPfree package.


%package perl
Summary: perl components for the perl-Geo-IPfree package.
Group: Default
Requires: perl-Geo-IPfree = %{version}-%{release}

%description perl
perl components for the perl-Geo-IPfree package.


%prep
%setup -q -n Geo-IPfree-1.160000
cd %{_builddir}
tar xf %{_sourcedir}/libgeo-ipfree-perl_1.151940-1.debian.tar.xz
cd %{_builddir}/Geo-IPfree-1.160000
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/Geo-IPfree-1.160000/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Geo-IPfree
cp %{_builddir}/Geo-IPfree-1.160000/LICENSE %{buildroot}/usr/share/package-licenses/perl-Geo-IPfree/d86b9ffe2c1d685f4bf674e8905bd284f3d33703
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Geo::IPfree.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Geo-IPfree/d86b9ffe2c1d685f4bf674e8905bd284f3d33703

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
