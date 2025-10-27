# Nobara-Project/rpm-sources - Bigscreen Beyond (1/2/2e)
Modified and additional packages from/added to the Nobara RPM sources. Contains tools and fixes for the Bigscreen Beyond 1/2/2e.

This repository contains everything required to get up and running with the Bigscreen Beyond 2e. Im new to patches and packaging but I think I did a good job.

## Usage
Enable the COPR repo:
```shell
sudo dnf copr enable rayfoxyote/nobara-42-bsb
```

### BSB Kernel Patches
Install:
```shell
sudo dnf install --repo="copr:copr.fedorainfracloud.org:rayfoxyote:nobara-42-bsb" kernel-0:6.17.3-200_bsb.nobara.fc42.x86_64 kernel-devel-0:6.17.3-200_bsb.nobara.fc42.x86_64
sudo akmods --force --rebuild
sudo dracut -f --kver --regenerate-all
```

### Installing steam-devices with udev Rules
Install:
```shell
sudo dnf upgrade --repo="copr:copr.fedorainfracloud.org:rayfoxyote:nobara-42-bsb" steam-devices
```

### [Baballonia Face Tracking Software](https://github.com/Project-Babble/Baballonia)
Install:
```shell
sudo dnf install baballonia
```

Open like any other Desktop app.



## Modifications Made
- appstream:
    - Added baballonia.spec to build and install [Baballonia](https://github.com/Project-Babble/Baballonia).
- baseos:
  - kernel (6.17)
    - Rebased and added the BSB Kernel Patches from LVRA ([1](https://lvra.gitlab.io/docs/hardware/bigscreen-beyond-kernel-6.17-1.patch) and [2](https://lvra.gitlab.io/docs/hardware/bigscreen-beyond-kernel-6.17-2.patch))
  - steam-devices
    - Added [BSB Rules](https://lvra.gitlab.io/docs/other/bigscreen-beyond/#bigscreen-beyond-2e-eyetracking-via-baballonia-under-linux)