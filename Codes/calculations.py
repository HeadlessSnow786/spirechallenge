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
                {"time": "2023-04-8T14:00:00", "lat": 40.2496605, "lon": -72.996762},
            ],
        },
        "bundles": "basic,maritime",
    }
)
url = "https://api.wx.spire.com/forecast/route"
response = requests.request("POST", url, headers=headers, data=payload)

json_data = response.json()
#print(type(json_data))


"""
hour1 = int(payload["route"]["waypoints"][0]["time"][10:12])
hour2 = int(payload["route"]["waypoints"][1]["time"][10:12])
"""

#getting the "lat": 40.526101, "lon": -74.039306 and "lat": 39.97322, "lon": -71.954218
#print(payload)
x_coor1 = float(json_data["data"][0]["location"]["coordinates"]["lat"])
y_coor1 = float(json_data["data"][0]["location"]["coordinates"]["lon"])
x_coor2 = float(json_data["data"][1]["location"]["coordinates"]["lat"])
y_coor2 = float(json_data["data"][1]["location"]["coordinates"]["lon"])
x_mid = float(json_data["data"][2]["location"]["coordinates"]["lat"])
y_mid = float(json_data["data"][2]["location"]["coordinates"]["lon"])
x_dif = x_coor2 - x_coor1
y_dif = y_coor2 - y_coor1
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

reason_list = []
danger = False
danger_cood = []
reason = "Reason(s) for danger: "
for x in range(3): #keep incrementing coordinates until reached the end
    #print(x_coor1)
    #print(y_coor1)
    wind_speed = float(json_data["data"][x]["values"]["wind_speed"])
    precip_rate = float(json_data["data"][x]["values"]["precipitation_rate"])
    visibility = float(json_data["data"][x]["values"]["surface_visibility"])
    wave_height = float(json_data["data"][x]["values"]["sea_surface_wave_significant_height"])
    if wind_speed > 8.9: #8.9 m/s is fast winds
        danger = True
        danger_cood.append((x_coor1, y_coor1))
        reason = reason + "Wind Speed is too high. "
    elif precip_rate > 0.0035: #0.5 inch/hr is considered high precipitation rate
        danger = True
        danger_cood.append((x_coor1, y_coor1))
        reason = reason + "Precipiation rate is too high. "
    elif visibility < 3704: #2 nautical miles or less considered poor visibility
        danger = True
        danger_cood.append((x_coor1, y_coor1))
        reason = reason + "Surface Visibility is too low. "
    elif wave_height > 5:
        danger = True
        danger_cood.append((x_coor1, y_coor1))
        reason = reason + "Waves are too high."
    x_coor1 += x_dif
    y_coor1 += y_dif 
    reason_list.append(reason)
    print(x_coor1)
    print(y_coor1)

if reason_list[0] == "Reason(s) for danger: ":
    print("This route looks safe. ")
else:
    print(set(danger_cood))
    print(reason_list)



