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

## 1.0.4

- Upgrade to CIS 3.1.1

### Highlights

- section 1
  - 1.3 sudo no longer required
  - other groups changes increased tests
  - more controls for GDM
- section 2
  - reorder of server services
  - rsyncd masked
  - 2.5 - 2.4
- section 3
  - some controls now L2
  - tidy of some rules
- section 4
  - tidy up
- section 5
  - sudo moved from 1.3 to 5.2
  - Other controls changed numbers
  - ssh kex, mac and ciphers updates
- section 6
  - many control orders changed

## Whats new in 1.0.3

- Thanks to Thulium-Drake
  - 6.1.12 - rework audit (no score) control #204
  - 4.1.1.3 regex improvement #202

- Thanks to jlosito
  - 1.2.1& 1.2.2- allow centos gpg key check #215
  - 5.1.1 & 5.2.22 -typo fixes #221
  - 5.4.1.4 - idempotence and Inactive whitelist added to defaults main #222
  - 5.5 - Idempotence improvement #213

- 4.2.1.4 - Idempotence improvement #217
  - thanks to andreyzher

- 1.5.2 moved grub capture to prelim

- 5.6 ability to supply an sugroup rather than default to wheel
  - thanks to ihotz #234

## Whats new in 1.0.2

- renamed goss library and aligned ansible.cfg file
  - thanks to Thulium-Drake

- selinux variable in defaults main - default enforcing
  - 1.7.1.3-5 now idempotent

## Whats new 1.0.1

- Fixed typos
- Added audit output file permissions
