Summary:	MultiPlatform networked ClipBoard
Summary(pl.UTF-8):	Przenośny sieciowy schowek
Name:		mpcb
Version:	0.4.2
Release:	1
License:	GPL
Group:		Applications/System
Source0:	ftp://ftp.idata.sk/pub/common/%{name}-%{version}.tgz
# Source0-md5:	f21bda5d809e18adac774c08a973710e
URL:		http://www.idata.sk/~robo/mpcb/
BuildRequires:	XFree86-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program for sharing clipboard over network between multiple stations
and even between X Window and Linux text console. Exist support for
X11 and Win32.

%description -l pl.UTF-8
Program do współdzielenia "schowka" pomiędzy wieloma stacjami, a nawet
pomiędzy X Window, a konsolą tekstową. Istnieje w wersji dla Uniksów i
Win32.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-gnome
# applet-widget.h - gnome-core-devel (GNOME1)

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/X11/GNOME/CORBA/servers,%{_datadir}/applets/Utility}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{name}.gnorba $RPM_BUILD_ROOT%{_sysconfdir}/X11/GNOME/CORBA/servers
install %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applets/Utility

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README INSTALL mpcbrc.sample
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/X11/GNOME/CORBA/servers/*
%{_datadir}/applets/Utility/*
