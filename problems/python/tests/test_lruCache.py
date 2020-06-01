import pytest
from lruCache import LRUCache


@pytest.mark.parametrize("calleres,argses,expecteds", [
    (
        ["LRUCache", "put", "put", "put", "put", "get", "get"],
        [[2], [2, 1], [1, 1], [2, 3], [4, 1], [1], [2]],
        [None, None, None, None, None, -1, 3]
    )
])
def test_lru_cache(calleres, argses, expecteds):
    cache = eval(calleres[0])(*argses[0])
    for caller, args, expected in zip(calleres[1:], argses[1:], expecteds[1:]):
        actual = getattr(cache, caller)(*args)
        assert actual == expected


def test_lru_cache_simple():
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)

    assert cache.get(1) == 1
    cache.put(3, 3)
    assert cache.get(2) == -1
    cache.put(4, 4)
    assert cache.get(1) == -1
    assert cache.get(3) == 3
    assert cache.get(4) == 4


# self.put(2, 1)
# self.put(1, 1)
# self.put(2, 3)
# self.put(4, 1)
# self.get(1)
# self.get(2)
