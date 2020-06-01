import pytest
from inorderTraversal import Solution, TreeNode


@pytest.mark.parametrize("nums, expected", [
    ([1, None, 2, 3], [1, 3, 2])
])
def test_inorderTraversal(nums, expected):
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

    actual = Solution().inorderTraversal(root)
    assert actual == expected


def test_inorderTraversal_if_null():
    assert Solution().inorderTraversal(None) == []
