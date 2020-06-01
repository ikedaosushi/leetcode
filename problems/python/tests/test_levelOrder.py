import pytest
from levelOrder import Solution, TreeNode


def test_levelOrder_if_null():
    assert Solution().levelOrder(None) == []


@pytest.mark.parametrize("nums, expected", [
    ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]])
])
def test_levelOrder(nums, expected):
    root = TreeNode(nums[0])
    queue = [root]
    idx = 1
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

    actual = Solution().levelOrder(root)
    assert actual == expected
