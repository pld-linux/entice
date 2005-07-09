Summary:	Image viewer using Enlightenment libraries
Summary(pl):	Przegl±darka obrazków u¿ywaj±ca bibliotek Enlightenmenta
Name:		entice
Version:	0.9.1
%define _snap	20050701
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Window Managers/Tools
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/snaps/enli/e17/apps/%{name}-%{_snap}.tar.gz
# Source0-md5:	3b1d9e40558ebc803efc7b2fd9e7df42
Patch0:		%{name}-no_buildtime_gimp.patch
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esmart-devel
BuildRequires:	libtool
Requires:	/usr/bin/gimp-remote
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Entice is an image viewer using Enlightenment libraries. Entice
currently takes no commandline options. It takes as arguments a list
of images to load. Run with no arguments it tries to load all files
from the working directory (currently it even tries files that aren't
images). You can instead give a directory name as a single argument,
and it will load all images from this directory.

%description -l pl
Entice to przegl±darka obrazków u¿ywaj±ca bibliotek Enlightenmenta.
Entice aktualnie nie pobiera ¿adnych opcji z linii poleceñ, przyjmuje
tylko listê obrazków do wczytania jako parametry. Uruchomiona bez
parametrów próbuje wczytaæ wszystkie pliki z bie¿±cego katalogu (w tej
chwili nawet te, które nie s± obrazkami). Mo¿na podaæ nazwê katalogu
jako pojedynczy argument - wtedy przegl±darka wczyta wszystkie obrazki
z tego katalogu.

%prep
%setup -q -n %{name}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
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
%doc AUTHORS ChangeLog COPYING README
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
