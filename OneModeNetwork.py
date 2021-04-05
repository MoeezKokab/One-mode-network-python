# -*- coding: utf-8 -*-
"""
Created on Mon Apr  5 03:06:09 2021

@author: moeez
"""
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

df = pd.read_csv('MyData.csv')
df = df.fillna(0) #set null /empty value witho
l = 5000


ht1AllNode = [] #ht 1 mode all node
ht1AllEdge = [] # ht 1 mode all edge


# get all node, edge from CSV file(one  mode network hashtag)
def OneModeHastag():
    bad_chars = ["[", "'", "]" ] #for remove these from string  
    new_list = [] 
    
    def check_pairs(source):
        result = []
        for p1 in range(0,l): 
            for p2 in range(p1+1, len(source)):
                result.append([source[p1], source[p2]])
        return result
    
    #read all hashtags
    for i in range(0, l):
        data = df['hashtags'][i]
        # cleaning string
        if data != 0:
            #print("yes")
            test_string = ''.join(i for i in data if i not in bad_chars)
            test_string = test_string.replace(' ', '')
            test_string = test_string.lower()
            data_list = test_string.split(',')
           # print(data_list)
            pairings = check_pairs(data_list)
            for j in pairings:
                if j != '':
                    j.sort()
                   # print(j)
                    new_list.append(j)
    
    Edge = []
    counter = []
    for pair in new_list:
        count = 0
        for pairs in new_list:
            if pair == pairs:
                count += 1
        if pair not in Edge:
           # print(pair)
            Edge.append(pair)
            counter.append(count)
    
    for edge, c in zip(Edge, counter):
        edge.append(c)
    
    Edge_list = []
    
    for edges in Edge:
        Edge_list.append(tuple(edges))
    
    #print(Edge_list)
    bad_chars = ['[', "'",  ']',',']
    
    node = []
    for i in range (0 , l):
        data = df['hashtags'][i]
        if data != 0:
            test_string = ''.join(i for i in data if i not in bad_chars).lower()
            test_string = test_string.lower()
            data_list = test_string.split()
        
            for j in data_list:
                if j != '':
                    node.append(j)
    return node,Edge_list

# draw network
def Network(n,e):
    print("network")
    G = nx.Graph()
    #G = nx.petersen_graph()
    G.add_nodes_from(n)
    G.add_weighted_edges_from(e)
    print("Vertex set: ",G.nodes())

    print("Edge set: ",G.edges())
    #nx.draw(G)
    nx.draw_circular(G, with_labels=False, font_weight='bold')
    
    
# divided into sub graph
#graph is unconnected so i divided into sub Graph
    components = [G.subgraph(c).copy() for c in nx.connected_components(G)]
    for idx,g in enumerate(components,start=1):
       # print(f"Component {idx}: Nodes: {g.nodes()} Edges: {g.edges()}")
        t=nx.Graph()
        n=tuple(g.nodes())
        e=tuple(list(g.edges()))
        
        t.add_nodes_from(n)
        t.add_edges_from(e)
        # nx.draw(t)
        r = nx.radius(t) # radius
        d = t.degree #degree
        di = nx.diameter(t)
        e = nx.eccentricity(t)
        print("Radius ",r)
        print("degree",d)
        print("Diameter",di)
        print("Eccentricity",e)
        #plt.title('subplot 1 {}'.format(idx))
        plt.show()
        #save in gexf
        nx.write_gexf(G, "OneMode.gexf")
        
       
    
  






#get all node ,edge   
ht1AllNode, ht1AllEdge = OneModeHastag()



#draw network
Network(ht1AllNode,ht1AllEdge)



 
    