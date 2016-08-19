RHEL 7 CIS STIG
================

[![Build Status](https://travis-ci.org/daswars/RHEL7-CIS.svg?branch=devel)](https://travis-ci.org/daswars/RHEL7-CIS)


Configure RHEL/Centos 7 machine to be CIS compliant. Level 1 and 2 findings will be corrected by default.

This role **will make changes to the system** that could break things. This is not an auditing tool but rather a remediation tool to be used after an audit has been conducted.

## IMPORTANT INSTALL STEP

If you want to install this via the `ansible-galaxy` command you'll need to run it like this:

`ansible-galaxy install -p roles -r requirements.yml`

With this in the file requirements.yml:

```
- src: https://github.com/MindPointGroup/RHEL7-CIS.git
```

Based on [CIS CentOS Linux 7 Benchmark v2.1.0 - 06-02-2016 ](https://community.cisecurity.org/collab/public/index.php).

This repo originated from work done by [Sam Doran](https://github.com/samdoran/ansible-role-stig)

Requirements
------------

You should carefully read through the tasks to make sure these changes will not break your systems before running this playbook.

Role Variables
--------------
There are many role variables defined in defaults/main.yml. This list shows the most important.

**rhel7cis_notauto**: Run CIS checks that we typically do NOT want to automate due to the high probability of breaking the system (Default: false)

**rhel7cis_section1**: CIS - General Settings (Section 1) (Default: true)

**rhel7cis_section2**: CIS - Services settings (Section 2) (Default: true)

**rhel7cis_section3**: CIS - Network settings (Section 3) (Default: true)

**rhel7cis_section4**: CIS - Logging and Auditing settings (Section 4) (Default: true)

**rhel7cis_section5**: CIS - Access, Authentication and Authorization settings (Section 5) (Default: true)

**rhel7cis_section6**: CIS - System Maintenance settings (Section 6) (Default: true)

Service variables: These control whether a server should or should not be allowed to continue to run these services.

False (Default) = Disallow service (it will be removed upon playbook run)
True = Allow service (service will not be removed)

    **rhel7cis_dhcp**: Allow dhcp (Default: false)
    **rhel7cis_ldap**: Allow ldap (Default: false)
    **rhel7cis_nfs**: Allow nfs (Default: false)
    **rhel7cis_rpc**: Allow rpc (Default: false)
    **rhel7cis_bind**: Allow bind (Default: false)
    **rhel7cis_vsftpd**: Allow vsftpd (Default: false)
    **rhel7cis_httpd**: Allow httpd (Apache) (Default: false)
    **rhel7cis_dovecot**: Allow dovecot (Default: false)
    **rhel7cis_samba**: Allow samba (Default: false)
    **rhel7cis_squid**: Allow squid (Default: false)
    **rhel7cis_net_snmp**: Allow SNMP (Default: false)


Dependencies
------------

Ansible > 1.9

Example Playbook
-------------------------

- name: Harden Server
  hosts: servers
  become: yes

  roles:
    - RHEL7-CIS


Tags
----
Many tags are available for precise control of what is and is not changed.

Some examples of using tags:

    # Only audit the site
    ansible-playbook site.yml --tags="audit"

    # Audit and patch the site
    ansible-playbook site.yml --tags="patch"


License
-------

MIT
