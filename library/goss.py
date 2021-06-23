#!/usr/bin/env python3
# FROM: https://github.com/indusbox/goss-ansible

import os

from ansible.module_utils.basic import AnsibleModule


DOCUMENTATION = '''
---
module: goss
author: Mathieu Corbin
short_description: Launch goss (https://github.com/aelsabbahy/goss) tests
description:
  - Launch goss tests.
    This module always returns `changed = false` for idempotence.
options:
  path:
    required: true
    description:
      - Test file to validate.
        The test file must be on the remote machine.
  goss_path:
    required: false
    description:
      - Path location for the goss executable.
        Default is "goss" (ie.`no absolute path,  goss executable must be available in $PATH).
  vars_path:
    required: false
    description:
      - Path location for a variables YAML/JSON file to use as templating inputs.
  format:
    required: false
    description:
      - Output goss format.
        Goss format list : goss v --format => [documentation json junit nagios nagios_verbose rspecish tap silent].
        Default is "rspecish".
  format_options:
    required: false
    description:
      - Extra options passed to the formatter, valid options: [perfdata pretty verbose]
        Goss format options: goss -v --format json --format_options pretty
        default: null
  output_file:
    required: false
    description:
      - Save the result of the goss command in a file whose path is output_file
examples:
  - name: run goss against the gossfile /path/to/file.yml
    goss:
      path: "/path/to/file.yml"
  - name: run goss against the gossfile /path/to/file.yml with nagios output
    goss:
      path: "/path/to/file.yml"
      format: "nagios"
  - name: run /usr/local/bin/goss against the gossfile /path/to/file.yml
    goss:
      path: "/path/to/file.yml"
      goss_path: "/usr/local/bin/goss"
  - name: run /usr/local/bin/goss with a variables file
    goss:
      vars_path: "/path/to/file.yml"
  - name: run goss against multiple gossfiles and write the result in JSON format to /my/output/ for each file
    goss:
      path: "{{ item }}"
      format: json
      output_file : /my/output/{{ item }}
    with_items: "{{ goss_files }}"
'''


def check(module, test_file_path, output_format, format_options, goss_path, vars_path):
    """
    Launch goss validate command on the file
    """
    cmd = f'{ goss_path } --gossfile { test_file_path }'
    # goss parent command flags
    if vars_path is not None:
        cmd += f' --vars { vars_path }'

    # validate sub-command flags
    cmd += ' validate'
    if output_format is not None:
        cmd += f' --format { output_format }'
    if format_options is not None:
        cmd += f' --format { output_format } --format-options { format_options }'


    return module.run_command(cmd)


def write_result(output_file_path, out):
    """
    Write goss result to output_file_path
    """
    if output_file_path is not None:
        with open(output_file_path, 'w') as output_file:
            output_file.write(out)


def run_module():
    module = AnsibleModule(
        argument_spec=dict(
            path=dict(required=True, type='str'),
            format=dict(required=False, type='str'),
            output_file=dict(required=False, type='str'),
            format_options=dict(required=False, type='str'),
            vars_path=dict(required=False, type='str'),
            goss_path=dict(required=False, default='goss', type='str'),
        ),
        supports_check_mode=False
    )

    test_file_path = module.params['path']
    output_format = module.params['format']  # goss output format
    format_options = module.params['format_options']  # goss format options
    output_file_path = module.params['output_file']
    goss_path = module.params['goss_path']
    vars_path = module.params['vars_path']

    test_file_path = os.path.expanduser(test_file_path)

    if not os.access(test_file_path, os.R_OK):
        module.fail_json(msg=f'Test file { test_file_path } not readable')

    if os.path.isdir(test_file_path):
        module.fail_json(msg=f'Test file { test_file_path } must be a file but is a path')

    if format_options is not None:
         format_options = (format_options)
         options = ('pretty', 'perfdata', 'verbose')
         if format_options not in options:
             module.fail_json(msg=f' format_options  { format_options }  - must be one of perfdata, pretty or verbose')

    rc, out, err = check(module, test_file_path, output_format, format_options, goss_path, vars_path)


    if output_file_path is not None:
        output_file_path = os.path.expanduser(output_file_path)

        if output_file_path.endswith(os.sep):
            module.fail_json(msg=f'output_file { output_file_path } must be a file')

        output_dirname = os.path.dirname(output_file_path)

        if not os.path.exists(output_dirname):
            module.fail_json(msg=f'directory { output_dirname } does not exists')

        if not os.access(os.path.dirname(output_file_path), os.W_OK):
            module.fail_json(msg=f'Destination { output_dirname } not writable')

        write_result(output_file_path, out)

    if rc is not None and rc != 0:
        error_msg = 'err : { err } ; out : { out }'
        module.fail_json(msg=error_msg)

    module.exit_json(stdout=out, changed=False)


if __name__ == '__main__':
    run_module()