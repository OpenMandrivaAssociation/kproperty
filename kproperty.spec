%define major 4
%define libname %mklibname KPropertyCore3 %{major}
%define devname %mklibname KPropertyCore -d
%define olibname %mklibname KPropertyCore3 3

%define wlibname %mklibname KPropertyWidgets3 %{major}
%define wdevname %mklibname KPropertyWidgets -d
%define owlibname %mklibname KpropertyWidgets3 3

Name:		kproperty
Version:	3.1.0
Release:	1
Source0:	http://download.kde.org/stable/%{name}/src/%{name}-%{version}.tar.xz
Summary:	A property editing framework with editor widget
URL:		http://community.kde.org/KReport
License:	LGPLv2+
Group:		System/Libraries
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(Qt5Core)
BuildRequires:	cmake(Qt5Gui)
BuildRequires:	cmake(Qt5Widgets)
BuildRequires:	cmake(Qt5Xml)
BuildRequires:	cmake(Qt5Test)
BuildRequires:	cmake(Qt5Network)
BuildRequires:	cmake(KF5I18n)
BuildRequires:	cmake(KF5CoreAddons)
BuildRequires:	cmake(KF5GuiAddons)
BuildRequires:	cmake(KF5WidgetsAddons)
BuildRequires:	cmake(KF5Config)
BuildRequires:	cmake(KF5I18n)
Requires:	%{libname} = %{EVRD}

%description
A property editing framework with editor widget

%package -n %{libname}
Summary: A property editing framework with editor widget
Group: System/Libraries
Requires: %{name} = %{EVRD}
Obsoletes:  %{olibname}

%description -n %{libname}
A property editing framework with editor widget

%package -n %{wlibname}
Summary: A property editing framework with editor widget
Group: System/Libraries
Requires: %{name} = %{EVRD}
Requires: %{libname} = %{EVRD}
Obsoletes: %{owlibname}

%description -n %{wlibname}
A property editing framework with editor widget

%package -n %{devname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{libname} = %{EVRD}

%description -n %{devname}
Development files (Headers etc.) for %{name}.

KProperty is a property editing framework with editor widget.

%package -n %{wdevname}
Summary: Development files for %{name}
Group: Development/C
Requires: %{wlibname} = %{EVRD}
Requires: %{devname} = %{EVRD}

%description -n %{wdevname}
Development files (Headers etc.) for %{name}.

KProperty is a property editing framework with editor widget.

%prep
%setup -q
%apply_patches
%cmake_kde5

%build
%ninja -C build

%install
%ninja_install -C build
%find_lang kproperty --with-qt --all-name

%files -f kproperty.lang
%{_datadir}/kpropertywidgets3

%files -n %{libname}
%{_libdir}/*Core*.so.%{major}*

%files -n %{wlibname}
%{_libdir}/*Widgets*.so.%{major}*

%files -n %{devname}
%{_includedir}/KPropertyCore3
%{_libdir}/*Core*.so
%{_libdir}/pkgconfig/*Core*
%{_libdir}/cmake/KPropertyCore3

%files -n %{wdevname}
%{_includedir}/KPropertyWidgets3
%{_libdir}/*Widgets*.so
%{_libdir}/pkgconfig/*Widgets*
%{_libdir}/cmake/KPropertyWidgets3
