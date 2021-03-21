import breadth_first_search

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

breadth_first_search.breadth_first_search(graph, 'Frankfurt', 'Augsburg')
