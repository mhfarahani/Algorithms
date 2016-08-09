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
        elif self.item > new_item:
            current_child = self.left_child
            if current_child:
                return current_child.insertNode(new_item)
            else:
                current_child = Node(new_item)
                return True
        else:
            current_child = self.right_child
            if current_child:
                return current_child.insertNode(new_item)
            else:
                current_child = Node(new_item)
                return True

    def find(self,an_item):
        if self.item == an_item:
            return True
        elif self.item > an_item:
            current_child = self.left_child
            if current_child:
                return current_child.find(an_item)
            else:
                return False
        else:
            current_child = self.right_child
            if current_child:
                return curretn_child.find(an_item)
            else:
                return False
            


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
                
        



tree = BinaryTree()
print(tree.insert(24))
print(tree.insert(12))
print(tree.insert(4))
print(tree.insert(24))
print(tree.insert(55))
print('---')
print(tree.isin(23))
print(tree.isin(24))
