import geopandas as gpd
import matplotlib.pyplot as plt

fp ="indiaDistrict/polbnda_ind.shp"

data = gpd.read_file(fp)
print(data.head())

data.plot()
plt.show()