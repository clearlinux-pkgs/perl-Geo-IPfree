#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Geo-IPfree
Version  : 1.151940
Release  : 4
URL      : https://cpan.metacpan.org/authors/id/B/BR/BRICAS/Geo-IPfree-1.151940.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BR/BRICAS/Geo-IPfree-1.151940.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libg/libgeo-ipfree-perl/libgeo-ipfree-perl_1.151940-1.debian.tar.xz
Summary  : 'Look up the country of an IPv4 address'
Group    : Development/Tools
License  : Artistic-1.0-Perl
BuildRequires : buildreq-cpan

%description
NAME
Geo::IPfree - Look up the country of an IPv4 address
SYNOPSIS
use Geo::IPfree;

my $geo = Geo::IPfree->new;
my( $code1, $name1 ) = $geo->LookUp( '200.176.3.142' );

# use memory to speed things up
$geo->Faster;

# lookup by hostname
my( $code2, $name2, $ip2 ) = $geo->LookUp( 'www.cnn.com' );

%package dev
Summary: dev components for the perl-Geo-IPfree package.
Group: Development
Provides: perl-Geo-IPfree-devel = %{version}-%{release}

%description dev
dev components for the perl-Geo-IPfree package.


%prep
%setup -q -n Geo-IPfree-1.151940
cd ..
%setup -q -T -D -n Geo-IPfree-1.151940 -b 1
mkdir -p deblicense/
mv %{_topdir}/BUILD/debian/* %{_topdir}/BUILD/Geo-IPfree-1.151940/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
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
/usr/lib/perl5/vendor_perl/5.28.0/Geo/IPfree.pm
/usr/lib/perl5/vendor_perl/5.28.0/Geo/ipscountry.dat

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Geo::IPfree.3
