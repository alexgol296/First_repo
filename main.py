from math import sin, cos, sqrt, atan2, radians

# Approximate radius of earth in km
RADIUS = 6371.01
R = 6371.01

lat1 = radians(50.45)
lon1 = radians(30.523)
lat2 = radians(51.5072)
lon2 = radians(-0.1275)

dlon = lon2 - lon1
dlat = lat2 - lat1

a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
c = 2 * atan2(sqrt(a), sqrt(1 - a))

distance = 6371.01 * c
print(distance)
