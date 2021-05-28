#i am here to create linked list


# first create a class for the node ->this will awlasy be a subclass

class node:
    def __init__(self,data=None):
        "this is a docstring for class node"
        self.data = data
        self.next = None



#create a linked list class and initiate header node as an attribute

class linked_list:
    def __init__(self):
        self.head = node()


#we could start creating functions like append

#append
    def append(self,data):
        cur_node = self.head
        new_node = node(data)
        while(cur_node.next!=None):
            cur_node = cur_node.next
        cur_node.next = new_node



#length
    def length(self):
        len_count = 0
        cur_node = self.head
        #new_node = node()
        while(cur_node.next!=None):
            cur_node = cur_node.next
            len_count += 1

        return len_count

#display
    def display(self):
        elem = []
        cur_node = self.head
        #new_node = node()
        while(cur_node.next!=None):
            cur_node = cur_node.next
            elem.append(cur_node.data)
        print(elem)

#erase
    def erase(self,ind):
        if(ind>=self.length()):
            print("the length is bigger than the index")
            new_node = node()
        else:
            cur_node=self.head
            ind_length=0
            while(cur_node.next!=None):
                last_node = cur_node
                cur_node=cur_node.next
                if(ind==ind_length):
                    last_node.next = cur_node.next
                    return
                ind_length+=1


#get a data element at an index

    def get_element(self,ind):
        if(ind>=self.length()):
            print("the length is bigger than the index")
        else:
            ind_length = 0
            cur_node=self.head
            while(cur_node.next!=None):
                cur_node=cur_node.next
                if(ind==ind_length):
                    print(cur_node.data)
                    return(cur_node.data)
                else:
                    ind_length+=1








my_list = linked_list()
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append('vimal')
my_list.display()
my_list.get_element(3)
print('length of my linked list is',my_list.length())
my_list.erase(3)
my_list.display()
