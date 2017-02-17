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

Based on [CIS RedHat Enterprise Linux 7 Benchmark v2.1.1 - 01-31-2017 ](https://community.cisecurity.org/collab/public/index.php).

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

##### Disable all selinux functions
`rhel7cis_selinux_disable: false`

##### Service variables:
###### These control whether a server should or should not be allowed to continue to run these services

```
rhel7cis_avahi_server: false  
rhel7cis_cups_server: false  
rhel7cis_dhcp_server: false  
rhel7cis_ldap_server: false  
rhel7cis_telnet_server: false  
rhel7cis_nfs_server: false  
rhel7cis_rpc_server: false  
rhel7cis_ntalk_server: false  
rhel7cis_rsyncd_server: false  
rhel7cis_tftp_server: false  
rhel7cis_rsh_server: false  
rhel7cis_nis_server: false  
rhel7cis_snmp_server: false  
rhel7cis_squid_server: false  
rhel7cis_smb_server: false  
rhel7cis_dovecot_server: false  
rhel7cis_httpd_server: false  
rhel7cis_vsftpd_server: false  
rhel7cis_named_server: false  
rhel7cis_bind: false  
rhel7cis_vsftpd: false  
rhel7cis_httpd: false  
rhel7cis_dovecot: false  
rhel7cis_samba: false  
rhel7cis_squid: false  
rhel7cis_net_snmp: false  
```  

##### Designate server as a Mail server
`rhel7cis_is_mail_server: false`


##### System network parameters (host only OR host and router)
`rhel7cis_is_router: false`  


##### IPv6 required
`rhel7cis_ipv6_required: true`  


##### AIDE
`rhel7cis_config_aide: true`

###### AIDE cron settings
```
rhel7cis_aide_cron:
  cron_user: root
  cron_file: /etc/crontab
  aide_job: '/usr/sbin/aide --check'
  aide_minute: 0
  aide_hour: 5
  aide_day: '*'
  aide_month: '*'
  aide_weekday: '*'  
```

##### SELinux policy
`rhel7cis_selinux_pol: targeted` 


##### Set to 'true' if X Windows is needed in your environment
`rhel7cis_xwindows_required: no` 


##### Client application requirements
```
rhel7cis_openldap_clients_required: false 
rhel7cis_telnet_required: false 
rhel7cis_talk_required: false  
rhel7cis_rsh_required: false 
rhel7cis_ypbind_required: false 
```

##### Time Synchronization
```
rhel7cis_time_synchronization: chrony
rhel7cis_time_Synchronization: ntp

rhel7cis_time_synchronization_servers:
    - 0.pool.ntp.org
    - 1.pool.ntp.org
    - 2.pool.ntp.org
    - 3.pool.ntp.org  
```  
  
##### 3.4.2 | PATCH | Ensure /etc/hosts.allow is configured
```
rhel7cis_host_allow:
  - "10.0.0.0/255.0.0.0"  
  - "172.16.0.0/255.240.0.0"  
  - "192.168.0.0/255.255.0.0"    
```  

```
rhel7cis_firewall: firewalld
rhel7cis_firewall: iptables
``` 
  

Dependencies
------------

Ansible > 1.9

Example Playbook
-------------------------

```
- name: Harden Server
  hosts: servers
  become: yes

  roles:
    - RHEL7-CIS
```

Tags
----
Many tags are available for precise control of what is and is not changed.

Some examples of using tags:

```
    # Audit and patch the site
    ansible-playbook site.yml --tags="patch"
```

License
-------

MIT
