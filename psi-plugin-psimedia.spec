%define	orgname	psimedia
Summary:	Audio and Video plugin for PSI
Name:		psi-plugin-psimedia
Version:	1.0.3
Release:	1
License:	LGPL v2.1+
Group:		Applications/Communications
Source0:	http://delta.affinix.com/download/psimedia/psimedia-%{version}.tar.bz2
# Source0-md5:	ddc1a2a35dc155ca46ad6ecaeccdf894
URL:		http://delta.affinix.com/psimedia/
BuildRequires:	QtCore-devel >= 4.5.0
BuildRequires:	glib2-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	liboil-devel
BuildRequires:	speex-devel
Requires:	psi >= 0.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PsiMedia is a thick abstraction layer for providing audio and video
RTP services to Psi-like IM clients.

%prep
%setup -q -n %{orgname}-%{version}

%build
./configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_libdir}/psi/plugins

install gstprovider/libgstprovider.so $RPM_BUILD_ROOT%{_libdir}/psi/plugins

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc TODO
%attr(755,root,root) %{_libdir}/psi/plugins/*.so