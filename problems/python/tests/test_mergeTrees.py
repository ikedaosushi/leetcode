from mergeTrees import Solution, TreeNode

"""
Input: 
	Tree 1                     Tree 2                  
          1                         2                             
         / \                       / \                            
        3   2                     1   3                        
       /                           \   \                      
      5                             4   7                  
Output: 
Merged tree
	     3
	    / \
	   4   5
	  / \   \ 
	 5   4   7
"""


def test_mergeTrees():
    tree1 = TreeNode(1)
    tree1.left = TreeNode(3)
    tree1.right = TreeNode(2)
    tree1.left.left = TreeNode(5)

    tree2 = TreeNode(2)
    tree2.left = TreeNode(1)
    tree2.right = TreeNode(3)
    tree2.left.right = TreeNode(4)
    tree2.right.right = TreeNode(7)

    actual = Solution().mergeTrees(tree1, tree2)

    assert actual.val == 3
    assert actual.left.val == 4
    assert actual.left.left.val == 5
    assert actual.left.right.val == 4
    assert actual.right.val == 5
    assert actual.right.right.val == 7
