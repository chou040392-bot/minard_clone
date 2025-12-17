from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import sqlite3
import pandas as pd

connection = sqlite3.connect("data/minard.db")
city_df = pd.read_sql("SELECT * FROM cities;", con = connection)
temperature_df = pd.read_sql("""SELECT * FROM temperatures;""", con=connection)
troop_df = pd.read_sql("""SELECT * FROM troops;""", con = connection)
directions = troop_df["direc"].values
survivals = troop_df["surviv"].values
connection.close()


loncs = city_df["lonc"].values
latcs = city_df["latc"].values
city_names = city_df["city"].values
rows = troop_df.shape[0]
lonps = troop_df["lonp"].values
latps = troop_df["latp"].values
fig, axes = plt.subplots(nrows = 2, figsize = (25,12), gridspec_kw = {"height_ratios":[4, 1]})
m = Basemap(projection='lcc',resolution='i', width = 1000000,
                    height = 400000, lon_0 =31, lat_0 = 55, ax = axes[0])
m.drawcountries()
m.drawrivers()
m.drawparallels(range(54,58), labels = [True,False, False, False])
m.drawmeridians(range(23,56,2), labels = [False, False, False, True])
x, y = m(loncs, latcs)
for xi, yi, city_name in zip (x, y, city_names):
    axes[0].annotate(text = city_name, xy = (xi,yi), fontsize = 12, zorder = 2)
x,y = m(lonps, latps)
for i in range(rows - 1):
    if directions[i] == "A":
        line_color = "tan"
    else:
        line_color = "black"
    start_stop_lons = (x[i], x[i+1])
    start_stop_lats = (y[i], y[i+1])
    line_width = survivals[i]
    m.plot(start_stop_lons,start_stop_lats, linewidth = line_width/10000, color = line_color, zorder =1)
plt.show()



"""
temp_celsius = (temperature_df["temp"]*5/4).values
lont = temperature_df["lont"].values
fig, ax = plt.subplots()
ax.plot(lont, temp_celsius)
plt.show()
"""

"""

rows = troop_df.shape[0]
lons = troop_df["lonp"].values
lats = troop_df["latp"].values
survivals = troop_df["surviv"].values
directions = troop_df["direc"].values
fig, ax = plt.subplots()
for i in range(rows - 1):
    if directions[i] == "A":
        line_color = "tan"
    else:
        line_color = "black"
    start_stop_lons = (lons[i], lons[i+1])
    start_stop_lats = (lats[i], lats[i+1])
    line_width = survivals[i]
    ax.plot(start_stop_lons,start_stop_lats, linewidth = line_width/10000, color = line_color)
plt.show()
"""