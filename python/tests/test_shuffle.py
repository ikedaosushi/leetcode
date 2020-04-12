from shuffle import Solution


def test_shuffle1():
    nums = [1, 2, 3]
    solution = Solution(nums)
    assert nums != solution.shuffle()
    assert nums == solution.reset()
    assert nums != solution.shuffle()
