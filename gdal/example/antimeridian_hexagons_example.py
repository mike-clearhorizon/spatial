
import datetime
import geopandas
import os
from osgeo import gdal


def main():
    """
    Main - program execute
    """
    datadir = 'C:/Dev/example/'
  
    gdal.UseExceptions()
    srcDS = gdal.OpenEx(datadir + 'input.geojson')
    ds = gdal.VectorTranslate(datadir + 'output.geojson', srcDS=srcDS, format = 'GeoJSON', layerCreationOptions = ['RFC7946=YES', 'WRITE_BBOX=YES'])
    
    exit()

if __name__ == '__main__':
    main()
