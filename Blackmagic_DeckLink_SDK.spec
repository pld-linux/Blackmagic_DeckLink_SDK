# TODO: build examples? (BR: qt4, OpenGL)
Summary:	Blackmagic Design DeckLink SDK
Summary(pl.UTF-8):	Pakiet programistyczny (SDK) Blackmagic Design DeckLink
Name:		Blackmagic_DeckLink_SDK
Version:	10.0
Release:	2
License:	MIT
Group:		Development/Libraries
Source0:	http://software.blackmagicdesign.com/SDK/%{name}_%{version}.zip
# Source0-md5:	f0b066dcbfde813f7150309611d2210d
URL:		http://www.blackmagicdesign.com/support/sdks
#BuildRequires:	libstdc++-devel
#BuildRequires:	qt4-qmake
Requires:	libstdc++-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The DeckLink SDK provides a stable, cross-platform interface to
Blackmagic Design capture and playback products.

The SDK provides both low-level control of hardware and high-level
interfaces to allow developers to easily perform common tasks.

%description -l pl.UTF-8
DeckLink SDK dostarcza stabilny, wieloplatformowy interfejs do
urządzeń Blackmagic Design służących do przechwytywania i odtwarzania
obrazu.

SDK udostępnia zarówno niskopoziomowe interfejsy do sterowania
sprzętem, jak i wysokopoziomowe, pozwalające programistom łatwo
wykonywać popularne zadania.

%prep
%setup -q -n "Blackmagic DeckLink SDK %{version}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_includedir}/decklink

cp -p Linux/include/*.{h,cpp} $RPM_BUILD_ROOT%{_includedir}/decklink

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Blackmagic\ Decklink\ SDK.pdf ReadMe.rtf
%dir %{_includedir}/decklink
%{_includedir}/decklink/DeckLinkAPI*.h
%{_includedir}/decklink/LinuxCOM.h
%{_includedir}/decklink/DeckLinkAPIDispatch*.cpp
