#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import crypt
import random
import string
from ansible.module_utils.basic import AnsibleModule


def gen_pass(size=16, chars=string.ascii_letters + string.digits):
    '''Generate a random password.'''
    return ''.join(random.choice(chars) for x in range(size))


def gen_salt(salt):
    '''Generate a random salt.'''
    ret = ''
    if not salt:
        with open('/dev/urandom', 'rb') as urandom:
            while True:
                byte = urandom.read(1)
                if byte in string.ascii_letters + string.digits + './':
                    ret += byte
                    if len(ret) == 16:
                        break
        return '$6$%s' % ret
    return '$6$%s' % salt


def main():
    '''Return a crypt-ed password for use with GRUB2'''
    module = AnsibleModule(
        argument_spec=dict(
            salt=dict(required=False, default=None),
            password=dict(
                no_log=True,
                required=False,
                default='random',
                type='str'
            ),
        )

    )
    salt = module.params['salt']
    password = module.params['password']
    if password == 'random':
        password = gen_pass()
    sha512_salt = gen_salt(salt)
    salted_pass = crypt.crypt(password, sha512_salt)
    module.exit_json(changed=False, passhash=salted_pass)


if __name__ == '__main__':
    main()
