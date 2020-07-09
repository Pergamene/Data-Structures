from node import Node

class LinkedList:
  def __init__(self, node=None):
    self.head = node
    self.tail = node
    self.len = 0

  def add_to_head(self, data):
    node = Node(data)
    if self.len == 0:
      self.head = node
      self.tail = node
    else:
      node.set_next_node(self.head)
      self.head = node
    self.len += 1

  def remove_head(self):
    if self.len == 0:
      return None
    value = self.head.get_value()
    if self.len == 1:
      self.head = None
      self.tail = None
      self.len = 0
    if self.len > 1:
      self.head = self.head.get_next_node()
      self.len -= 1
    return value

  def add_to_tail(self, data):
    new_node = Node(data)
    if self.len == 0:
      self.head = new_node
    else:
      self.tail.set_next_node(new_node)
    self.tail = new_node
    self.len += 1

  def contains(self, data):
    if self.len == 0:
      return False
    node = self.head
    for i in range(self.len):
      if node.get_value() == data:
        return True
      node = node.get_next_node()
    return False

  def get_max(self):
    if self.len == 0:
      return None
    node = self.head
    max_value = node.get_value()
    for i in range(self.len):
      if node.get_value() > max_value:
        max_value = node.get_value()
      node = node.get_next_node()
    return max_value

  def __len__(self):
    return self.len
