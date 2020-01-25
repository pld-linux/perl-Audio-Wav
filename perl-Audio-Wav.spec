#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%define		pdir	Audio
%define		pnam	Wav
Summary:	Audio::Wav - Perl modules for reading and writing WAV files
Summary(pl.UTF-8):	Audio::Wav - moduły Perla do odczytu i zapisu plików WAV
Name:		perl-Audio-Wav
Version:	0.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Audio/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	06530e12542afb7fb3354ee5419a6dc4
URL:		http://search.cpan.org/dist/Audio-Wav/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These modules provide a method of reading and writing uncompressed WAV
files.

%description -l pl.UTF-8
Te moduły udostępniają możliwość odczytu i zapisu nieskompresowanych
plików WAV.

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
