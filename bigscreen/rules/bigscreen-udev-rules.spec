Name:           bigscreen-udev-rules
Version:        0.0.1
Release:        1%{?dist}
Summary:        udev rules for the Bigscreen Beyond Headsets.

License:        NONE
URL:            https://github.com/Banakin/Nobara-BSB-RPM-Sources
Source0:        99-bsb.rules
Source1:        99-bsb-cams.rules

%description
udev rules for the Bigscreen Beyond Headsets.

%prep
%autosetup


%build
%configure
%make_build


%install
install -Dpm0644 %{Source0} %{buildroot}%{_sysconfdir}/udev/rules.d/99-bsb.rules
install -Dpm0644 %{Source1} %{buildroot}%{_sysconfdir}/udev/rules.d/99-bsb.rules

%files
%license add-license-file-here
%doc add-docs-here
%{_sysconfdir}/udev/rules.d/99-bsb.rules
%{_sysconfdir}/udev/rules.d/99-bsb-cams.rules


%changelog
* Wed Oct 29 2025 Ray Foxyote <ray@foxyote.com>
- Added Rules
