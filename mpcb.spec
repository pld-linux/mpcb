Summary:	MultiPlatform networked ClipBoard
Summary(pl):	Przeno�ny sieciowy schowek
Name:		mpcb
Version:	0.4.2
Release:	1
License:	GPL
Group:		Applications/System
Group(de):	Applikationen/System
Group(pl):	Aplikacje/System
Source0:	ftp://ftp.idata.sk/pub/common/%{name}-%{version}.tgz
URL:		http://www.idata.sk/~robo/mpcb/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
Program for sharing clipboard over network between multiple stations
and even between X Window and Linux text console. Exist support for
X11 and Win32.

%description -l pl
Program do wsp�dzielenia "schowka" pomi�dzy wieloma stacjami, a nawet
pomi�dzy X Window, a konsol� tekstow�. Istnieje w wersji dla UNIX�w i
Win32.

%prep
%setup -q

%build
%configure2_13
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_sysconfdir}/X11/GNOME/CORBA/servers/,%{_datadir}/applets/Utility/}

%{__make} DESTDIR=$RPM_BUILD_ROOT install

install %{name}.gnorba $RPM_BUILD_ROOT%{_sysconfdir}/X11/GNOME/CORBA/servers/
install %{name}.desktop $RPM_BUILD_ROOT%{_datadir}/applets/Utility/

gzip -9nf AUTHORS ChangeLog NEWS README INSTALL mpcbrc.sample

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_sysconfdir}/X11/GNOME/CORBA/servers/*
%{_datadir}/applets/Utility/*