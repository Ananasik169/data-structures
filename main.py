
# todo: в отдельном модуле реализовать все перечисленные методы для двусвязного списка


class Node:
  """
  Узел односвязного списка
  """
  def __init__(self, value, next: 'Node'=None):
    self.value = value
    self.next = next

  @staticmethod
  def make(items: list) -> 'Node':
    # Рекурсивная реализация:
    # return Node(items[0], Node.make(items[1:])) if items else None

    # todo: сделать нерекурсивную реализацию
    node = None
    items.reverse()
    for item in items:
      node = Node(item, node)
    return node
      
  def __iter__(self):
    node = self
    while node:
      yield node.value
      node = node.next

  def __str__(self) -> str:
    return str(list(self))

  def __repr__(self) -> str:
    '''
    > repr(Node.make([1, 2, 3]))
    Node.make([1, 2, 3])
    '''
    # todo:
    print(1)
    node = self
    print(self)
    nodes = []
    while node:
      print(2)
      nodes.append(node.value)
      node = node.next
    return f'Node.make({nodes})'
    
  # def __len__(self) -> int:
  #   print(self)
  #   print(list(self))
  #   # _len = 0
  #   # node = self
  #   # while node:
  #   #   _len += 1
  #   #   node = node.next
  #   return len(self) # todo: оптимизировать

  def repr_recursive(self) -> str:
    '''
    > repr(Node.make([1, 2, 3]))
    Node(1, Node(2, Node(3)))
    '''
    # todo:
    return f"Node({self.value}, {Node.repr_recursive(self.next) if self.next.next else f'Node({self.next.value})'})"

  def __eq__(self, other: 'Node') -> bool:
    '''Эффективное сравнение односвязных списков'''
    return list(self) == list(other)  # todo: оптимизировать

  def __reversed__(self) -> 'Node':
    ...
    # todo:
        
  def __getitem__(self, index):
    """
    > Node.make([1, 2, 3])[1]
    2

    > Node.make([1, 2, 3])[1:] == Node.make([2, 3])
    True
    """
    print(index)
    # todo:

node1a = Node(1, Node(2, Node(3)))
node1b = Node.make([1, 2, 3])
# print(node1b)
# print(node1b.__repr__)
print(node1b.__str__)

# node1a[1:5:2]


def test_reversed(lst):
  assert lst.reversed().reversed() == lst
  assert list(lst.reversed()) == list(reversed(list(lst)))