# Detect and Remove Loop in a Linked List

# Write a function detectAndRemoveLoop() that checks whether a given Linked List contains loop and if loop is present then removes the loop and returns true. If the list doesn’t contain loop then it returns false. Below diagram shows a linked list with a loop. detectAndRemoveLoop() must change the below list to 1->2->3->4->5->NULL.

class Node :
    def __init__ ( self , data ) :
        self.data = data
        self.next = None

class LinkedList :
    def __init__ ( self ) :
        self.head = None
    
    def printList ( self ) :
        temp = self.head
        while ( temp ) :
            print ( temp.data )
            temp = temp.next
        
    def add ( self , data ) :
        if self.head != None :
            last = self.head
            end = self.head
            while ( end ) : 
                last = end
                end = end.next
            last.next = Node ( data )
        else : self.head = Node ( data )
    
    def detectAndResolveLoop ( self ) :
        prev = self.head
        temp = self.head
        while ( temp ) :
            if temp.flag == 1 : break
            prev = temp
            temp.flag = 1
            temp = temp.next
        prev.next = None

llist = LinkedList()
llist.add ( 1 )
llist.add ( 2 )
llist.add ( 3 )
llist.add ( 4 )
llist.add ( 5 )
llist.head.next.next.next.next.next = llist.head
# llist.printList()
llist.detectAndResolveLoop()
llist.printList()
