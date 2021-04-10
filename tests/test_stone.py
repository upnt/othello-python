from othello.stone import Stone, Color, Candidate


def test_stone():
   stone1 = Stone(Color.BLACK)
   stone2 = Stone(Color.WHITE)
   test_patterns = []
   test_patterns.append((str(stone1), '○'))
   test_patterns.append((str(stone2), '●'))
   stone2.reverse()
   test_patterns.append((stone1.color, stone2.color))
   stone1.reverse()
   test_patterns.append((str(stone1), '●'))
   test_patterns.append((str(stone2), '○'))

   for execute_result, expected_result in test_patterns:
       assert execute_result == expected_result

def test_candidate():
    candidate = Candidate()
    assert str(candidate) == '・'
