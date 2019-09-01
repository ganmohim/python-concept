"""
A simple cross-platform ping utility


Author: GAN MOHIM.
"""
import platform

from subprocess import Popen, PIPE, TimeoutExpired


def ping(address):
    """Pings an ip or url.

    Returns:

    """

    os_type = platform.system()

    cmd = ['ping', address, '-c 1'] if os_type in ['Linux', 'Darwin'] else ['ping', address, '-n', '1']

    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)

    try:
        stdout, stderr = proc.communicate(timeout=5)
        ret_code = proc.returncode

        # Prints stderr in case of failure
        if ret_code != 0:
            print("Error found: {}".format(stderr))
    except TimeoutExpired as e:
        proc.kill()
        raise e

    return ret_code, stdout, stderr
