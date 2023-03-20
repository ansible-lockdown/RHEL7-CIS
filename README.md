# RHEL 7 CIS

![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL7-CIS/CommunityToDevel?label=Devel%20Build%20Status&style=plastic)
![Build Status](https://img.shields.io/github/workflow/status/ansible-lockdown/RHEL7-CIS/DevelToMain?label=Main%20Build%20Status&style=plastic)
![Release](https://img.shields.io/github/v/release/ansible-lockdown/RHEL7-CIS?style=plastic)

Configure RHEL/Centos 7 machine to be [CIS](https://www.cisecurity.org/cis-benchmarks/) compliant
Untested on OEL

Based on [CIS RedHat Enterprise Linux 7 Benchmark v3.1.1 - 05-21-2021 ](https://www.cisecurity.org/cis-benchmarks/)

## Join us

On our [Discord Server](https://discord.gg/JFxpSgPFEJ) to ask questions, discuss features, or just chat with other Ansible-Lockdown users

## Caution(s)

This role **will make changes to the system** which may have unintended consequences. This is not an auditing tool but rather a remediation tool to be used after an audit has been conducted.

Check Mode is not supported! The role will complete in check mode without errors, but it is not supported and should be used with caution. The RHEL7-CIS-Audit role or a compliance scanner should be used for compliance checking over check mode.

This role was developed against a clean install of the Operating System. If you are implementing to an existing system please review this role for any site specific changes that are needed.

To use release version please point to main branch and relevant release for the cis benchmark you wish to work with.

## Matching security Level for CIS

It is possible to to only run level 1 or level 2 controls for CIS.
This is managed using tags:

- level1_server
- level1_workstation
- level2_server
- level2_workstation

The control found in defaults main also need to reflect this as this control the testing thet takes place if you are using the audit component.

## Coming from a previous release

CIS release always contains changes, it is highly recommended to review the new references and available variables. This have changed significantly since ansible-lockdown initial release.
This is now compatible with python3 if it is found to be the default interpreter. This does come with pre-requisites which it configures the system accordingly.

Further details can be seen in the [Changelog](./ChangeLog.md)

## Auditing (new)

This can be turned on or off within the defaults/main.yml file with the variable rhel7cis_run_audit. The value is false by default, please refer to the wiki for more details. The defaults file also populates the goss checks to check only the controls that have been enabled in the ansible role.

This is a much quicker, very lightweight, checking (where possible) config compliance and live/running settings.

A new form of auditing has been developed, by using a small (12MB) go binary called [goss](https://github.com/aelsabbahy/goss) along with the relevant configurations to check. Without the need for infrastructure or other tooling.
This audit will not only check the config has the correct setting but aims to capture if it is running with that configuration also trying to remove [false positives](https://www.mindpointgroup.com/blog/is-compliance-scanning-still-relevant/) in the process.

Refer to [RHEL7-CIS-Audit](https://github.com/ansible-lockdown/RHEL7-CIS-Audit).

## Documentation

- [Getting Started](https://www.lockdownenterprise.com/docs/getting-started-with-lockdown)
- [Customizing Roles](https://www.lockdownenterprise.com/docs/customizing-lockdown-enterprise)
- [Per-Host Configuration](https://www.lockdownenterprise.com/docs/per-host-lockdown-enterprise-configuration)
- [Getting the Most Out of the Role](https://www.lockdownenterprise.com/docs/get-the-most-out-of-lockdown-enterprise)
- [Wiki](https://github.com/ansible-lockdown/RHEL7-CIS/wiki)
- [Repo GitHub Page](https://ansible-lockdown.github.io/RHEL7-CIS/)

## Requirements

**General:**

- Basic knowledge of Ansible, below are some links to the Ansible documentation to help get started if you are unfamiliar with Ansible

  - [Main Ansible documentation page](https://docs.ansible.com)
  - [Ansible Getting Started](https://docs.ansible.com/ansible/latest/user_guide/intro_getting_started.html)
  - [Tower User Guide](https://docs.ansible.com/ansible-tower/latest/html/userguide/index.html)
  - [Ansible Community Info](https://docs.ansible.com/ansible/latest/community/index.html)
- Functioning Ansible and/or Tower Installed, configured, and running. This includes all of the base Ansible/Tower configurations, needed packages installed, and infrastructure setup.
- Please read through the tasks in this role to gain an understanding of what each control is doing. Some of the tasks are disruptive and can have unintended consiquences in a live production system. Also familiarize yourself with the variables in the defaults/main.yml file or the [Main Variables Wiki Page](https://github.com/ansible-lockdown/RHEL7-CIS/wiki/Main-Variables).

**Technical Dependencies:**

- Running Ansible/Tower setup (this role is tested against Ansible version 2.9.1 and newer)
- Python3 Ansible run environment
- python-def (should be included in RHEL/CentOS 7) - First task sets up the prerequisites (Tag pre-reqs)for python3 and python2 (where required)
  - libselinux-python
  - python3-rpm (package used by py3 to use the rpm pkg)

## Role Variables

This role is designed that the end user should not have to edit the tasks themselves. All customizing should be done via the defaults/main.yml file or with extra vars within the project, job, workflow, etc. These variables can be found [here](https://github.com/ansible-lockdown/RHEL7-CIS/wiki/Main-Variables) in the Main Variables Wiki page. All variables are listed there along with descriptions.

## Tags

There are many tags available for added control precision. Each control has it's own set of tags noting what level, if it's scored/notscored, what OS element it relates to, if it's a patch or audit, and the rule number.

Below is an example of the tag section from a control within this role. Using this example if you set your run to skip all controls with the tag services, this task will be skipped. The opposite can also happen where you run only controls tagged with services.

```sh
      tags:
      - level1-workstation
      - level1-server
      - automated
      - avahi
      - services
      - patch
      - rule_2.2.4
```

## Example Audit Summary

The audit when run from ansible also uses all the specific variables, so will test relevant variables based on host configuration settings.
This is based on a vagrant image, based upon a pre-configured image for filesystem layout etc. e.g. No Gui or firewall.
Note: More tests are run during audit as we are checking config and running state.

```sh
TASK [RHEL7-CIS : Show Audit Summary] ******************************************************************************************************************************************************************************
******
ok: [cent7_efi] => {
    "msg": [
        "The pre remediation results are: Count: 380, Failed: 121, Duration: 10.399s.",
        "The post remediation results are: Count: 380, Failed: 10, Duration: 12.324s.",
        "Full breakdown can be found in /var/tmp",
        ""
    ]
}

PLAY RECAP ******************************************************************************************************************************************************************************************************************
******
cent7_efi                  : ok=274  changed=143  unreachable=0    failed=0    skipped=140  rescued=0    ignored=0  

```

## Branches

- **devel** - This is the default branch and the working development branch. Community pull requests will pull into this branch
- **main** - This is the release branch
- **reports** - This is a protected branch for our scoring reports, no code should ever go here
- **gh-pages** - This is the github pages branch
- **all other branches** - Individual community member branches

## Community Contribution

We encourage you (the community) to contribute to this role. Please read the rules below.

- Your work is done in your own individual branch. Make sure to Signed-off and GPG sign all commits you intend to merge.
- All community Pull Requests are pulled into the devel branch
- Pull Requests into devel will confirm your commits have a GPG signature, Signed-off, and a functional test before being approved
- Once your changes are merged and a more detailed review is complete, an authorized member will merge your changes into the main branch for a new release

## Pipeline Testing

uses:

- ansible-core 2.12
- ansible collections - pulls in the latest version based on requirements file
- runs the audit using the devel branch
- This is an automated test that occurs on pull requests into devel

## Support

This is a community project at its core and will be managed as such.

If you would are interested in dedicated support to assist or provide bespoke setups

- [Ansible Counselor](https://www.mindpointgroup.com/products/ansible-counselor-on-demand-ansible-services-and-consulting/)
- [Try us out](https://engage.mindpointgroup.com/try-ansible-counselor)

## Credits

This repo originated from work done by [Sam Doran](https://github.com/samdoran/ansible-role-stig)
