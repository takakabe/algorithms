import queue

def breadth_first_search(graph, root_node, destination):
  search_queue = queue.Queue()
  search_queue.put(graph[root_node])
  searched = []

  while not search_queue.empty():
    node_children = search_queue.get()
    for current in node_children:
      if current == destination:
        return('find '+current)
      else:
        searched.append(current)
        if graph[current] is not None and current is not searched:
          search_queue.put(graph[current])
  return(current+'is not found')


if __name__ == '__main__':
  root_node = 'Frankfurt'
  destination = 'Stuttgart'

  graph = {}
  graph['Frankfurt'] = ['Mannheim', 'Wurzburg', 'Kassel',]
  graph['Mannheim'] = ['Karlsruhe',]
  graph['Wurzburg'] = ['Nurunberg', 'Erfurt',]
  graph['Kassel'] = ['Munchen',]
  graph['Karlsruhe'] = ['Augsburg',]
  graph['Nurunberg'] = ['Stuttgart',]
  graph['Erfurt'] = []
  graph['Munchen'] = []
  graph['Augsburg'] = []
  graph['Stuttgart'] = []

  print(breadth_first_search(graph, root_node, destination))
