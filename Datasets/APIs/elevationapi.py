import requests
import csv
import json
from elevationapi import Elevation

myrequest = 'https://api.open-elevation.com/api/v1/lookup?locations='

lat=[]
lon=[]
elevation=[]
with open('jalgaon.csv', 'rt') as csvfile:
        coords_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
        for row in coords_reader :
            row = [x.strip() for x in row[0].split(',')]
            lat1 = row[0].strip("ï»¿").replace(" ", "")
            lon1 = row[1].replace(" ", "")
            lat.append(lat1)
            lon.append(lon1)
            e = Elevation()
            axes=(float(lat1),float(lon1))
            elevation.append(str(e.getElevation(axes)))
            #print(elevation_of_Geneva)

with open('coords_altitude.csv', 'wt') as csvfile:
    altitude_writer = csv.writer(csvfile, delimiter=' ',quotechar='|', quoting=csv.QUOTE_MINIMAL)
    for i in range(len(elevation)) :
        altitude_writer.writerow(lat[i]+","+lon[i]+","+elevation[i])
##            myrequest = myrequest + lat + ',' + lon
##            #print(myrequest)
##            r = requests.get(myrequest)
##            jsonData = json.loads(r)
##            print(jsonData)
