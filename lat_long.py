import os
import matplotlib.pyplot as plt
import gmplot
import webbrowser

path = '/Users/Charlotte/Documents/Code/gpx_viewer/activities/'
dirs = os.listdir(path)

lat_rides = []
lon_rides = []
lat_runs = []
lon_runs = []
for file in dirs:
	a = []
	b = []
	if not file.startswith('.'):
		if "Ride" in file:
			filename = path + file
			f = open(filename, 'rU')
			lines=f.readlines()
			f.close()
			for l in lines:
			    if "lat" in l:
			    	a.append(float(l[15:24]))
			    	b.append(float(l[32:41]))
			lat_rides.append(a)	
			lon_rides.append(b)	
		elif "Run" in file:
			filename = path + file
			f = open(filename, 'rU')
			lines=f.readlines()
			f.close()
			for l in lines:
			    if "lat" in l:
			    	a.append(float(l[15:24]))
			    	b.append(float(l[32:41]))
			lat_runs.append(a)	
			lon_runs.append(b)	

gmap = gmplot.GoogleMapPlotter(51.46, -2.59, 7)
for i in range(0, len(lat_rides)):
	gmap.plot(lat_rides[i], lon_rides[i], 'r', edge_width=3, alpha=0.3)
for i in range(0, len(lat_runs)):
	gmap.plot(lat_runs[i], lon_runs[i], 'b', edge_width=3, alpha=0.3)
gmap.draw("myactivities.html")
webbrowser.open_new_tab("file:///Users/Charlotte/Documents/Code/gpx_viewer/myactivities.html")

# lat_ride = []
# lon_ride = []
# lat_run = []
# lon_run = []
# for file in dirs:
# 	if not file.startswith('.'):
# 		if "Ride" in file:
# 			filename = path + file
# 			f = open(filename, 'rU')
# 			lines=f.readlines()
# 			f.close()
# 			for l in lines:
# 			    if "lat" in l:
# 			    	lat_ride.append(float(l[15:24]))
# 			    	lon_ride.append(float(l[32:41]))
# 		elif "Run" in file:
# 			filename = path + file
# 			f = open(filename, 'rU')
# 			lines=f.readlines()
# 			f.close()
# 			for l in lines:
# 			    if "lat" in l:
# 			    	lat_run.append(float(l[15:24]))
# 			    	lon_run.append(float(l[32:41]))

# plt.scatter(lon_ride, lat_ride, color = 'r')
# plt.scatter(lon_run, lat_run, color = 'g')
# #plt.xlim(xmin = -7, xmax = 2)
# #plt.ylim(ymin = 50, ymax = 58)
# plt.savefig("all")

# gmap = gmplot.GoogleMapPlotter(51.46, -2.59, 7)
# gmap.heatmap(lat_run, lon_run, threshold=1, radius=10, gradient=False, opacity=1, dissipating=True)
# gmap.draw("mymap.html")
# webbrowser.open_new_tab("file:///Users/Charlotte/Documents/Code/gpx_viewer/mymap.html")
