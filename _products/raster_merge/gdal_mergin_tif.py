from osgeo import gdal
import pandas as pd
import os

#read csv table 
files = pd.read_csv("table_from_shapefile.csv")
#take only grid column as it contains the name of files
filenames = files["grids"]

#make a list of filenames
demnames = []
for names in filenames:
    name = "Grid/"+str(names)+"DEM.tif"
    #check if file exists, if so, append to list
    if os.path.exists(name) == True:
         demnames.append(name)

#copy demnames
files_to_mosaic = demnames
g = gdal.Warp("output.tif", files_to_mosaic, format="GTiff",
              options=["COMPRESS=LZW", "TILED=YES"]) 

# Close file and flush to disk
g = None 
