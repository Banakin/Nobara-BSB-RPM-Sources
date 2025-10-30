%global debug_package %{nil}

Name:           baballonia-nvidia
Version:        1.1.0.8
Release:        1%{?dist}
Summary:        A cross-platform, hardware-agnostic VR eye and face tracking application.

License:        Babble Software Distribution License 1.0
URL:            https://github.com/Project-Babble/Baballonia

%global commit 43b3af174be0d922736e9218cced2b9070b38164
%global gittag v1.1.0.8
%global shortcommit %(c=%{commit}; echo ${c:0:7})
## We fetch sources from git in %prep (includes submodules). The upstream GitHub auto-archive
## does not include submodule contents, so we clone the repo with submodules here.

BuildRequires:  dotnet-sdk-8.0
BuildRequires:  git
BuildRequires:  ca-certificates
BuildRequires:  cudnn9-cuda-12
Requires:       dotnet-runtime-8.0
Requires:       lttng-ust
Requires:       cudnn9-cuda-12

Patch0:        baballonia-nvidia.patch

%description
Baballonia is a cross-platform, hardware-agnostic VR eye and face tracking application.

%prep
%setup -c -T
rm -rf PROJECT-%{commit}
git clone --branch %{gittag} --recurse-submodules https://github.com/Project-Babble/Baballonia.git PROJECT-%{commit}

# Move repository contents into the current build root so paths like "src/Baballonia.Desktop/..." match
cp -a PROJECT-%{commit}/. ./
pushd PROJECT-%{commit} >/dev/null

# Ensure the exact commit is checked out (fall back silently if not available)
git fetch --depth 1 origin %{commit} || true
git checkout --detach %{commit} || true
git submodule update --init --recursive || true

# Remove VCS metadata to present a clean source tree to rpmbuild
rm -rf PROJECT-%{commit}/.git
popd >/dev/null

# cleanup the now-empty cloned dir
rm -rf PROJECT-%{commit}

# Apply Patches
patch -p1 -i %{PATCH0}

%build
# Restore and publish a framework-dependent build (we depend on dotnet-runtime-8.0)
dotnet publish src/Baballonia.Desktop/Baballonia.Desktop.csproj \
    -r linux-x64 -c LinuxRelease --no-self-contained -f net8.0

%global _publishdir src/Baballonia.Desktop/bin/LinuxRelease/net8.0/linux-x64

%install
# create target directories
install -d %{buildroot}%{_libexecdir}/%{name}
install -d %{buildroot}%{_datadir}/applications
install -d %{buildroot}/lib64

# Copy published files into libexec; publish output is relative to buildroot in our build step
cp -a %{_publishdir}/* %{buildroot}%{_libexecdir}/%{name}/

# Install icons
install -Dm 0644 %{_publishdir}/Assets/Icon_512x512.png %{buildroot}%{_datadir}/icons/hicolor/512x512/apps/baballonia.png
install -Dm 0644 %{_publishdir}/Assets/Icon_32x32.ico %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/baballonia.ico

# Create .desktop file
cat > %{buildroot}%{_datadir}/applications/Baballonia.desktop << 'EOF'
[Desktop Entry]
Type=Application
Name=Baballonia
Comment=A cross-platform, hardware-agnostic VR eye and face tracking application
Exec=/usr/bin/dotnet "%{_libexecdir}/%{name}/Baballonia.Desktop.dll" %%U
Icon=baballonia
Categories=Utility;
EOF
chmod 0644 %{buildroot}%{_datadir}/applications/Baballonia.desktop


%files
%{_datadir}/applications/Baballonia.desktop
%{_datadir}/icons/hicolor/*/apps/baballonia.*
%dir %{_libexecdir}/%{name}
%{_libexecdir}/%{name}/*
%license LICENSE
%doc README.md

%changelog
* Sun Oct 26 2025 Ray Foxyote <ray@foxyote.com>
- Packaged Baballonia desktop dotnet application
