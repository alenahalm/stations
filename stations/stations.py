from xmlrpc.client import MAXINT
import json


class Point:
    def __init__(self, x: float, y: float) -> None:
        self.x = x
        self.y = y

    def distance(self, other: "Point") -> float:
        return ((self.x - other.x) ** 2 + (self.y - other.y) ** 2) ** 0.5

    def triangle_area(self, p1: "Point", p2: "Point") -> float:
        a = self.distance(p1)
        b = self.distance(p2)
        c = p1.distance(p2)
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5

class Station:
    
    def __init__(self) -> None:
        self.points = []

    def add_station(self, p: Point):
        self.points.append(p)
    
    def min_area(self):
        area = MAXINT
        for i in range(len(self.points)):
            for j in range(len(self.points)):
                for k in range(len(self.points)):
                    if i != j and j != k and i != k:
                        if self.points[i].triangle_area(self.points[j], self.points[k]) < area:
                            area = self.points[i].triangle_area(self.points[j], self.points[k])
        return area

file = json.load(open('stations.json'))
st = Station()
for i in file:
    try:
        st.add_station(Point(float(i["location"]["lat"]), float(i["location"]["lon"])))
    except:
        pass
print('Calculating')
print('smallest area is', st.min_area())
