## Binary Search Tree Algorithm

class Node(object):
    ''' '''
    def __init__ (self,item):
        self.item = item
        self.left_child = None
        self.right_child = None

    def insertNode(self,new_item):
        if self.item == new_item:
            print('Item already exist!')
            return False
        else:
            if self.item > new_item:
                if self.left_child:
                    return self.left_child.insertNode(new_item)
                else:
                    self.left_child = Node(new_item)
                    return True
            else:
                if self.right_child:
                    return self.right_child.insertNode(new_item)
                else:
                    self.right_child = Node(new_item)
                    return True

    def find(self,an_item):
        if self.item == an_item:
            return True
        else:
            if self.item > an_item:
                current_child = self.left_child
            else:
                current_child = self.right_child
                
            if current_child:
                return current_child.find(an_item)
            else:
                return False

    def traversal(self,method):
        if self:
            if method == 'preorder':
                print(self.item)
            if self.left_child:
                self.left_child.traversal(method)
            if method == 'inorder':
                print(self.item)
            if self.right_child:
                self.right_child.traversal(method)
            if method == 'postorder':
                print(self.item) 


class BinaryTree(object):
    ''' '''
    def __init__ (self):
        self.root = None

    def insert(self,item):
        if self.root:
            return self.root.insertNode(item)
        else:
            self.root = Node(item)
            return True

    def isin(self,item):
        if self.root:
            return self.root.find(item)
        else:
            return False

    def preorderTraversal(self):
        print('-------------------')
        print('Preorder Traversal:')
        if self.root:
            self.root.traversal('preorder')
        print('-------------------')

    def inorderTraversal(self):
        print('-------------------')
        print('Inorder Traversal:')
        if self.root:
            self.root.traversal('inorder')
        print('-------------------')

    def postorderTraversal(self):
        print('-------------------')
        print('Postorder Traversal:')
        if self.root:
            self.root.traversal('postorder')
        print('-------------------')


            



tree = BinaryTree()
print(tree.insert(24))
print(tree.insert(12))
print(tree.insert(4))
print(tree.insert(12))
print(tree.insert(55))
print(tree.insert(33))
print('---')
print(tree.isin(23))
print(tree.isin(55))
tree.preorderTraversal()
tree.postorderTraversal()
tree.inorderTraversal()
