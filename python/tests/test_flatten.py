from flatten import Solution, TreeNode


def test_flatten():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    Solution().flatten(root)

    assert root.val == 1
    assert root.right.val == 2
    assert root.right.right.val == 3
    assert root.right.right.right.val == 4
    assert root.right.right.right.right.val == 5
    assert root.right.right.right.right.right.val == 6
