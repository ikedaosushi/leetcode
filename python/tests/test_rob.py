import pytest
from rob import Solution, TreeNode


@pytest.mark.parametrize("nums, expected", [
    ([3, 2, 3, None, 3, None, 1], 7),
    ([3, 4, 5, 1, 3, None, 1], 9)
])
def test_rob(nums, expected):
    root = TreeNode(nums[0])
    idx = 1
    queue = [root]
    while queue:
        try:
            current = queue.pop(0)
            if nums[idx]:
                left = TreeNode(nums[idx])
                current.left = left
                queue.append(left)
            idx += 1
            if nums[idx]:
                right = TreeNode(nums[idx])
                current.right = right
                queue.append(right)
            idx += 1
        except IndexError:
            break

    actual = Solution().rob(root)
    assert actual == expected
