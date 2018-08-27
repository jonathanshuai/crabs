import unittest
from unittest import mock

import crabs
from crabs import Crab


class CrabsTestCase(unittest.TestCase):

    # Dummy test to make sure testing is working
    def test_call_crabs(self):
        test_crab = Crab()
        self.assertTrue(test_crab.call_crabs())
