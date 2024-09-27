import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import numpy as np

def create_discrete_colormap(colormap: str = 'viridis', steps: int = 11, under: str = None, over: str = None, bad: str = None) -> mcolors.ListedColormap:
    """
    Creates a discrete colormap with optional under, over, and bad colors.

    Args:
        colormap (str): The name of a valid Matplotlib colormap. Defaults to 'viridis'.
        steps (int): The number of discrete colors in the new colormap.
        under (str, optional): Color for values below the colormap range.
        over (str, optional): Color for values above the colormap range.
        bad (str, optional): Color for invalid values.

    Returns:
        matplotlib.colors.ListedColormap: The created discrete colormap.
    """

    cmap = plt.get_cmap(colormap)
    colors = [cmap(i) for i in np.linspace(0, 1, steps)]
    cmap = mcolors.ListedColormap(colors)

    if under is not None:
        cmap.set_under(under)
    if over is not None:
        cmap.set_over(over)
    if bad is not None:
        cmap.set_bad(bad)
    return cmap
