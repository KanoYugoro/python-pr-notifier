from pyprnotifier import github_retrieval
import unittest
import datetime

class MockModel:
    pass

class BasicTestSuite(unittest.TestCase):
    """Basic test cases."""

    def test_dummyTest(self):
        assert True

    def test_isPRTooOld_yes(self):
        PRObject = MockModel()
        PRObject.updated_at = '2011-01-26T19:01:12Z'
        self.assertTrue(github_retrieval.isPRTooOld(PRObject,datetime.date(2012,1,1)))
    
    def test_isPRTooOld_no(self):
        PRObject = MockModel()
        PRObject.updated_at = '2011-01-26T19:01:12Z'
        self.assertFalse(github_retrieval.isPRTooOld(PRObject,datetime.date(2011,1,25)))
    
    def test_isPRTooOld_invalidInput(self):
        PRObject = MockModel()
        PRObject.updated_at = 'NotADate'
        self.assertRaisesRegex(ValueError, 'Invalid date pulled from Pull Request update_at field: NotADate', github_retrieval.isPRTooOld, PRObject, datetime.date(2011,1,25))


if __name__ == '__main__':
    unittest.main()