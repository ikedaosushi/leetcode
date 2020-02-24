import pytest
from isSymmetric import Solution, TreeNode


def test_isSymmetric_if_null():
    assert Solution().isSymmetric(None)


@pytest.mark.parametrize("nums, expected", [
    ([1, 2, 2, 3, 4, 4, 3], True),
    ([1, 2, 2, None, 3, None, 3], False)
])
def test_isSymmetric(nums, expected):
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

    actual = Solution().isSymmetric(root)
    assert actual == expected
