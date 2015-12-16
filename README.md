RHEL 6 DISA STIG
================

Configure RHEL 6 machine to be DISA STIG compliant. CAT I findings will be corrected by default. CAT II and CAT III findings can be corrected by setting the appropriate variable to enable those playbooks.

This role **will make changes to the system** that could break things. This is not an auditing tool but rather a remediation tool to be used after an audit has been conducted.

The role tries to be helpful and pause to let you know it found something. You can disable this behaviour if you want to run it unattended by setting `rhel6stig_fullauto` to `true`.

## IMPORTANT INSTALL STEP

If you want to install this via the `ansible-galaxy` command you'll need to run it like this: 

`ansible-galaxy install -p roles nousdefions.STIG-RHEL6,devel`

Based on [Red Hat Enterprise Linux 6 STIG Version 1 Release 6 - 2015-01-23](http://iase.disa.mil/stigs/os/unix-linux/Pages/index.aspx).

Inspiration and some config files taken from [RedHatGov](https://github.com/RedHatGov) [stig-fix-el6](https://github.com/RedHatGov/stig-fix-el6).

This repo originated from work done by [Sam Doran](https://github.com/samdoran/ansible-role-stig)

Requirements
------------

You should carefully read through the tasks to make sure these changes will not break your systems before running this playbook.

Role Variables
--------------
There are many role variables defined in defaults/main.yml. This list shows the most important.

**rhel6stig_cat1**:           Correct CAT I findings (Default: true)

**rhel6stig_cat2**:           Correct CAT II findings (Default: false)

**rhel6stig_cat3**:           Correct CAT III findings (Default: false)

**rhel6stig_fullauto**:       Run the role without pausing (Default: true)

**rhel6stig_use_dhcp**:       Whether the system should use DHCP or Static IPs. **Setting this false is dangerous.** (Default: true)

**rhel6stig_system_is_router** Whether on not the target system is acting as a router. Disables settings that would break the system if it is a acting as a router. (Default: false)

**rhel6stig_root_email_address**:          Address where system email is sent (Default: foo@baz.com)

**rhel6stig_xwindows_required**:           Whether or not X Windows is is use on taregt systems. Disables some changes if X Windows is not in use. (Default: false)

**rhel6stig_ipv6_in_use**       Whether or not ipv6 is in use of the target system. This is set automatically to 'true' if ipv6 is found to be in use. (Default: false)

**rhel6stig_tftp_required**  Whether or not TFTP is required. This will prevent the removal of `tftp` and `tftp-server` packages. It will also  reconfigure the `tftp-server` to run securely. (Default: false)
Dependencies

**rhel6stig_change_grub_password**: Whether or not to update the grub password even if a hash already exists in `/boot/grub/grub.conf`. (Default: false)

**rhel6stig_bootloader_password**: The new grub password to use if rhel6stig_change_grub_password is **TRUE** (Default: randomly generated and encrypted string)


Dependencies
------------

Ansible > 1.8

Example Playbook
-------------------------

Make sure to include the vars_prompt section in your playbook. It is needed for the tasks that set the grub password.

    - hosts: servers
      sudo: yes

      roles:
         - { role: RHEL6-STIG, rhel6stig_cat1: true, rhel6stig_cat2: true, rhel6stig_cat3: false }


Tags
----
Many tags are available for precise control of what is and is not changed. When running this playbook with tags, always include the `prelim_tasks` tag. This will run all the setup tasks that gather information and set variables used by subsequest tasks. If run without `prelim_tasks`, certain tasks may fail.

Some examples of using tags:

    # Only remediate ssh
    ansible-playbook site.yml --tags="prelim_tasks,ssh"

    # Don't change SNMP or postfix
    ansible-playbook site.yml --skip-tags="postfix,mail,snmp"


License
-------

MIT

