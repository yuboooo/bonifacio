import input_check as t

def test_substitutability():
    # TEST 1
    prefs = {
                        1: [[1,2],[1,5],[2,5]],
                        2: [[3,6],[3,5],[5,6]],
                        3: [[2,4],[1,2],[3,4]]
              }
    assert t.substitutability(prefs) == True
    # TEST 2
    prefs = {
                    1: [[1,2],[2,5],[2,5]],
                    2: [[3,6],[3,5],[5,6]],
                    3: [[2,4],[1,4],[3,4]]
            }
    assert t.substitutability(prefs) == True
    # TEST 3
    prefs = {
                        1: [[1,2],[1,5],[2,5]],
                        2: [[3,6],[3,5],[5,6]],
                        3: [[2,4],[1,2],[3,7]]
              }
    assert t.substitutability(prefs) == True
    # TEST 4
    firms_prefs = {
                            1: [[1,2],[1,5],[2,5],[1,3],[4,5],[2,4],[1,4],[3,4],[3,5],[2,3],[1],[4],[3],[2],[5]],
                            2: [[3,6],[3,5],[5,6],[2,5],[1,3],[2,6],[1,5],[1,2],[2,3],[1,6],[1],[2],[3],[5],[6]],
                            3: [[2,4],[1,2],[3,4],[2,3],[1,3],[1,4],[1],[2],[3],[4]]
                }
    assert t.substitutability(prefs) == True
    # TEST 5
    workers_prefs = {
                        1: [[3],[1],[2]],
                        2: [[2,3],[1,3],[1,2],[1],[2],[3]],
                        3: [[1],[2]],
                        4: [[1],[3],[2]],
                        5: [[2],[3]],
                        6: [[1,3],[3],[1]]
                }
    assert t.substitutability(prefs) == True

    # TEST 6
    prefs = {
                    1: [[1,2],[3,5],[2,5]],
                    2: [[3,6],[3,5],[5,6]],
                    3: [[2,4],[1,2],[3,4]]
            }
    assert t.substitutability(prefs) == False
    # TEST 7
    prefs = {
                    1: [[1,2],[1,5],[2,5]],
                    2: [[3,6],[4,5],[5,6]],
                    3: [[2,4],[1,2],[3,4]]
            }
    assert t.substitutability(prefs) == False
    # TEST 8
    prefs = {
                        1: [[1,2],[1,5],[2,5]],
                        2: [[3,6],[3,5],[5,6]],
                        3: [[2,4],[1,3],[3,4]]
              }
    assert t.substitutability(prefs) == False
    # TEST 9
    prefs = {
                    1: [[1,2],[3],[2,5]],
                    2: [[3,6],[3,5],[5,6]],
                    3: [[2,4],[1,3],[3,4]]
            }
    assert t.substitutability(prefs) == False
    # TEST 10
    workers_prefs = {
                        1: [[3],[1],[2]],
                        2: [[2,3],[1,3],[1,2],[1],[2],[3]],
                        3: [[1],[2]],
                        4: [[1],[3],[2]],
                        5: [[2],[3]],
                        6: [[1,3],[4],[1]]
                }
    assert t.substitutability(prefs) == False