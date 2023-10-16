import geopandas as gpd
import os

directory_path = './ttc-subway-shapefile-wgs84'

files = ['TTC_SUBWAY_LINES_WGS84.shp','TTC_SUBWAY_LINES_WGS84.shx','TTC_SUBWAY_LINES_WGS84.dbf','TTC_SUBWAY_LINES_WGS84.prj']

for file in files:
    file_path = os.path.join(directory_path, file)
    print(file_path)
    gdf = gpd.read_file(file_path)
    print(gdf.head())
    print(gdf.crs)
    print(gdf.shape)
    print(gdf.columns)
    print(gdf.dtypes)
    print(gdf.describe())
    print(gdf.info())
    print(gdf['geometry'].head())