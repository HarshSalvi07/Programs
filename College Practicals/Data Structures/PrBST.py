class Node :
    def __init__(self,data):
        self.data = data
        self.left = self.right = None
class BST:
    def __init__(self):
        self.root = None
    def insert(self,data):
         if self.root is None:
            self.root = Node(data)
            return
         else:
            self._insert(data,self.root)
    def _insert(self,data,root):
        
        if root is None:
            return Node(data)
        if data > root.data:
            root.right = self._insert(data,root.right)
        else:
            root.left = self._insert(data,root.left)
        return root
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            print(root.data," ",end=" ")
            self.inorder(root.right) 
    def preorder(self,root):
        if root:
            print(root.data," ",end=" ")
            self.inorder(root.left)
            self.inorder(root.right)
    def postorder(self,root):
        if root:
            self.inorder(root.left)  
            self.inorder(root.right)
            print(root.data," ",end=" ")
if __name__ == "__main__":
 t = BST()
 t.insert(20)
 t.insert(10)
 t.insert(30)
 t.inorder(t.root)
 print()
 t.preorder(t.root)
 print()
 t.postorder(t.root)