from stations.stations import Station, Point
import json

file = json.load(open('stations.json'))
st = Station()
for i in file:
    try:
        st.add_station(Point(float(i["location"]["lat"]), float(i["location"]["lon"])))
    except:
        pass
print('Calculating')
print('smallest area is', st.min_area())
