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

%autosetup

%build

%install
install -Dpm0644 %{SOURCE0} %{buildroot}%{_sysconfdir}/udev/rules.d/99-bsb.rules
install -Dpm0644 %{SOURCE1} %{buildroot}%{_sysconfdir}/udev/rules.d/99-bsb-cams.rules

%files
%{_sysconfdir}/udev/rules.d/99-bsb.rules
%{_sysconfdir}/udev/rules.d/99-bsb-cams.rules


%changelog
* Wed Oct 29 2025 Ray Foxyote <ray@foxyote.com>
- Added Rules
