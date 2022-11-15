import bonifacio as b

def test_da():
    # E.g.1 - Paper's Eg
    firms_pref = {
                            1: [[1,2],[1,5],[2,5],[1,3],[4,5],[2,4],[1,4],[3,4],[3,5],[2,3],[1],[4],[3],[2],[5]],
                            2: [[3,6],[3,5],[5,6],[2,5],[1,3],[2,6],[1,5],[1,2],[2,3],[1,6],[1],[2],[3],[5],[6]],
                            3: [[2,4],[1,2],[3,4],[2,3],[1,3],[1,4],[1],[2],[3],[4]]
                }
    workers_pref = {
                            1: [[3],[1],[2]],
                            2: [[2,3],[1,3],[1,2],[1],[2],[3]],
                            3: [[1],[2]],
                            4: [[1],[3],[2]],
                            5: [[2],[3]],
                            6: [[1,3],[3],[1]]
                }
    # 1. firms proposing:
    assert b.da(firms_pref, workers_pref) == [{1: [1, 2], 2: [3, 5], 3: [2, 4]}, {1: [1], 2: [1, 3], 3: [2], 4: [3], 5: [2]}]
    # 2. workers proposing:
    assert b.da(workers_pref, firms_pref) == [{1: [3], 2: [2, 3], 3: [1], 4: [1], 5: [2], 6: 'None'}, {1: [3, 4], 2: [2, 5], 3: [1, 2]}]

    # E.g.2 - delete f1 from w1's preference list
    firms_pref = {
                        1: [[1,2],[1,5],[2,5],[1,3],[4,5],[2,4],[1,4],[3,4],[3,5],[2,3],[1],[4],[3],[2],[5]],
                        2: [[3,6],[3,5],[5,6],[2,5],[1,3],[2,6],[1,5],[1,2],[2,3],[1,6],[1],[2],[3],[5],[6]],
                        3: [[2,4],[1,2],[3,4],[2,3],[1,3],[1,4],[1],[2],[3],[4]]
              }

    workers_pref = {
                            1: [[3],[2]],
                            2: [[2,3],[1,3],[1,2],[1],[2],[3]],
                            3: [[1],[2]],
                            4: [[1],[3],[2]],
                            5: [[2],[3]],
                            6: [[1,3],[3],[1]]
                    }
    # 1. firms proposing:
    assert b.da(firms_pref, workers_pref) == [{1: [2, 4], 2: [3, 5], 3: [1, 2]}, {1: [3], 2: [1, 3], 3: [2], 4: [1], 5: [2]}]
    # 2. workers proposing:
    assert b.da(workers_pref, firms_pref) == [{1: [3], 2: [2, 3], 3: [1], 4: [1], 5: [2], 6: 'None'}, {1: [3, 4], 2: [2, 5], 3: [1, 2]}]

    # E.g.3: delete f1 from w2's preference list
    firms_pref = {
                        1: [[1,2],[1,5],[2,5],[1,3],[4,5],[2,4],[1,4],[3,4],[3,5],[2,3],[1],[4],[3],[2],[5]],
                        2: [[3,6],[3,5],[5,6],[2,5],[1,3],[2,6],[1,5],[1,2],[2,3],[1,6],[1],[2],[3],[5],[6]],
                        3: [[2,4],[1,2],[3,4],[2,3],[1,3],[1,4],[1],[2],[3],[4]]
              }

    workers_pref = {
                            1: [[3],[1],[2]],
                            2: [[2,3],[1,3],[1,2],[2],[3]],
                            3: [[1],[2]],
                            4: [[1],[3],[2]],
                            5: [[2],[3]],
                            6: [[1,3],[3],[1]]
                    }
    # 1. firms proposing:
    assert b.da(firms_pref, workers_pref) == [{1: [1, 3], 2: [2, 5], 3: [2, 4]}, {1: [1], 2: [2, 3], 3: [1], 4: [3], 5: [2]}]
    # 2. workers proposing:
    assert b.da(workers_pref, firms_pref) == [{1: [3], 2: [2, 3], 3: [1], 4: [1], 5: [2], 6: 'None'}, {1: [3, 4], 2: [2, 5], 3: [1, 2]}]

    # E.g.4: test a normal 1-1 DA cases:
    firms_pref = {
                        1: [[1],[3],[2],[4]],
                        2: [[4],[3],[1],[2]],
                        3: [[3],[1],[4],[2]],
                        4: [[1],[2],[3],[4]]
              }

    workers_pref = {
                        1: [[1],[4],[3],[2]],
                        2: [[3],[2],[1],[4]],
                        3: [[1],[3],[2],[4]],
                        4: [[1],[2],[3],[4]]
                }
    assert b.da(firms_pref, workers_pref) == [{1: [1], 2: [4], 3: [3], 4: [2]}, {1: [1], 2: [4], 3: [3], 4: [2]}]
