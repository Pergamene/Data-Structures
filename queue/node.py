class Node:
  def __init__(self, value):
    self.value = value
    self.next_node = None

  def set_value(self, value):
    self.value = value

  def set_next_node(self, node):
    self.next_node = node
  
  def get_value(self):
    return self.value

  def get_next_node(self):
    return self.next_node
