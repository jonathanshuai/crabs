import unittest
from unittest import mock

import crabs
from crabs import Crab
from crabs.api_caller import CrabCaller


class CrabsTestCase(unittest.TestCase):

    # Dummy test to make sure testing is working
    def test_call_crabs(self):
        test_crab = Crab()
        self.assertTrue(test_crab.call_crabs())


class CrabCallerTestCase(unittest.TestCase):

    @mock.patch('crabs.api_caller.crabcaller.requests.models.Response')
    @mock.patch('crabs.api_caller.crabcaller.requests.get')
    def call_crabs_four_article(self, n, MockRequestGet, MockResponse):
        MockRequestGet.return_value = MockResponse()
        MockResponse().json.return_value = {
            'status': 'ok',
            'articles': [
                {'title': 'Crabs1', 'urlToImage': 'imgurl1'},
                {'title': 'Crabs2', 'urlToImage': 'imgurl2'},
                {'title': 'Crabs3', 'urlToImage': 'imgurl3'},
                {'title': 'Crabs4', 'urlToImage': 'imgurl4'},
            ]}

        test_crab_caller = CrabCaller()
        result = test_crab_caller.call_crabs(n)
        return result

    @mock.patch('crabs.api_caller.crabcaller.requests.models.Response')
    @mock.patch('crabs.api_caller.crabcaller.requests.get')
    def call_crabs_four_article_one_corrupt(self, n, MockRequestGet, MockResponse):
        MockRequestGet.return_value = MockResponse()
        MockResponse().json.return_value = {
            'status': 'ok',
            'articles': [
                {'title': 'Crabs1', 'urlToImage': 'imgurl1'},
                {'title': 'Crabs2', 'urlToImage': 'imgurl2'},
                {'title': 'Crabs3'},
                {'title': 'Crabs4', 'urlToImage': 'imgurl4'},
            ]}

        test_crab_caller = CrabCaller()
        result = test_crab_caller.call_crabs(n)
        return result


    @mock.patch('crabs.api_caller.crabcaller.requests.models.Response')
    @mock.patch('crabs.api_caller.crabcaller.requests.get')
    def call_crabs_bad_status(self, n, MockRequestGet, MockResponse):
        MockRequestGet.return_value = MockResponse()
        MockResponse().json.return_value = {
            'status': 'bad',
            'articles': []}

        test_crab_caller = CrabCaller()
        result = test_crab_caller.call_crabs(n)
        return result

    def test_call_crab_four_one(self):
        result = self.call_crabs_four_article(1)
        self.assertEqual(len(result), 1)

    def test_call_crab_four_none(self):
        result = self.call_crabs_four_article(0)
        self.assertEqual(len(result), 0)

    def test_call_crab_four_five(self):
        result = self.call_crabs_four_article(5)
        self.assertEqual(len(result), 4)

    def test_call_crab_corrupt_3(self):
        result = self.call_crabs_four_article_one_corrupt(3)
        self.assertEqual(len(result), 3)

    def test_call_crab_corrupt_4(self):
        result = self.call_crabs_four_article_one_corrupt(4)
        self.assertEqual(len(result), 3)

    def test_call_crab_bad_status(self):
        result = self.call_crabs_bad_status(1)
        self.assertEqual(len(result), 0)