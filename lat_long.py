import os
import matplotlib.pyplot as plt
import gmplot

path = '/Users/Charlotte/Documents/Code/strava/activities/'
dirs = os.listdir(path)

lat_ride = []
lon_ride = []
lat_run = []
lon_run = []
for file in dirs:
	if not file.startswith('.'):
		if "Ride" in file:
			filename = path + file
			f = open(filename, 'rU')
			lines=f.readlines()
			f.close()
			for l in lines:
			    if "lat" in l:
			    	lat_ride.append(float(l[15:24]))
			    	lon_ride.append(float(l[32:41]))
		elif "Run" in file:
			filename = path + file
			f = open(filename, 'rU')
			lines=f.readlines()
			f.close()
			for l in lines:
			    if "lat" in l:
			    	lat_run.append(float(l[15:24]))
			    	lon_run.append(float(l[32:41]))

# plt.scatter(lon_ride, lat_ride, color = 'r')
# plt.scatter(lon_run, lat_run, color = 'g')
# #plt.xlim(xmin = -7, xmax = 2)
# #plt.ylim(ymin = 50, ymax = 58)
# plt.savefig("all")

gmap = gmplot.GoogleMapPlotter(51.45, -2.59, 12)
gmap.heatmap(lat_run, lon_run, threshold=1, radius=30, gradient=None, opacity=0.9, dissipating=True)
gmap.draw("mymap.html")
