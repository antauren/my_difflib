"""Test module"""

import unittest

from step2 import get_diff


class Step2(unittest.TestCase):
    '''test_step2'''

    def test_step_2(self):
        '''test step2'''

        true = ['   host: hexlet.io',
                ' + verbose: True',
                ' - proxy: 123.234.53.22',
                ' - follow: False',
                ' - timeout: 50',
                ' + timeout: 20']

        before = {
            "host": "hexlet.io",
            "timeout": 50,
            "proxy": "123.234.53.22",
            "follow": False
        }

        after = {
            "timeout": 20,
            "verbose": True,
            "host": "hexlet.io"
        }

        test = get_diff(before, after)
        self.assertSetEqual(set(test), set(true))
