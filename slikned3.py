
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
        cur_node = self.head
        len_index = 0
        while(cur_node.next!=None):
            cur_node = cur_node.next
            len_index+=1

        return len_index

    def get_element(self,ind):
        if(ind>=self.length()):
            print("sorry too big")
        else:
            cur_node = self.head
            len_index = 0

            while(cur_node.next!=None):
                cur_node = cur_node.next
                if(ind==len_index):
                    print(cur_node.data)
                len_index+=1


    def erase(self,ind):
        if(ind>=self.length()):
            print("sorry too big")
        else:
            cur_node = self.head
            len_index = 0

            while(cur_node.next != None):
                last_node = cur_node
                cur_node = cur_node.next
                if(len_index==ind):
                    last_node.next = cur_node.next
                len_index+=1


list1 = linked_list()

for i in range(0,100):
    list1.append(i+1)

list1.display()

list1.get_element(40)

list1.erase(40)

list1.display()
