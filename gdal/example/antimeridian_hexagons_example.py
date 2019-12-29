
import datetime
import geopandas
import os
from osgeo import gdal


def main():
    """
    Main - program execute
    """
    datadir = 'C:/Dev/example/'
  
    # read input file and convert to WGS84 / EPSG: , with bounding boxes (avoids issues at anti-meridian)
    gdal.UseExceptions()
    inputFileName = datadir + 'example.geojson'
    srcDS = gdal.OpenEx(inputFileName)
    outputFileName = datadir + 'example_output.geojson'
    ds = gdal.VectorTranslate(outputFileName, srcDS=srcDS, format = 'GeoJSON', layerCreationOptions = ['RFC7946=YES', 'WRITE_BBOX=YES'])
    # Dereference and close dataset.
    del ds
    
    exit()

if __name__ == '__main__':
    main()
