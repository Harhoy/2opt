
import networkx
from random import randint
import numpy as np
import time
import sys

iter = int(sys.argv[1])

#route = [x for x in range(10)]

cost = 10**6

mat = np.zeros((3,10))
for i in range(len(mat)):
    mat[0][i] = 1

#print(mat)

class Node:

    def __init__(self,x,y,id):
        self._x = x
        self._y = y
        self._id = id

    def dist(self,next):
        return ((self._x - next._x)**2+(self._y - next._y)**2)**.5


route = []
for i in range(iter):
    x = randint(0,100)
    y = randint(0,100)
    route.append(Node(x,y,i))

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

def routeClipper(points,mat):
    x1 = randint(0,len(mat)-1)
    y1 = randint(0,len(mat)-1)
    x2 = randint(0,len(mat)-1)
    y2 = randint(0,len(mat)-1)


    swap = mat[x1][y1]
    mat[x1][y1] = mat[x2][y2]
    mat[x2][y2] = swap

    routes = []

    for i in range(len(mat)):
        print(len(mat))
        tempRoute = []
        for j in range(len(mat)):
            if (mat[i][j]==1):
                tempRoute.append(points[j])
                print(points[j])
        routes.append(tempRoute)

    #print(routes)
    return routes

'''
for i in range(1000):
    routes = routeClipper(route,mat)
    sumCost = 0
    for route in routes:
        optR,minCost = optimalRoute(route)
        sumCost += minCost
    print("Iterasjon",i,"Kostnad",minCost)

print(routes)
'''
start = time.time()
optR,minCost = optimalRoute(route)
end = time.time()



for r in optR:
    print("Steg:",r._id)

print("Kostnad",minCost)
print("Antall minutter",(end-start)/60)
