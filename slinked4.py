#write a class for node
#write a class for linked list with funcitons append,display,length,get_element,erase

class node:
    def __init__(self,data=None,next=None):
        self.data=data
        self.next=None

class linked_list:
    def __init__(self):
        self.head=node()

    def append(self,data):
        cur_node = self.head
        new_node = node(data)

        while(cur_node.next!=None):
            cur_node = cur_node.next

        cur_node.next = new_node

    def display(self):
        cur_node = self.head
        elem = []
        while(cur_node.next!=None):
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)

    def length(self):
        len_index = 0
        cur_node = self.head

        while(cur_node.next!=None):
            cur_node=cur_node.next
            len_index +=1
        return len_index

    def get_element(self,ind):
        if(ind>=self.length()):
            print('sorry index is too big of a range')
            return
        cur_node = self.head
        len_index=0
        while(cur_node.next != None):
            cur_node = cur_node.next

            if(len_index==ind):
                print(cur_node.data)

            len_index+=1

    def erase(self,ind):
        if(ind>=self.length()):
            print('sorry index is too big of a range')
            return
        cur_node = self.head
        len_index=0
        while(cur_node.next != None):
            last_node = cur_node
            cur_node = cur_node.next

            if(len_index==ind):
                last_node.next=cur_node.next

            len_index+=1

mylist = linked_list()


for i in range(0,10):
    mylist.append(i+10)

mylist.display()
print(mylist.length())
mylist.get_element(9)
mylist.erase(8)
mylist.display()
