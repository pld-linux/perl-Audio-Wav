#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Wav
Summary:	Audio::Wav - Perl modules for reading and writing WAV files
Summary(pl):	Audio::Wav - modu�y Perla do odczytu i zapisu plik�w WAV
Name:		perl-Audio-Wav
Version:	0.05
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d67557a5c605057aedb0cff3685ed597
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These modules provide a method of reading and writing uncompressed WAV
files.

%description -l pl
Te modu�y udost�pniaj� mo�liwo�� odczytu i zapisu nieskompresowanych
plik�w WAV.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Audio/Wav.pm
%{perl_vendorlib}/Audio/Wav
%{_mandir}/man3/*
