from unittest.mock import patch
import unittest

from beginners_selection.abc086c_traveling import traveling


class TestCase(unittest.TestCase):
    def test_traveling1(self):
        user_input = [
            "2",
            "3 1 2",
            "6 1 1",
        ]
        exp_ans = "Yes"

        with patch("builtins.input", side_effect=user_input):
            ans = traveling()
        self.assertEqual(exp_ans, ans)

    def test_traveling2(self):
        user_input = [
            "1",
            "100 1 2",
        ]
        exp_ans = "No"

        with patch("builtins.input", side_effect=user_input):
            ans = traveling()
        self.assertEqual(exp_ans, ans)


if __name__ == "__main__":
    unittest.main()
