%bcond check 1

# prevent library files from being installed
%global cargo_install_lib 0

Name:           gst-plugin-bigeye
Version:        0.1.0
Release:        %autorelease
Summary:        Rust Tutorial Plugin

SourceLicense:  Apache-2.0
License:        LICENSE

URL:            https://github.com/Banakin/gst-plugin-bigeye

%global commit 1e13936eb8a62c152e8575808515d60f205790d6
%global gittag HEAD
%global shortcommit %(c=%{commit}; echo ${c:0:7})
Source: https://github.com/Banakin/gst-plugin-bigeye/archive/%{commit}/%{name}-%{shortcommit}.tar.gz
Source: gst-plugin-bigeye-0.1.0-vendor.tar.xz

BuildRequires:  glib2-devel
BuildRequires:  gstreamer1-plugins-base-devel
BuildRequires:  clang
BuildRequires:  libuvc-devel
BuildRequires:  cargo-rpm-macros >= 26
Requires:       libuvc

%global _description %{expand:
Rust Tutorial Plugin.}

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
install -d %{buildroot}/lib64/gstreamer-1.0
install -d %{buildroot}/lib/gstreamer-1.0

%global _publishfile target/release/libgstbigeye.so
cp %{_publishfile} %{buildroot}/lib/gstreamer-1.0
cp %{_publishfile} %{buildroot}/lib64/gstreamer-1.0

%if %{with check}
%check
%cargo_test
%endif

%files
%license LICENSE
%license LICENSE.dependencies
%license cargo-vendor.txt
%doc README.md

%changelog
%autochangelog
