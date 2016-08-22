import os

BASE_LOCATION = Path('/home/santiago/pictures')
pics = ['travel.jpg', 'cake.png']

for pic in pics:
    path = BASE_LOCATION / pic