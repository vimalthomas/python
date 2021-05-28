class node:
    def __init__(self,value=None):
        self.value = value
        self.leftchild = None
        self.rightchild = None


class tree:
    def __init__(self):
        self.root = None

    def insertion(self,value):

        if(self.root==None):
            self.root=node(value)
        else:
            #print('the head element is already existing')
            self._insertion(self.root,value)

    def _insertion(self,curnode,elem):


        if(curnode.value>elem):
            if(curnode.rightchild==None):
                #print('rightchild value is none')
                curnode.rightchild=node(elem)
            else:
                self._insertion(curnode.rightchild,elem)
        elif(curnode.value<elem):
            if(curnode.leftchild==None):
                curnode.leftchild=node(elem)
            else:
                self._insertion(curnode.leftchild,elem)
        elif(curnode.value==elem):
            print('element already is existing')



    def display(self):
        if(self.root==None):
            print('nothing to print')
        else:
            print('start of display')
            #print(self.root.value)
            self._display(self.root)

    def _display(self,curnode):
        #print('start ',curnode.value)
        if(curnode!=None):
            print(curnode.value)
            #print('start of leftchild')
            self._display(curnode.leftchild)
            #print('start of rightchild')
            self._display(curnode.rightchild)




lst = [10,20,1,2,30,40,4,5]

bst = tree()

for i in lst:
    print(i)
    bst.insertion(i)


bst.display()
