from typing import List


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

    def __str__(self):
        return f"val: {self.val} left: {self.left and self.left.val} right: {self.right and self.right.val} next: {self.next and self.next.val}"


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return root

        queue = [root]
        before = None
        next_queue = []
        while queue or next_queue:
            current = queue.pop(0)
            # print(
            #     f"before: {before and before.val}, current: {current and current.val}")
            if current.left:
                next_queue.append(current.left)
            if current.right:
                next_queue.append(current.right)

            if before:
                before.next = current

            if not queue:
                queue = next_queue
                next_queue = []
                before = None
            else:
                before = current

        return root


def from_nums(nums) -> Node:
    root = Node(nums[0])
    queue = [root]
    idx = 1
    while queue:
        try:
            current = queue.pop(0)
            if nums[idx]:
                left = Node(nums[idx])
                current.left = left
                queue.append(left)
            idx += 1
            if nums[idx]:
                right = Node(nums[idx])
                current.right = right
                queue.append(right)
            idx += 1
        except IndexError:
            break

    print('root:', root)
    return root


if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    actual = Solution().connect(from_nums(nums))
    queue = [actual]
    while queue:
        current = queue.pop(0)
        print(current)
        if current.left:
            queue.append(current.left)
        if current.right:
            queue.append(current.right)
