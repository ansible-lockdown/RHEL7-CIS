# Release CIS RedHat Enterprise Linux 7 Benchmark

## CIS v4.0.0 21-12-2023

- updated workflows files
- updated audit and layout
  - audit_only option added
- added new option for centos to update to archived repo for packages if required
  if set to true will update and backup the CentOS-Base file to use new url
  - rhel7cis_add_updated_repo
- rule 5.14 updated to remove jmespath reqirement

## v4.0.0 - 21-12-2023

- Rewrite to address v4.0.0 changes - refer to full changelog in release
- Audit binary version updates
- Audit only option added
- Audit moved earlier in process
- Audit improvements for copy/unarchive etc
- workflow update to self hosted runner

## v3.0.1 - 09-21-2020

## 1.1.4

- update lint
- files relinted
- [#315](https://github.com/ansible-lockdown/RHEL7-CIS/issues/315)
  thanks to @dankxylese
- [#316](https://github.com/ansible-lockdown/RHEL7-CIS/issues/316)
  thanks to I-am-Mos
- readme update
- workflow update

## 1.1.3

- [#313](https://github.com/ansible-lockdown/RHEL7-CIS/issues/313)
  thanks to @xiranlyu and community member Tony(whozzyourdaddy)

## 1.1.2

- update to yamllint
- update linting
- update to galaxy workflow
- rule 2.2.1.1 moved to block
- readme update and badges
- full module names added

## 1.1.1

- Oracle alignment now works and tested with oracle7.9
- audit alignment benchmark version used to test against
- goss audit version updated
- lint file update
- workflow updates

## Major 1.1

- Upgrade to CIS 3.1.1

## Whats new 1.0.0

- New auditing tool all controlled via defaults main. run on host using [goss](https://github.com/aelsabbahy/goss)
- reorder of rules inline with CIS changes
- If Python3 discovered adds the epel repo to install python-rpm and then disables the repo after installing
- Adding of the goss module to the library path
- Python3 now default for control node (should be backward compatible in setup)
- Grub password no longer created using passlib needs to be supplied as variable
  - assert has been created if rule still enabled and password not changed
- Use of the packages facts module

### Highlights

- rhel7cis_allow_reboot is now an option to reboot at the end of remediation - default false
- linting - including command replaced with shell
- section 1
  - 1.1 rewritten to providing better auditing and output
  - 1.3 sudo no longer required move to section 5
  - 1.4.1 bootloader password reworked
  - other groups changes increased tests
  - more controls for GDM
- section 2
  - reorder of server services
  - rsyncd masked
  - 2.5 - 2.4
- section 3
  - some controls now L2
  - tidy of some rules
  - 3.1 disable ipv6 now via grub 9No longer sysctl
- section 4
  - tidy up
- section 5
  - sudo moved from 1.3 to 5.2
  - Other controls changed numbers
  - ssh kex, mac and ciphers updates
- section 6
  - many control orders changed
  - 6.2.11 create missing home dirs rewritten

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
