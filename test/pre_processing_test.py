"""
pytest

"""
import unittest
from pre_processing.pre_processing import PreProcessor



class Test(unittest.TestCase):
    """
    pytest preprocessing
    """
    def setUp(self):
        self.pre_processor = PreProcessor(padding_size=20)

    def test_divide(self):
        """
        test
        """
        result = self.pre_processor.pre_process_text('I <user> am hewei Yang! :),, !!!')
        expected_result = [12, 2, 227, 1, 186, 11, 1, 6, 6, 11, 11, 11, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(result, expected_result)
