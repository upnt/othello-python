from othello.stone import Stone, Color


def test_with_valid_params(self):
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
       assert execute_result == expected_result
