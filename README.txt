RHEL 7 CIS STIG
================

Configure RHEL/Centos 7 machine to be CIS compliant. Level 1 and 2 findings will be corrected by default.

This role **will make changes to the system** that could break things. This is not an auditing tool but rather a remediation tool to be used after an audit has been conducted.

## IMPORTANT INSTALL STEP

If you want to install this via the `ansible-galaxy` command you'll need to run it like this:

`ansible-galaxy install -p roles -r requirements.yml

With this in the file requirements.yml:

---
- src: https://github.com/MindPointGroup/RHEL7-CIS.git

Based on [CIS CentOS Linux 7 Benchmark v2.1.0 - 06-02-2016 ](https://community.cisecurity.org/collab/public/index.php).

This repo originated from work done by [Sam Doran](https://github.com/samdoran/ansible-role-stig)

Requirements
------------

You should carefully read through the tasks to make sure these changes will not break your systems before running this playbook.

Role Variables
--------------
There are many role variables defined in defaults/main.yml. This list shows the most important.

#3 Service configuration booleans, set to true to keep the service!
By default the services below will be removed:
rhel7cis_dhcp: false
rhel7cis_ldap: false
rhel7cis_nfs: false
rhel7cis_rpc: false
rhel7cis_bind: false
rhel7cis_vsftpd: false
rhel7cis_httpd: false
rhel7cis_dovecot: false
rhel7cis_samba: false
rhel7cis_squid: false
rhel7cis_net_snmp: false

# These are switches to enable or disable audit point and patches from the relevant chapters in CIS/
rhel7cis_notauto: true
1. Initial setup
rhel7cis_section1: true

2. Services
rhel7cis_section2: true

3. Network Configuration
rhel7cis_section3: true

4. Logging and Auditing
rhel7cis_section4: true

5. Access, Authentication and Authorization
rhel7cis_section5: true

6. System Maintenance
rhel7cis_section6: true

7. User Accounts and Environment
rhel7cis_section7: true

8.  Warning Banners
rhel7cis_section8: true

9. System Maintenance
rhel7cis_section9: true



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

