#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import random, string
from hashlib import pbkdf2_hmac
from binascii import hexlify
from os import urandom
from ansible.module_utils.basic import AnsibleModule


def gen_pass(size=16, chars=string.ascii_letters + string.digits):
    '''Generate a random password.'''
    return ''.join(random.choice(chars) for x in range(size))


def gen_salt(salt):
    '''Generate a random salt.'''
    if not salt:
        return urandom(length)
    else:
        return salt


def main():
    '''Return a pbkdf2 password for use with GRUB2'''
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
    
    algo = 'sha512'
    iterCount = 10000
    
    salt = module.params['salt']
    password = module.params['password']
    if password == 'random':
        password = gen_pass()
    sha512_salt = gen_salt(salt)
    salted_pass = pbkdf2_hmac(algo, password, sha512_salt, iterCount)
    pbkdf2_pass = 'grub.pbkdf2.{}.{}.{}.{}'.format(algo, iterCount, hexlify(sha512_salt).upper(), hexlify(salted_pass).upper())
    module.exit_json(changed=False, passhash=pbkdf2_pass)


if __name__ == '__main__':
    main()
