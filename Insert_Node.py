# Click on Run Code button to see the result

# node structure
class Node:
  def __init__(self, data):
    self.data = data
    self.next = None

#class Linked List
class LinkedList:
  def __init__(self):
    self.head = None

  #Add new element at the start of the list
  def push_front(self, newElement):
    newNode = Node(newElement)
    newNode.next = self.head
    self.head = newNode

  #display the content of the list
  def PrintList(self):
    temp = self.head
    if(temp != None):
      print("The list contains:", end=" ")
      while (temp != None):
        print(temp.data, end=" ")
        temp = temp.next
      print()
    else:
      print("The list is empty.")

# test the code
MyList = LinkedList()

#Add three elements at the start of the list.
MyList.push_front(10)
MyList.push_front(20)
MyList.push_front(30)
MyList.PrintList()
