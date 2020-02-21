import pytest
from isValidBST import Solution, TreeNode


def test_isValidBST_if_null():
    assert Solution().isValidBST(None)


@pytest.mark.parametrize("nums, expected", [
    ([10, 5, 15, None, None, 6, 20], False),
    ([1, 1], False),
    ([2, 1, 3], True),
    ([5, 1, 4, None, None, 3, 6], False)
])
def test_isValidBST(nums, expected):
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

    actual = Solution().isValidBST(root)
    assert actual == expected
