# release CIS RedHat Enterprise Linux 7 Benchmark v3.0.1 - 09-21-2020

## Whats new

- New auditing tool all controlled via defaults main. run on host using [goss](https://github.com/aelsabbahy/goss)
- reorder of rules inline with CIS changes
- If Python3 discovered adds the epel repo to install python-rpm and then disables the repo after installing
- Adding of the goss module to the library path

## High level changes within tasks

- Python3 now default for control node (should be backward compatible in setup)
- Grub password no longer created using passlib needs to be supplied as variable

  - assert has been created if rule still enabled and password not changed

- use of the packages facts module
