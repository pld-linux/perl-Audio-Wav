#
# Conditional build:
# _without_tests - do not perform "make test"
%include	/usr/lib/rpm/macros.perl
%define		pdir	Audio
%define		pnam	Wav
Summary:	Audio::Wav - Perl modules for reading and writing WAV files
Summary(pl):	Audio::Wav - modu³y Perla do odczytu i zapisu plików WAV
Name:		perl-Audio-Wav
Version:	0.02
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
These modules provide a method of reading and writing uncompressed WAV
files.

%description -l pl
Te modu³y udostêpniaj± mo¿liwo¶æ odczytu i zapisu nieskompresowanych
plików WAV.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/Audio/Wav.pm
%{perl_sitelib}/Audio/Wav
%{_mandir}/man3/*
