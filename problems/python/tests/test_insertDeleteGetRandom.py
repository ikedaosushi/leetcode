from insertDeleteGetRandom import RandomizedSet


def test_insertDeleteGetRandom():
    randomSet = RandomizedSet()
    assert(randomSet.insert(1))
    assert(not randomSet.remove(2))
    assert(randomSet.insert(2))
    assert(set(randomSet.getRandom() for _ in range(1000)) == {1, 2})
    assert(randomSet.remove(1))
    assert(not randomSet.insert(2))
    assert(set(randomSet.getRandom() for _ in range(1000)) == {2})
