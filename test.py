"""Test module"""

import unittest

from make_diff_dict import make_diff_dict
from make_diff_list import make_diff_list


class Test(unittest.TestCase):

    def test_make_diff_dict(self):
        true = {'+ verbose': True,
                '- proxy': '123.234.53.22',
                '- timeout': 50,
                '+ timeout': 20,
                '  host': 'hexlet.io',
                '- follow': False}

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

        test = make_diff_dict(before, after, {})
        self.assertDictEqual(test, true)

    def test_make_diff_list(self):
        true = ["Property 'proxy' was removed",
                "Property 'verbose' was added with value: True",
                "Property 'follow' was removed",
                "Property 'timeout' was updated. From 50 to 20"]

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

        test = make_diff_list(before, after, [], [])

        self.assertSetEqual(set(test), set(true))
