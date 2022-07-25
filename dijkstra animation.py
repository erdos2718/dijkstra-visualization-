# -*- coding: utf-8 -*-
"""
Created on Sun Jul 10 14:09:39 2022

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
    colors = {v: "blue" for v in list(G)}
    dist[start] = 0
    steps = []
    
    while (Q):
        current = min(Q,key=dist.get)
        
        colors[current] = 'red'
        colors1 = copy.deepcopy(colors)
        steps.append(colors1)
        print(current)
        Q.remove(current)
        for n in G.neighbors(current):
            
            if n in Q:
                e = G.edges[current,n]
                weight = e['weight']
                print (weight)
                newPath = weight + dist[current]
                
                if ((newPath < dist[n]) and (not dist[current]==infinity)):
                    dist[n] = newPath
                    print (dist)
                    prev[n] = current

    return steps       

def simple_update(num,steps, layout, G, ax):
    ax.clear()
    # Draw the graph with random node colors
    edges = G.edges()
    # G['a']['b']['color']= 'g'
    
    colors = list(steps[num].values())
    
    nx.draw(G, pos=layout, node_color=colors, width=0.5)
    # Set the title
    ax.set_title("Frame {}".format(num))

def simple_animation():

    # Build plot
    fig, ax = plt.subplots(figsize=(6,4))

    # Create a graph and layout
    G = nx.Graph()

    G.add_edge("a", "b", color= 'black', weight=0.6)
    G.add_edge("b", "c",color= 'black', weight=0.2)
    G.add_edge("c", "d",color= 'black', weight=0.1)
    G.add_edge("a", "e",color= 'black', weight=500)
    G.add_edge("e", "f",color= 'black', weight=800)
    G.add_edge("f", "d",color= 'black', weight=1)
    steps = dijkstra(G,list(G)[0])
    layout = nx.spring_layout(G)

    ani = animation.FuncAnimation(fig, simple_update, len(steps), fargs=(steps,layout, G, ax))
    ani.save('animation_1.gif', writer='imagemagick')

    plt.show()

simple_animation()    
        