%bcond check 1

# prevent library files from being installed
%global cargo_install_lib 0

Name:           gst-plugin-bigeye
Version:        0.1.1
Release:        %autorelease
Summary:        Rust Tutorial Plugin

SourceLicense:  Apache-2.0
License:        LICENSE

URL:            https://github.com/Banakin/gst-plugin-bigeye

Source: https://github.com/Banakin/gst-plugin-bigeye/archive/refs/tags/v%{version}.tar.gz
Source: gst-plugin-bigeye-0.1.0-vendor.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  clang
BuildRequires:  libuvc-devel
BuildRequires:  cargo-rpm-macros >= 26
Requires:       libuvc

%global _description %{expand:
Bigscreen Beyond 2e eye tracking video source using libuvc. Plugin is not affiliated with Bigscreen.}

%description %{_description}

%prep
%autosetup -n gst-plugin-bigeye-%{commit} -p1 -a1
%cargo_prep -v vendor

%build
%cargo_build
%{cargo_license_summary}
%{cargo_license} > LICENSE.dependencies
%{cargo_vendor_manifest}

%install
install -d %{buildroot}%{_libdir}/gstreamer-1.0

%global _publishfile libgstbigeye.so
cp target/release/%{_publishfile} %{buildroot}%{_libdir}/gstreamer-1.0/%{_publishfile}

%if %{with check}
%check
%cargo_test
%endif

%files
%{_libdir}/gstreamer-1.0/%{_publishfile}
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md

%changelog
%autochangelog
