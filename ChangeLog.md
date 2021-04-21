# release CIS RedHat Enterprise Linux 7 Benchmark v3.0.1 - 09-21-2020

## Whats new 1.0.0

- New auditing tool all controlled via defaults main. run on host using [goss](https://github.com/aelsabbahy/goss)
- reorder of rules inline with CIS changes
- If Python3 discovered adds the epel repo to install python-rpm and then disables the repo after installing
- Adding of the goss module to the library path
- Python3 now default for control node (should be backward compatible in setup)
- Grub password no longer created using passlib needs to be supplied as variable
  - assert has been created if rule still enabled and password not changed
- Use of the packages facts module

## Whats new 1.0.1

- Fixed typos
- Added audit output file permissions

## Whats new in 1.0.2

- renamed goss library and aligned ansible.cfg file
  - thanks to Thulium-Drake

- selinux variable in defaults main - default enforcing
  - 1.7.1.3-5 now idempotent

## Whats new in 1.0.3

- 6.1.12 - rework audit (no score) control
  - thanks to Thulium-Drake #204

- 4.1.1.3 regex improvement
  - thanks to Thulium-Drake #202
  
- 1.5.2 moved grub capture to prelim
