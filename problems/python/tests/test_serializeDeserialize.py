from serializeDeserialize import Codec, TreeNode


def test_serializedeserialize_1():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    codec = Codec()
    actual = codec.deserialize(codec.serialize(root))

    assert actual.val == 1
    assert actual.left.val == 2
    assert actual.right.val == 3
    assert actual.left.left is None
    assert actual.left.right is None
    assert actual.right.left.val == 4
    assert actual.right.right.val == 5


def test_serializedeserialize_2():
    root = TreeNode(1)
    root.left = TreeNode(2)

    codec = Codec()
    actual = codec.deserialize(codec.serialize(root))

    assert actual.val == 1
    assert actual.left.val == 2
    assert actual.right is None


def test_serializedeserialize_if_null():
    codec = Codec()

    seri = codec.serialize(None)
    assert seri == ""

    deseri = codec.deserialize(seri)
    assert deseri is None
