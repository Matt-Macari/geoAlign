import orb as orb
from shapely.geometry import Point, Polygon

import matplotlib.pyplot as plt
from  matplotlib.patches import Polygon




xCords = orb.width/3 
yCords = orb.height/3

#constants
Y1 = 0
Y2 = yCords - 1
Y3 = yCords
Y4 = (yCords * 2) - 1
Y5 = yCords * 2
Y6 = yCords * 3

X1 = 0
X2 = xCords - 1
X3 = xCords
X4 = (xCords * 2) - 1
X5 = xCords * 2
X6 = xCords * 3

#define polygon 1
polygon1 = Polygon([(X1,Y1), (X2, Y1), (X2, Y2), (X1, Y2)])

polygon2 = Polygon([(X3,Y1), (X4, Y1), (X4, Y2), (X3, Y2)])

polygon3 = Polygon([(X5,Y1), (X6, Y1), (X6,Y2), (X5,Y2)])

polygon4 = Polygon([(X1,Y3), (X2, Y3), (X2, Y4), (X1, Y4)])

polygon5 = Polygon([(X3,Y3), (X4, Y3), (X4,Y4), (X3, Y4)])

polygon6 = Polygon([(X5,Y3), (X6,Y3), (X6,Y4), (X5,Y4)])

polygon7 = Polygon([(X1,Y5), (X2,Y5), (X2, Y6), (X1,Y6)])

polygon8 = Polygon([(X3,Y5), (X4, Y5),(X4, Y6), (X3, Y6)])

polygon9 = Polygon([(X5,Y5), (X6,Y5), (X6,Y6), (X5,Y6)])


polyList = [polygon1, polygon2, polygon3, polygon4, polygon5, polygon6, polygon7, polygon8, polygon9]


for each in polyList:
    fig, ax = plt.subplots()
    ax.add_patch(each)
    ax.set_xlim(0, 1410)
    ax.set_ylim(1248,0)
    plt.grid(True)
    plt.show()
    








#put polygon into lists and check each keypoint against each polygon
#and put each keypoint into corresponding polygon list
#sort each polygon list
#if polygon.contains(point):
#    print("text")
#else: 