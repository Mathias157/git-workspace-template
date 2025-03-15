
import eel
import pkg_resources
import rasterio
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import pandas as pd
import numpy as np
import rioxarray as rxr

eel.browsers.set_path('chrome', '/home/mberos/.local/share/flatpak/app/org.chromium.Chromium/x86_64/stable/active/export/bin/org.chromium.Chromium')

# 1.0 Variables
legend = pd.read_csv('/home/mberos/Repos/tests/Data/CORINE/u2018_clc2018_v2020_20u1_raster100m/u2018_clc2018_v2020_20u1_raster100m/Legend/CLC2018_CLC2018_V2018_20_QGIS.txt', header=None)
legend.columns = ['Code', 'R', 'G', 'B', 'A', 'Legend']
# legend.index = np.arange(1, len(legend)+1)
cmap = ListedColormap(['#{0:02x}{1:02x}{2:02x}'.format(*(legend.loc[i, 'R'],
                        legend.loc[i, 'G'],
                        legend.loc[i, 'B']))
                       for i in legend.index])


# It was possible to load the dataset using rioxarray (also required an installation of the module dask)
# Check this link https://climag.readthedocs.io/land_cover/clc_2018.html
# There's also a tutorial on how to load the .qml legend entry

# import rioxarray as rxr
# landcover = rxr.open_rasterio('/home/mberos/Repos/tests/Data/CORINE/u2018_clc2018_v2020_20u1_raster100m/u2018_clc2018_v2\
# 020_20u1_raster100m/DATA/U2018_CLC2018_V2020_20u1.tif', chunks="auto")
# ...


# 1.1 Functions
def make_figure(x0: int, x1: int,
                y0: int, y1: int):

    # Image path
    img_path = '/home/mberos/Repos/tests/Data/CORINE/u2018_clc2018_v2020_20u1_raster100m/u2018_clc2018_v2020_20u1_raster100m/DATA/U2018_CLC2018_V2020_20u1.tif'

    # Open the file with rasterio
    with rasterio.open(img_path) as src:
        # Get metadata
        # print(f"Width: {src.width}, Height: {src.height}")
        # print(f"Number of bands: {src.count}")
        
        # For very large files, read a subset of the data
        # This reads a 1000x1000 window from the top-left corner
        window = ((x0, x1), (y0, y1))
        subset = src.read(1, window=window)
        
        # Plot the subset
        fig, ax = plt.subplots(figsize=(5, 8))
        img = ax.imshow(subset, cmap=cmap)
        
        
        vmin, vmax = img.get_clim()
        cbar = plt.colorbar(img)
        
        num_colors = len(legend) # Adjust this to match your actual number of colors
        bounds = np.linspace(vmin, vmax, num_colors + 1)
        tick_positions = bounds[:-1] + (bounds[1] - bounds[0])/2  # Center of each color band

        # Apply the custom ticks and labels to the colorbar
        cbar.set_ticks(tick_positions)
        cbar.set_ticklabels(list(legend.Legend.values))
        
        ax.axes.set_axis_off()
    
    # Save the figure to a bytes buffer
    fig.savefig('./mod/static/test.png', 
                transparent=True,
                bbox_inches='tight')
    
    return 'test.png'

def GUI():
    
    # Get working directory and package directory
    static_path = pkg_resources.resource_filename(__name__, 'static')
    
    eel.init(static_path)
    eel.expose(make_figure)
    eel.start('index.html', size=(800, 600), position=(315, 150))# mode="browser", )
    
    
if __name__ == '__main__':
  GUI()
  