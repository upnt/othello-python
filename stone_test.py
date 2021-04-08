from unittest import TestCase, main
from stone import Stone, Color


class TestRockPaperScissors(TestCase):
    """ This test case tests rock_paper_scissors method """

    def test_with_valid_params(self):
        """
        With SubTest, All patterns will be tested even if there are some failures.
        Consequently, we can test all patterns every time.
        """

        stone1 = Stone(Color.BLACK)
        stone2 = Stone(Color.WHITE)
        test_patterns = []
        test_patterns.append((str(stone1), '○'))
        test_patterns.append((str(stone2), '●'))
        stone1.reverse()
        stone2.reverse()
        test_patterns.append((str(stone1), '●'))
        test_patterns.append((str(stone2), '○'))

        for execute_result, expected_result in test_patterns:
            self.assertEqual(execute_result, expected_result)
