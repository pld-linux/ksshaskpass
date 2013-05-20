Summary:	OpenSSH KDE4 passphrase dialog with KWallet support
Name:		ksshaskpass
Version:	0.5.3
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://kde-apps.org/CONTENT/content-files/50971-%{name}-%{version}.tar.gz
# Source0-md5:	05dad7745e9d92b08bd86e7ab7a9540d
URL:		http://kde-apps.org/content/show.php/Ksshaskpass?content=50971
BuildRequires:	cmake
BuildRequires:	kde4-kdelibs-devel
Requires:	openssh-clients
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is an KDE4-based passphrase dialog with KWallet support for use
with OpenSSH.

%prep
%setup -q

%build
install -d build
cd build
%cmake \
	..

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%attr(755,root,root) %{_bindir}/ksshaskpass
%{_desktopdir}/kde4/ksshaskpass.desktop
%{_mandir}/man1/ksshaskpass.1*
