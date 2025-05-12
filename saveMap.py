import contextily as ctx
import matplotlib.pyplot as plt
from shapely.geometry import box
import geopandas as gpd
from pyproj import Transformer

def saveMap(lon, lat, filename='map.png', source=ctx.providers.OpenStreetMap.Mapnik):
    """
    Generates and saves a 1000x1000 meter map image (1m/pixel) centered on given coordinates.

    Parameters:
        lon (float): Center longitude
        lat (float): Center latitude
        filename (str): Output PNG filename
        source: Tile provider (OpenStreetMap by default)
    """
    # Convert center coordinates to EPSG:3857 (meters)
    transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
    center_x, center_y = transformer.transform(lon, lat)

    # 1km bounding box: 500m in each direction
    half_size = 500
    minx = center_x - half_size
    maxx = center_x + half_size
    miny = center_y - half_size
    maxy = center_y + half_size

    # Create bounding box GeoDataFrame
    bbox = box(minx, miny, maxx, maxy)
    gdf = gpd.GeoDataFrame({'geometry': [bbox]}, crs="EPSG:3857")

    # Create 1000x1000 pixel figure (1m/pixel at 100 DPI)
    fig, ax = plt.subplots(figsize=(10, 10), dpi=100)
    gdf.plot(ax=ax, edgecolor='none', alpha=0)

    # Add basemap
    ctx.add_basemap(ax, crs=gdf.crs, source=source, zoom=19)
    ax.set_axis_off()
    plt.tight_layout()
    plt.savefig(filename, bbox_inches='tight', pad_inches=0)
    plt.close()
    print(f"Saved map to '{filename}'")