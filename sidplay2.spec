Summary:	Sidplay - SID-chip emulator for playing Commodore 64 music
Summary(pl):	Sidplay - emulator uk³adu SID s³u¿±cego do odgrywania muzyki w Commodore 64
Name:		sidplay2
Version:	2.0.9
Release:	1
License:	GPL v2
Group:		X11/Applications
Source0:	http://dl.sourceforge.net/sidplay2/sidplay-%{version}.tar.gz
# Source0-md5:	8b0449e501ba8e684f718dce9b77c5a5
URL:		http://sidplay2.sourceforge.net/
BuildRequires:	libsidplay2-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sidplay 2 is the second in the Sidplay series originally developed by
Michael Schwendt. This version is written by Simon White and is cycle
accurate for improved sound reproduction. Sidplay 2 is capable of
playing all C64 mono and stereo file formats.

%description -l pl
Sidplay 2 to druga wersja serii Sidplay oryginalnie rozwijanej przez
Michaela Schwendta. Ta wersja zosta³a napisana przez Simona White'a i
bardzo wiernie oddaje d¼wiêk. Sidplay 2 jest zdolny do grania
wszystkich formatów mono i stereo z C64. Ogromna kolekcja muzyki SID
dostêpna jest na <http://www.hvsc.c64.org/>.

%prep
%setup -q -n sidplay-%{version}

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/%{name}.*
