from unittest.mock import patch
import unittest

from beginner_contest.abc211.b_cycle_hit import c_hit


class abc211bTestCase(unittest.TestCase):
    def test_chit(self):
        user_input = [
            "3B",
            "HR",
            "2B",
            "H",
        ]
        exp_ans = "Yes"

        with patch("builtins.input", side_effect=user_input):
            ans = c_hit()
        self.assertEqual(exp_ans, ans)


if __name__ == "__main__":
    unittest.main()
