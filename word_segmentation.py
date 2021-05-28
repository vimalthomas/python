class node:
    def __init__(self,data=None):
        data=self.data
        next=None


class linked_list:
    def __init__(self):
        self.head=node()

    def append(self,value):
        cur_node = self.head
        new_node = node(value)
        if(curnode.next==None):
            cur_node = node(value)

        while(curnode.next!=None):

            cur_node = cur_node.next

        cur_node.next = new_node


    def display(self):
        cur_node= self.head

        while(cur_node.next!=None):
            print(cur_node.data)
            cur_node = cur_node.next



    def length(self):
        if(cur_node.next==None):
            print('nothing to print')
        cur_node=self.head
        len = 0
        while(cur_node.next!=None):
            len+=1
            cur_node = cur_node.next

        return len    
