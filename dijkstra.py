# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 14:14:28 2022

@author: 13072
"""

import matplotlib.pyplot as plt 
import networkx as nx 
import math
import numpy as np
from matplotlib import animation
import copy 

infinity = math.inf


def dijkstra(G,start):
    dist = {v: infinity for v in list(G)}
    prev = {v: "Undefined" for v in list(G)}
    Q = [v for v in list(G)]
    dist[start] = 0
    
    while (Q):
        current = min(Q,key=dist.get)
        Q.remove(current)
        for n in G.neighbors(current):
            
            if n in Q:
                e = G.edges[current,n]
                weight = e['weight']
                newPath = weight + dist[current]
                
                if ((newPath < dist[n]) and (not dist[current]==infinity)):
                    dist[n] = newPath
                    prev[n] = current

    return (dist,prev) 

# Build plot
fig, ax = plt.subplots(figsize=(6,4))

# Create a graph and layout
G = nx.Graph()

done = False 
while (not done):
    start = input("enter starting node: ")
    end = input ("enter ending node: ")
    w = int(input("enter weight: "))
    G.add_edge(start,end,color ='black',weight=w )
    d = input("are you done? Y/N: ")
    if (d == 'Y'):
        done = True

previous = dijkstra(G,list(G)[0])[1]
node = input("Enter the destination node: ")
layout = nx.spring_layout(G)
while (not previous[node] == 'Undefined'):
    G[node][previous[node]]['color'] = 'r'
    node = previous[node]
colors = [G[u][v]['color'] for u,v in G.edges()]
print(colors)
nx.draw(G, pos=layout, edge_color=colors, width=2, with_labels = True)

