class Node:
    def __init__(self,item):
        self.next = None
        self.prev = None
        self.data =item
class DNode:
    def __init__(self):
        self.front = None
        self.tail = None
    
    # menyisipkan node di belakang list
    def push(self,newItem):
        newNode = Node(newItem)
        newNode.next = self.front
        if self.front is not None:
            self.front.prev = newNode
        self.front = newNode


    # Menyisipkan node di depan list
    def insert(self, prev, item):
        if prev is None:
            return
        NewNode = Node(item)
        NewNode.next = prev.next
        prev.next = NewNode
        NewNode.prev = prev
        if NewNode.next is not None:
            NewNode.next.prev = NewNode
    
    # Mengeprint list   
    def listprint(self, item):
        while (item is not None):
            print(item.data),
            last = item
            item = item.next
    
    # delete first
    def pop_front(self):
        if(self.front == None):    
            return;    
        else:       
            if(self.front != self.tail):    
                self.front = self.front.next;    
                self.front.prev = None;    
            else:    
                self.front = self.tail = None;    
    # DELETE LAST
    def deleteNode(self, item):
            if(self.front != None):
                if(self.front.next == None):
                    self.front = None
                else:
                    temp = self.front
                    while(temp.next != None):
                        # temp = temp.next
                        # lastNode = temp.next
                        temp.next = None
                        lastNode = None
    def hapus_node_target(self, x):
        if self.front is None:
            print("Tidak ada element yang mau dihapus")
            return 
        if self.front.next is None:
            if self.front.data == x:
                self.front = None
            else:
                print("Item tidak ditemukan")
            return 

        if self.front.data == x:
            self.front = self.front.next
            self.front.prev = None
            return
        n = self.front
        while n.next is not None:
            if n.data == x:
                break
            n = n.next
        if n.next is not None:
            n.prev.next = n.next
            n.next.prev = n.prev
        else:
            if n.data== x:
                n.prev.next = None
            else:
                print("Element tidak ditemukan")
    def menghitungMundur(self):
        temp = None
        current = self.front
        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp is not None:
            self.front = temp.prev
   
 

listq = DNode()
listq.push(47)
listq.push(90)   
listq.push(13)
listq.insert(listq.front.next, 13)
listq.listprint(listq.front)
# listq.deleteNode(listq.front)
print("Menghapus")
listq.deleteNode(listq.front.next)
listq.deleteNode(listq.front.next)
listq.hapus_node_target(1)
listq.pop_front()
print("data setelah dihapus")
listq.menghitungMundur()
listq.listprint(listq.front)