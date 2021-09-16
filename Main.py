from library2 import detect
from shapely import geometry
import cv2


class object:
    def __init__(self, id, xcoo, ycoo, date_arrival, date_departure, duration):
        self.id = id
        self.xcoo = xcoo
        self.ycoo = ycoo
        self.date_arrival = date_arrival
        self.date_departure = date_departure
        self.duration = duration
#First step: gather previous cross locations.
list_old = []
list_old.append( object(id= 1, xcoo= 50, ycoo = 50, date_arrival=0, date_departure=0, duration=0))
#Second step: gather current object positions and Time.
conf = 0.4
nms = 0.5
imagepath = 'img/E9Y2DJ.jpg'
list = detect(conf, nms, imagepath)
for object in list:
    print(object.xcoo)

#Check for each result in OLD list wheter it is in range of the new results
#If so, keep in list, if not so, delete.
# create your two points
for object_old in list_old:
    point_old = geometry.Point(object_old.xcoo, object_old.ycoo)
    # create your circle buffer from one of the points
    foundpoint = False
    distance = 10
    circle_buffer = point_old.buffer(distance)
    for object_new in list:
        point_new = geometry.Point(object_new.xcoo, object_new.ycoo)
        # and you can then check if the other point lies within
        if point_new.within(circle_buffer):
            print('point 2 is within the distance buffer of point 1')
            foundpoint = True
        else:
            foundpoint = False
    if not foundpoint:
        list_old.remove(object_old)