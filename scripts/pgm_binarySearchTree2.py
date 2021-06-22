#createa  class for roote node
class node:
    def __init__(self,value=None):
        self.value=value
        self.leftchild=None
        self.rightchild=None

#create a class for tree node
class tree:
    def __init__(self):
        self.root=None

#funtion for insertion
    def insertion(self,value):
        if(self.root==None):
            self.root = node(value)
        else:
            self._insertion(self.root,value)

    def _insertion(self,cur_node,value):
        if(cur_node.value>value):
            if(cur_node.rightchild==None):
                cur_node.rightchild=node(value)
            else:
                self._insertion(cur_node.rightchild,value)
        elif(cur_node.value<value):
            if(cur_node.leftchild==None):
                cur_node.leftchild=node(value)
            else:
                self._insertion(cur_node.leftchild,value)
        else:
            print('sorry the value already in the tree')


    def print_tree(self):
        if(self.root==None):
            print('no tree to print')
        else:
            self._print_tree(self.root)

    def _print_tree(self,cur_node):
        if(cur_node!=None):
            print(cur_node.value)
            self._print_tree(cur_node.leftchild)
            self._print_tree(cur_node.rightchild)


    def search_tree(self,elem):
        if(self.root==None):
            print('no tree to search')
        else:
            self._search_tree(self.root,elem)

            print('elem not in the tree')

    def _search_tree(self,cur_node,elem):
        if(cur_node!=None):

            if(cur_node.value==elem):
                print('the elem is in the tree')
                res=True
                return True
            else:

                self._search_tree(cur_node.leftchild,elem)
                self._search_tree(cur_node.rightchild,elem)
                


mytree = tree()

for i in [250,10,20,15,10,11,6,8,26]:
    mytree.insertion(i)

mytree.print_tree()
mytree.search_tree(10)





#function for print
