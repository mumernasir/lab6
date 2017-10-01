
import math

class Point(object):
  pass


def distance_between_points(Point,x,y):
  dist = math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)
  print (dist)
  
p1=Point()
p2=Point()
p1.x=5
p2.x=6
p1.y=4
p2.y=3
  
  
distance_between_points(Point,p1,p2)