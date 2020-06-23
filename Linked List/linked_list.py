class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None
    
class LinkedList:
  def __init__(self):
    self.head = None
    
  def add(self, data):
    if self.head:
      trav = self.head
      while trav.next != None:
        trav = trav.next
      trav.next = Node(data)
    else:
      self.head = Node(data)
      
  def insert_first(self, data):
      node = Node(data)
      if self.head:
          node.next = self.head
      self.head = node
      
  def find_node(self, data):
      trav = self.head
      while trav != None:
          if trav.data == data:
              return trav
          trav = trav.next
      return None
      
  def insert_after(self, after, data):
      node = find_node(after)
      if node:
          new_node = node.
      trav = self.head
      while trav.data != after and trav.next != None:
          trav = trav.next
      if trav.data == after:
          node = Node(data)
          trav.next = node
      else:
          print('Did not found {} in the list.'.format(after))
  def display(self):
    trav = self.head
    while trav != None:
      print(trav.data, end=' ')
      trav = trav.next
    print()

def main():
  animals = LinkedList()
  animals.add('Dog')
  animals.add('Cat')
  animals.add('Horse')
  animals.insert_after('Dog', 'Giraffe')
  animals.insert_first('Apple')
  animals.display()
      
if __name__ == '__main__':
  main()