import unittest
from mock import Mock
from dvSwitchDataRetriever import dvSwitchDataRetriever

class test_dvSwitchDataRetriever(unittest.TestCase):

    def test_RetrieveDvSwitchData(self):
        switchRetriever = dvSwitchDataRetriever('host', 'user', 'password')
        switchRetriever.RetrieveDvSwitchData('switchName')
        self.assertEqual(True, True)

if __name__ == '__main__':
    unittest.main()
