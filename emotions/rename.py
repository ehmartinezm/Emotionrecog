import os

path = '/Users/edwin/emotions/downloads/headphones/'
files = os.listdir(path)


for index, file in enumerate(files,start=2900):
    os.rename(os.path.join(path, file), os.path.join(path, ''.join(str(index)+'.jpg')))

##Script starts at :
"""
100 Airplane
200 Cars
300 Parks
400 Trees
500 Landscape
600 Computer
700 Books
900 Phones
800 Buses
2900 Headphones
1100 Fruits
1200 Boats
1300 Stadiums
1400 Lake
1500 mountains
1600 bikes
1700 antennas
1800 bottles
1900 pencil
2000 roads


"""
