Summary:	Image viewer using enlightenment libraries
Name:		entice
Version:	0.9.1
%define _snap	20050105
Release:	0.%{_snap}.0.1
License:	BSD
Group:		X11/Window Managers
#Source0:	http://dl.sourceforge.net/enlightenment/%{name}-%{version}.tar.gz
Source0:	ftp://ftp.sparky.homelinux.org/pub/e17/%{name}-%{version}-%{_snap}.tar.gz
# Source0-md5:	44b576acbe2327b22bb9b06bb8c70327
URL:		http://enlightenment.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	esmart-devel
BuildRequires:	/usr/bin/gimp-remote-2.2
BuildRequires:	libtool
Requires:	/usr/bin/gimp-remote-2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Entice is an image viewer using enlightenment libraries. Entice
currently takes no commandline options. It takes as arguments a list
of images to load. Run with no arguments it tries to load all files
from the working directory (currently it even tries files that aren't
images). You can instead give a directory name as a single argument,
and it will load all images from this directory.

%prep
%setup -q -n %{name}
sed 's/gimp-remote-2.0/gimp-remote-2.2/' \
	-i configure.in

%build
%{__libtoolize}
%{__aclocal}
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