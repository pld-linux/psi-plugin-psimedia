%define	orgname	psimedia
Summary:	Audio and Video plugin for PSI
Name:		psi-plugin-psimedia
Version:	1.0.3
Release:	5
License:	LGPL v2.1+
Group:		Applications/Communications
Source0:	http://delta.affinix.com/download/psimedia/psimedia-%{version}.tar.bz2
# Source0-md5:	1be71c37d71c655ffc2c53cf86c77a7a
Patch0:		%{orgname}-2.6.38.patch
Patch1:		%{orgname}-drop-v4l.patch
Patch2:		glib2.patch
URL:		http://delta.affinix.com/psimedia/
BuildRequires:	QtCore-devel >= 4.5.0
BuildRequires:	QtGui-devel
BuildRequires:	QtNetwork-devel
BuildRequires:	glib2-devel
BuildRequires:	gstreamer-plugins-base-devel
BuildRequires:	liboil-devel
BuildRequires:	pkgconfig
BuildRequires:	qt4-qmake
BuildRequires:	qt4-build
BuildRequires:	speex-devel
BuildRequires:	speexdsp-devel
BuildRequires:	which
Requires:	gstreamer-audio-effects-base
Requires:	gstreamer-audio-effects-good
Requires:	gstreamer-audiosink-alsa
Requires:	gstreamer-plugins-base
Requires:	gstreamer-plugins-good
Requires:	gstreamer-speex
Requires:	gstreamer-theora
Requires:	gstreamer-video-effects
Requires:	gstreamer-vorbis
Requires:	psi >= 0.13
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
PsiMedia is a thick abstraction layer for providing audio and video
RTP services to Psi-like IM clients.

%prep
%setup -q -n %{orgname}-%{version}
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
