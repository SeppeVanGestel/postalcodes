# store data in an ordered manner
# array is fixd length

# linked list heef geen lineaire order structuur maar nodes
# de node heeft een pointer naar het volgende element in de list

# twee soorten linked lists: single(kent de volgende node) and double (kent de vlogende en de vorige node)

from dataclasses import dataclass


class node:
    def __init__(self, data=None):
        self.data=data
        self.next=None #laatste node wijst naar none

class linkedlist:
    def __init__(self):
        self.head = node() # head is eerste node (een placeholder om naar het eerste element in de list te wijzen)
    # appendfunction maakt een new datapoint aan het einde van de list

    def append(self,data):
        new_node = node(data)
        cur = self.head
        while cur.next!= None:
            cur = cur.next
        cur.next = new_node

    def length(self):
        cur=self.head
        total = 0
        while cur.next !=None:
            total +=1
            cur = cur.next
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.next != None:
            cur_node=cur_node.next
            elems.append(cur_node.data)
        print(elems)
    
    def display_same(self):
        elems = []
        cur_node = self.head
        
        while cur_node.next != None:
            if cur_node == cur_node.next:
                print('ok')
            
            
            
        print(elems)    

    def get(self, index):
        if index >=self.length():
            print("ERROR: 'Get' Index out of range!")
            return None
        cur_idx=0
        cur_node=self.head
        while True:
            cur_node=cur_node.next
            if cur_idx==index: return cur_node.data
            cur_idx+=1    
    
    def erase(self, index):
        if index >=self.length():
            print("ERROR: 'Erase' Index out of range!")
            return
        cur_idx=0
        cur_node=self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.next
            if cur_idx==index:
                last_node.next = cur_node.next
                return
            cur_idx+=1        


my_list = linkedlist()            

my_list.append(0)
my_list.append(1)
my_list.append(1)
my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.display_same()



