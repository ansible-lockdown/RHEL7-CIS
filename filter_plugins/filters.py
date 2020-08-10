try:
    import passlib.hash
    HAS_PASSLIB = True
    PASSLIB_VERSION = float(passlib.__version__[:3])
except ImportError as e:
    HAS_PASSLIB = False

from ansible import errors


def grub2_hash(password, salt=None, iterations=25000):
    # Build list of keyword arguments to pass into hash/encrypt method
    kwargs = dict()

    if salt:
        # passlib generates a random salt of 64 byte length by default (recommended)
        kwargs['salt'] = salt.encode()

    if iterations:
        # passlib does 25000 rounds (in version 1.7) by default (recommended or set to a higher value)
        kwargs['rounds'] = iterations

    # Make sure we have passlib and the correct version
    if not HAS_PASSLIB:
        raise errors.AnsibleFilterError('grub2_hash requires the passlib python module to generate password hashes')

    if PASSLIB_VERSION < 1.5:
        raise errors.AnsibleFilterError('passlib >= 1.5 is required and %s is installed' % PASSLIB_VERSION)

    elif PASSLIB_VERSION < 1.7:
        encrypted = passlib.hash.grub_pbkdf2_sha512.encrypt(password, **kwargs)

    else:
        encrypted = passlib.hash.grub_pbkdf2_sha512.using(**kwargs).hash(password)

    return encrypted


class FilterModule(object):

    def filters(self):
        return {
            'grub2_hash': grub2_hash
        }
