#
# Conditional build:
%bcond_without	tests	# Do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Crypt
%define	pnam	Anubis
Summary:	Crypt::Anubis - Crypt::CBC-compliant block cipher
Summary(pl):	Crypt::Abubis - szyfr blokowy kompatybilny z Crypt::CBC
Name:		perl-Crypt-Anubis
Version:	1.0.4
Release:	1
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	aa62fb3a199063b5dff8bcbfc632338e
BuildRequires:	perl-devel >= 5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Anubis is a variable-length key, 128-bit block cipher designed by
Vincent Rijmen and Paulo S. L. M. Barreto. Key length can be 128, 160,
192, 224, 256, 288, or 320 bits. The default key length used in this
implementation is 128 bits (16 bytes). This module supports the
Crypt::CBC interface.

%description -l pl
Anubis to 128-bitowy szyfr blokowy o zmiennej d³ugo¶ci klucza
opracowany przez Vincenta Rijmena i Paulo S. L. M. Baretto. Klucz mo¿e
mieæ d³ugo¶æ 128, 160, 192, 224, 256, 228 lub 320 bitów. Domy¶lna
d³ugo¶æ klucza w tej implementacji to 128 bitów (16 bajtów). Ten modu³
obs³uguje interfejs Crypt::CBC.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor

%{__make} OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

cd examples
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
for f in * ; do
	sed -e "s@#!/usr/local/bin/perl@#!/usr/bin/perl@" $f \
		> $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}/$f
done

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorarch}/Crypt/Anubis.pm
%dir %{perl_vendorarch}/auto/Crypt/Anubis
%{perl_vendorarch}/auto/Crypt/Anubis/Anubis.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Crypt/Anubis/Anubis.so
%{_mandir}/man3/*
%attr(755,root,root) %{_examplesdir}/%{name}-%{version}
