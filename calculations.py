import requests
import json

url = "https://api.wx.spire.com/forecast/route"


points = {
        "route": {"name": "my_example_route",
        "waypoints": [
            {"time": "2023-04-8T12:00:00", "lat": 40.526101, "lon": -74.039306}, #a: starting point
            {"time": "2023-04-8T13:00:00", "lat": 39.97322, "lon": -71.954218},
            
            ]
        },
        "bundles": "basic,maritime",
}

hour1 = int(points["route"]["waypoints"][0]["time"][10:12])
hour2 = int(points["route"]["waypoints"][1]["time"][10:12])

#getting the "lat": 40.526101, "lon": -74.039306 and "lat": 39.97322, "lon": -71.954218
x_coor1 = float(points["route"]["waypoints"][0]["lat"])
y_coor1 = float(points["route"]["waypoints"][0]["lon"])
x_coor2 = float(points["route"]["waypoints"][1]["lat"])
y_coor2 = float(points["route"]["waypoints"][1]["lon"])

#slope rise over run
rise = y_coor2 - y_coor1
run = x_coor2 - x_coor1
slope = rise/run

"""
print(x_coor1)
print(x_coor2)
print(y_coor1)
print(y_coor2)
print(hour1)
print(hour2)
print(rise)
print(run)
"""


while True:
    print(x_coor1)
    print(y_coor1)
    x_coor1 += slope
    y_coor1 += slope
    if x_coor1 >= x_coor2 and run > 0: #break if start is greater than end if run is increases
        break
    elif x_coor1 <= x_coor2 and run < 0: #break if start is less than end if run decreases
        break
print(x_coor1)
print(y_coor1)


    


