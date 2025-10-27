Nobara-Project/rpm-sources - Bigscreen Beyond (1/2/2e)
---
This repository contains everything required to get up and running with the Bigscreen Beyond 2e. Im new to patches and packaging but I think I did a good job.

Installing Kernel Patches
---

Installing Steam with udev Rules
---

Installing EyeTracking Software
---


Modifications
---
- appstream:
  - steam
    - Added [BSB Rules](https://lvra.gitlab.io/docs/other/bigscreen-beyond/#bigscreen-beyond-2e-eyetracking-via-baballonia-under-linux)
  - Baballonia
    - Added baballonia.spec to build and install [Baballonia](https://github.com/Project-Babble/Baballonia).
- baseos:
  - kernel (6.17)
    - Rebased and added the BSB Kernel Patches from LVRA ([1](https://lvra.gitlab.io/docs/hardware/bigscreen-beyond-kernel-6.17-1.patch) and [2](https://lvra.gitlab.io/docs/hardware/bigscreen-beyond-kernel-6.17-2.patch))
  - steam-devices
    - Added [BSB Rules](https://lvra.gitlab.io/docs/other/bigscreen-beyond/#bigscreen-beyond-2e-eyetracking-via-baballonia-under-linux)