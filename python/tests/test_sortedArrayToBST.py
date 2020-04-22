import pytest
from sortedArrayToBST import Solution, TreeNode
from utils.binary_tree import from_nums


@pytest.mark.parametrize("nums, expected", [
    ([-10, -3, 0, 5, 9], [0, -3, 9, -10, None, 5])
])
def test_sortedArrayToBST(nums, expected):
    actual = Solution().sortedArrayToBST(nums)
    expected = from_nums(expected)

    actual_queue = [actual]
    expected_queue = [expected]

    while expected_queue:
        actual = actual_queue.pop(0)
        expected = expected_queue.pop(0)

        assert actual.val == expected.val

        for queue, node in [(actual_queue, actual), (expected_queue, expected)]:
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
