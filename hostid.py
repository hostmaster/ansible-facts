#!/usr/bin/env python

try:
    import json
except ImportError:
    import simplejson as json
import subprocess


def gethostid():
    return subprocess.check_output("hostid").rstrip()


def main():

    try:
        ansible_facts = {
            'ansible_facts': {
                'hostid': gethostid()
            }
        }
    except subprocess.CalledProcessError, e:
        module.fail_json(msg=e.output)
    except OSError:
        module.fail_json(msg='hostid executable is not found')

    print json.dumps(ansible_facts, sort_keys=False, indent=4)

# import module snippets
from ansible.module_utils.basic import *
main()
