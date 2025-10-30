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
sudo dnf install --repo="copr:copr.fedorainfracloud.org:rayfoxyote:nobara-42-bsb" kernel-0:6.17.5-200_bsb.nobara.fc42.x86_64 kernel-devel-0:6.17.5-200_bsb.nobara.fc42.x86_64
sudo akmods --force --rebuild
sudo dracut -f --regenerate-all
```
Then reboot.

### Installing udev Rules
Install:
```shell
sudo dnf install bigscreen-udev-rules
```
Then reboot.

### [Baballonia Face Tracking Software](https://github.com/Project-Babble/Baballonia)
#### Regular Install
Install:
```shell
sudo dnf install baballonia
```

#### Patched With CUDA Support
Enable Nvidia cuDNN repo:
```shell
sudo dnf config-manager addrepo --from-repofile='https://developer.download.nvidia.com/compute/cuda/repos/rhel10/x86_64/cuda-rhel10.repo'
sudo dnf clean all
```

Install:
```shell
sudo dnf install baballonia-nvidia
```

Open like any other Desktop app.



## Modifications Made
- baseos:
  - kernel (6.17)
    - Rebased and added the BSB Kernel Patches from LVRA ([1](https://lvra.gitlab.io/docs/hardware/bigscreen-beyond-kernel-6.17-1.patch) and [2](https://lvra.gitlab.io/docs/hardware/bigscreen-beyond-kernel-6.17-2.patch))
- bigscreen:
    - Baballonia
      - Added baballonia.spec to build and install [Baballonia](https://github.com/Project-Babble/Baballonia).
      - Added baballonia-nvidia.spec to build and install [Baballonia](https://github.com/Project-Babble/Baballonia) with CUDA support.
    - Rules
      - Added bigscreen-udev-rules.spec to install the required udev rules for the BSB2e.
