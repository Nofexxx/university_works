class TreeNode:
    def __init__(self):
        self.children = []

    def addChild(self, child):
        self.children.append(child)

class Tree:
    def __init__(self, inarray):
        self.root = None
        node_list = [None]*len(inarray)
        for i in range(0, len(inarray)):
            node_list[i] = TreeNode()
        for i in range(0, len(inarray)):
            if inarray[i] == -1:
                self.root = node_list[i]
            else:
                node_list[inarray[i]].addChild(node_list[i])

    def depth(self, root):
        if root is None:
            return 0
        result = 1
        for i in range(0, len(root.children)):
            result = max(result, 1 + self.depth(root.children[i]))
        return result


if __name__ == '__main__':
    some_value = int(input())
    inarray1 = list(map(int, input().split()))

    tree = Tree(inarray1)
    print(tree.depth(tree.root))