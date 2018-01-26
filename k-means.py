# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 22:12:49 2017

@author: rjx
"""

from math import pi, sin, cos
from collections import namedtuple
from random import random, randint,sample
from copy import copy
import matplotlib.pyplot as plt

class Point:
    __slots__= ["x","y","group"]
    def __init__(self,x=0.0,y=0.0,group=0):
        self.x,self.y,self.group = x,y,group
        
        
#genarate points randomly        
def generate_points(npoints,radius):
    x = []
    y = []
    points = [Point() for _ in range(npoints)]
    for p in points:
        r = random() * radius
        ang = 2*pi*random()
        p.x = r * cos(ang)
        p.y = r * sin(ang)
    for p in points:
        x.append(p.x)
        y.append(p.y)
        plt.scatter(x,y)
    return points
        
#choose cluster centroids from initial points
def generate_centroid(k,points):
        clusters = [Point() for _ in range(k)]
        cluster = sample(range(0,99),k)
        for i in range(len(cluster)):
            clusters[i].x = points[cluster[i]].x
            clusters[i].y = points[cluster[i]].y
            clusters[i].group = i+1
        return clusters
        
def calculate(point_1,point_2):
    distance = (point_1.x-point_2.x)*(point_1.x-point_2.x)+(point_1.y-point_2.y)*(point_1.y-point_2.y)
    return distance

def update_group(points,clusters):
    while True:
        changed = 0;
        for p in points:
            mins = 10000
            ori_group = p.group
            for i in range(len(clusters)):
                dis = calculate(p,clusters[i])
                if (dis < mins):
                   mins = dis
                   p.group = i+1
            if(ori_group != p.group):
                changed = changed + 1
        update_centroid(points,clusters)
        if(changed < 5):
                break;
def update_centroid(points,clusters):
    for i in range(len(clusters)):
        sum_x = 0
        sum_y = 0
        num = 0
        for j in points:
            if(j.group == (i+1)):
                sum_x += j.x
                sum_y += j.y
                num = num + 1
    clusters[i].x = sum_x / num
    clusters[i].y = sum_y / num

def printResult(points,clusters):
    color = ["blue","green","black"]
    for i in range(len(clusters)):
        x = []
        y = []
        for p in points:
            if (p.group == i):
                x.append(p.x)
                y.append(p.y)
                plt.scatter(x,y,c = color[i])
                
def printClusters(clusters):
    x = []
    y = []
    for cluster in clusters:
        x.append(cluster.x)
        y.append(cluster.y)
        plt.scatter(x,y,c = "red")

def kmeans(npoints,k):
    points = generate_points(npoints,2)
    clusters = generate_centroid(k,points)
    update_group(points,clusters)
    printResult(points,clusters)
    printClusters(clusters)
   
    
kmeans(100,3)

    

        

        
