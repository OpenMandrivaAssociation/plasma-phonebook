#define snapshot 20200710
#define commit 869a837079fc60c9d976528d6a9ce3dce19790d0

Name:		plasma-phonebook
Version:	0.1
Release:	%{?snapshot:0.%{snapshot}.}2
Summary:	Phone book application for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/plasma-phonebook/-/archive/v%{version}/plasma-phonebook-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Quick)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Svg)
BuildRequires:	cmake(Qt5QuickControls2)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5Kirigami2)
BuildRequires:	cmake(KF5People)
BuildRequires:	cmake(KF5Contacts)
BuildRequires:	cmake(KF5PeopleVCard)

%description
Phone book application for Plasma Mobile

%prep
%autosetup -p1 -n plasma-phonebook-v%{version}
%cmake_kde5 -G Ninja

%build
%ninja_build -C build

%install
%ninja_install -C build

%files
%{_bindir}/plasma-phonebook
%{_libdir}/qt5/plugins/kpeople/actions/phonebook_kpeople_plugin.so
%{_datadir}/applications/org.kde.phonebook.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.phonebook.svg
%{_datadir}/metainfo/org.kde.phonebook.metainfo.xml
