from main import TreeNode, Tree

def test_f():
    tree = Tree([4, -1, 4, 1, 1])
    assert tree.depth(tree.root) == 3

def test_s():
    tree = Tree([1, -1, 1, 0, 2, 3, 3])
    assert tree.depth(tree.root) == 4

def test_t():
    tree = Tree([1, -1])
    assert tree.depth(tree.root) == 2

def tree_four():
    tree = Tree([0])
    assert tree.depth(tree.root) == 0

def tree_five():
    tree = Tree([-1])
    assert tree.depth(tree.root) == 1
