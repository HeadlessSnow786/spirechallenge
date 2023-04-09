import requests
import json

headers = {
    "spire-api-key": "DaVrozYhAZbbVJVb37AccvH8PjucQXTe",
    "Content-Type": "application/json",
}
payload = json.dumps(
    {
        "route": {
            "name": "my_example_route",
            "waypoints": [
                {"time": "2023-04-8T12:00:00", "lat": 40.526101, "lon": -74.039306},
                {"time": "2023-04-8T13:00:00", "lat": 39.97322, "lon": -71.954218},
                {"time": "2023-04-8T14:00:00", "lat": 39.485893, "lon": -66.749471},
                {"time": "2023-04-8T15:00:00", "lat": 37.434774, "lon": -53.753772},
                {"time": "2023-04-8T16:00:00", "lat": 36.693392, "lon": -42.424287},
            ],
        },
        "bundles": "basic,maritime",
    }
)
url = "https://api.wx.spire.com/forecast/route"
response = requests.request("POST", url, headers=headers, data=payload)

json_data = response.json()
print(type(json_data))


"""
hour1 = int(payload["route"]["waypoints"][0]["time"][10:12])
hour2 = int(payload["route"]["waypoints"][1]["time"][10:12])
"""

#getting the "lat": 40.526101, "lon": -74.039306 and "lat": 39.97322, "lon": -71.954218
print(payload)
x_coor1 = float(json_data["data"][0]["location"]["coordinates"]["lat"])
y_coor1 = float(json_data["data"][0]["location"]["coordinates"]["lon"])
x_coor2 = float(json_data["data"][1]["location"]["coordinates"]["lat"])
y_coor2 = float(json_data["data"][1]["location"]["coordinates"]["lon"])


x_mid = (x_coor2 - x_coor1)/2
y_mid = (y_coor2 - y_coor1)/2

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


while True: #keep incrementing coordinates until reached the end
    print(x_coor1)
    print(y_coor1)
    #printing each increment
    x_coor1 += x_mid
    y_coor1 += y_mid #incrementing
    #check the coordinate if it goes above for any of the conditions

    if x_coor1 >= x_coor2 and x_mid > 0: #break if start is greater than end if run is increases
        break
    elif x_coor1 <= x_coor2 and x_mid < 0: #break if start is less than end if run decreases
        break

print(x_coor1)
print(y_coor1)



    


