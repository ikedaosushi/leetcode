class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def queue_has_data(self, queue):
        return bool([q for q in queue if q])

    def serialize(self, root: TreeNode) -> str:
        if not root:
            return ""
        data = []
        queue = [root]
        while self.queue_has_data(queue):
            current = queue.pop(0)
            if current:
                queue.extend([current.left, current.right])
            data.append(str(current.val) if current else "#")

        if len(data) % 2 == 0:
            data.append("#")
        print(",".join(data))
        return ",".join(data)

    def deserialize(self, data: str) -> TreeNode:
        if not data:
            return None
        nums = [int(d) if d != "#" else d for d in data.split(",")]
        root = TreeNode(nums[0])
        queue = [root]
        idx = 1
        while queue and idx < len(nums):
            current = queue.pop(0)
            print("current:", current.val)
            print("left, nums[idx]:", nums[idx])
            if nums[idx] != "#":
                current.left = TreeNode(nums[idx])
                queue.append(current.left)
            idx += 1

            print("right, nums[idx]:", nums[idx])
            if nums[idx] != "#":
                current.right = TreeNode(nums[idx])
                queue.append(current.right)
            idx += 1

        return root


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    codec = Codec()
    s = codec.serialize(root)
    root = codec.deserialize(s)

    queue = [root]
    while queue:
        current = queue.pop(0)
        if current:
            print(current.val)
            queue.append(current.left)
            queue.append(current.right)
