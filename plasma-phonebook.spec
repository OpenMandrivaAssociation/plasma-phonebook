#define snapshot 20200710
#define commit 869a837079fc60c9d976528d6a9ce3dce19790d0

Name:		plasma-phonebook
Version:	24.02.0
Release:	%{?snapshot:0.%{snapshot}.}1
Summary:	Phone book application for Plasma Mobile
Source0:	https://invent.kde.org/plasma-mobile/plasma-phonebook/-/archive/v%{version}/plasma-phonebook-v%{version}.tar.bz2
License:	GPLv3
Group:		Applications/Productivity
BuildSystem:	cmake
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt6Core)
BuildRequires:	cmake(Qt6Quick)
BuildRequires:	cmake(Qt6Test)
BuildRequires:	cmake(Qt6Gui)
BuildRequires:	cmake(Qt6Svg)
BuildRequires:	cmake(Qt6QuickControls2)
BuildRequires:	cmake(KF6CoreAddons)
BuildRequires:	cmake(KF6Kirigami2)
BuildRequires:	cmake(KF6People)
BuildRequires:	cmake(KF6Contacts)

%description
Phone book application for Plasma Mobile

%files -f %{name}.lang
%{_bindir}/plasma-phonebook
%{_qtdir}/plugins/kpeople/actions/phonebook_kpeople_plugin.so
%{_datadir}/applications/org.kde.phonebook.desktop
%{_datadir}/icons/hicolor/scalable/apps/org.kde.phonebook.svg
%{_datadir}/metainfo/org.kde.phonebook.metainfo.xml
