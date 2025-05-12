import geopandas as gpd
import contextily as ctx
import matplotlib.pyplot as plt
from shapely.geometry import box
from pyproj import Transformer
from math import radians, cos
from PIL import Image

from pyproj import Transformer
import geopandas as gpd
from shapely.geometry import box
import matplotlib.pyplot as plt
import contextily as ctx
from math import cos, radians

def saveMap(lon, lat, size=1000, filename='temp.png'):
    """
    Generates and saves a size x size meter map image (1m/pixel) centered on given coordinates.
    This accounts for Earth curvature and varying distances between latitudes and longitudes.
    """

    # Setup the map
    source=ctx.providers.CartoDB.VoyagerNoLabels

    # Calculate distances for 1 degree of latitude and longitude at the given latitude
    lat_degree_in_meters = 111320  # Approximate meters per degree of latitude (at the equator)
    lon_degree_in_meters = lat_degree_in_meters * cos(radians(lat))  # Varies with latitude

    # Half size of the bounding box in meters (half in each direction)
    half_size = size / 2

    # Calculate the bounding box in lat/lon
    delta_lat = half_size / lat_degree_in_meters
    delta_lon = half_size / lon_degree_in_meters

    min_lat = lat - delta_lat
    max_lat = lat + delta_lat
    min_lon = lon - delta_lon
    max_lon = lon + delta_lon

    # Convert lat/lon to EPSG:3857 (meters) using pyproj
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
    minx, miny = transformer.transform(min_lon, min_lat)
    maxx, maxy = transformer.transform(max_lon, max_lat)

    # Create a bounding box GeoDataFrame
    bbox = box(minx, miny, maxx, maxy)
    gdf = gpd.GeoDataFrame({'geometry': [bbox]}, crs="EPSG:3857")

    # Correct figure size calculation: size meters / 100 pixels per inch (100 DPI)
    fig_width = size / 100
    fig_height = size / 100

    # Create figure with specific size and DPI
    fig, ax = plt.subplots(figsize=(fig_width, fig_height), dpi=100)

    # Set the extent to the bounding box
    ax.set_xlim(minx, maxx)
    ax.set_ylim(miny, maxy)

    # Plot the bounding box with no edge
    gdf.plot(ax=ax, edgecolor='none', alpha=0)

    # Add high-contrast no-label basemap
    ctx.add_basemap(ax, crs=gdf.crs, source=source, zoom=19)

    # Remove axis for clean map
    ax.set_axis_off()

    # Save the image
    plt.tight_layout(pad=0)
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close()