
import networkx
from random import randint
import numpy as np
import time
import sys

'''
2opt algorithm for the traveling salesman problem

One parameter: the number of nodes to solve

Generates a set of random nodes and finds an "optimal" tour

'''

#No. of nodes
iter = int(sys.argv[1]) 

#Initialize cost variable
cost = 10**6


#-------CLASS-------#

#Node class
class Node:

    def __init__(self,x,y,id):
        self._x = x
        self._y = y
        self._id = id

    def dist(self,next):
        return ((self._x - next._x)**2+(self._y - next._y)**2)**.5

#-------DATA-------#
    
#Matrix of nodes (randomly generated)
route = []
for i in range(iter):
    x = randint(0,100)
    y = randint(0,100)
    route.append(Node(x,y,i))

#-------FUNCTIONS-------#

def totalDistance(route):
    dist = 0
    for k in range(0,len(route)-1):
        dist += route[k].dist(route[k+1])
    return dist

def swap(route,i,k):
    new_route = []
    for j in range(0,i):
        new_route.append(route[j])
    for j in range(k,i-1,-1):
        new_route.append(route[j])
    for j in range(k+1,len(route)):
        new_route.append(route[j])
    return new_route

def optimalRoute(route):
    cost = 10**6
    for i in range(len(route)):
        for j in range(len(route)):
            new_route = swap(route,i,j)
            new_cost = totalDistance(new_route)
            if new_cost < cost:
                route = new_route
                cost = new_cost
    return route,cost

#-------MAIN-------#

start = time.time()
optR,minCost = optimalRoute(route)
end = time.time()

for r in optR:
    print("Steg:",r._id)

print("Kostnad",minCost)
print("Antall minutter",(end-start)/60)
