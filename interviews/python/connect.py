class Solution:
    def connect(self, root: 'Node') -> 'Node':
        old_root = root
        prekid = Node(0)
        kid = prekid   # Let kid point to prekid
        while root:
            while root:
                if root.left:
                    kid.next = root.left
                    kid = kid.next
                if root.right:
                    kid.next = root.right
                    kid = kid.next
                root = root.next
            root, kid = prekid.next, prekid
            kid.next = None  # Reset the chain for prekid
        return old_root
