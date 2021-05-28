#i need a class for the tree root node
#i need a class for bst
# obviously functions for insertion and display and length of the tree and search element
#condition is left side child is always lesser than the parent. right side child is always
#bigger than the parent
#if same element comes, return ' value already exist in tree'
#if only one side of the tree is filled thats icalled a linked list


class node:
    def __init__(self,value=None):
        self.value=value
        self.leftchild=None
        self.rightchild=None

class tree:
    def __init__(self):
        self.root = None

    def insertion(self,value):
        if(self.root==None):
            self.root=node(value)

        else:

            self._insertion(value,self.root)

    def _insertion(self,value,cur_node):
            if(cur_node.value>value):

                if(cur_node.leftchild== None):
                    cur_node.leftchild=node(value)

                else:
                    self._insertion(value,cur_node.leftchild)

            elif(cur_node.value<value):
                if(cur_node.rightchild== None):
                    cur_node.rightchild=node(value)

                else:
                    self._insertion(value,cur_node.rightchild)
            else:
                print("sorry the number", value," already is in the tree")


    def print_tree(self):
        if(self.root==None):
            print("no tree to print")
        else:

            self._print_tree(self.root)



    def _print_tree(self,cur_node):
        if(cur_node!=None):

            print (str(cur_node.value))
            self._print_tree(cur_node.leftchild)

            self._print_tree(cur_node.rightchild)







mytree = tree()

for i in [250,10,20,15,10,11,6,8,26]:
    mytree.insertion(i)

mytree.print_tree()
