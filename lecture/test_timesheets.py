import unittest
from unittest import TestCase
from unittest.mock import patch, call

import timesheets


class TestTimeSheet(TestCase):

    """ mock input() and force to return a value """

    @patch('builtins.input', side_effect=['2'])
    def test_get_hours_for_day(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)

    @patch('builtins.input', side_effect=['cat', '', 'fish', '123bird', 'pizza1234', '2'])
    def test_get_hours_for_day_non_numeric_rejected(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(2, hours)

    @patch('builtins.input', side_effect=['-1', '-1000', '6'])
    def test_get_hours_for_day_greater_than_zero(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(6, hours)

    @patch('builtins.input', side_effect=['24.0000001', '1000', '25', '9'])
    def test_get_hours_for_day_less_than_24(self, mock_input):
        hours = timesheets.get_hours_for_day('Monday')
        self.assertEqual(9, hours)


if __name__ == '__main__':
    unittest.main()
