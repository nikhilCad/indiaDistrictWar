import geopandas as gpd

fp ="L2_data/NLS/2018/L4/L41/L4132R.shp\m_L4132R_p.shp"

data = gpd.read_file(fp)
print(data.head())