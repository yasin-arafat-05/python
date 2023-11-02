#creating node class
#class name should be in PascalCase
class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next
    
#creatign linked list class
class LinkedList:
    def __init__(self):
        self.head = None

    #insert element at the begining 
    def insertAtBeganing(self,data):
        node = Node(data,self.head)
        self.head = node

    #insert element at the end
    def insertAtEnd(self,data):
        #if linked list is empty
        if self.head == None:
            self.head = Node(data,None)
            return 
        #if linked list is not empty
        ptr = self.head
        while ptr.next:
            ptr = ptr.next
        ptr.next = Node(data,None)

    #get length of the linked list
    def getLength(self):
        ptr = self.head
        cnt = 0
        while ptr:
            cnt +=1
            ptr = ptr.next
        return cnt
    
    #insert element at middle
    def insert_at(self,index,data):
        if index<0 or index> self.getLength():
            raise Exception("Invalid Index")
        # index == 0 insert at beginning
        if index==0:
            self.insertAtBeganing(data)
            return
        # insert at middle and last
        ptr = self.head
        cnt = 0
        while ptr:
            if cnt== index-1:
                node = Node(data,ptr.next)
                ptr.next = node
                break
            ptr = ptr.next
            cnt+=1
    #traverse all data element 
    #store data in a string then print all data
    def traverse(self):
        ptr = self.head
        output = ""
        while ptr:
            prefix = "--->" if ptr.next else ""
            output += str(ptr.data) + prefix
            ptr = ptr.next
        print(output)
    #remove element from linked list
    def remove_at(self,index):
        if index<0 or index>self.getLength():
            raise Exception("Invalid index")
        #delete first element
        if index==0:
            self.head = self.head.next
            return
        #delete rather than first
        ptr = self.head
        cnt = 0
        while ptr:
            if cnt == index-1:
                ptr.next = ptr.next.next
                break
            ptr = ptr.next
            cnt+=1
    #insert value as a list
    def insertValues(self,data_list):
        for i in data_list:
            self.insertAtEnd(i)

#define main funciton:
if __name__ == "__main__":
    root = LinkedList()
    root.insert_at(0,12)
    root.insert_at(1,14)
    root.insert_at(1,13)
    root.insert_at(0,10)
    root.insert_at(1,11)
    root.traverse()
    root.remove_at(4)
    root.traverse()
    root.insertValues([1,2,3,4,5])
    root.traverse()
    print(f"Length: {root.getLength()}")