import pytest
from buildTree import Solution, TreeNode


@pytest.mark.parametrize("preorder, inorder", [
    ([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])
])
def test_buildTree(preorder, inorder):
    actual = Solution().buildTree(preorder, inorder)
    assert actual.val == 3
    assert actual.left.val == 9
    assert actual.right.val == 20
    assert actual.right.left.val == 15
    assert actual.right.right.val == 7
