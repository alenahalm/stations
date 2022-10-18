from stations.stations import Point, Station
import pytest

def points():
    return Point(-4.3, 0), Point(1.2, 12)

def triangle():
    return Point(-4.3, 0), Point(1.2, 12), Point(3, 9.8)

def area():
    return [Point(-4.3, 0), Point(1.2, 12), Point(3, 9.8), Point(5.0, -2.3)]

class TestStation:

    def test_distance(self):
        p1, p2 = points()
        assert p1.distance(p2) == pytest.approx(13.2, 0.1)
    
    def test_triangle_area(self):
        p1, p2, p3 = triangle()
        assert p1.triangle_area(p2, p3) == pytest.approx(16.5, 0.1)

    def test_min_area(self):
        points = area()
        stations = Station()
        for i in points:
            stations.add_station(i)
        assert stations.min_area() == pytest.approx(8.69, 0.1)
