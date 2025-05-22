# graph_config.py
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.dates as mdates

# Color and Style
plt.style.use('ggplot')
custom_colors = ['#071d33', '#63adf2', '#a7cced', '#82a0bc', '#2f4b26']
plt.rcParams['axes.prop_cycle'] = plt.cycler(color=custom_colors)
sns.set_palette(custom_colors)

# Figure & Font
plt.rcParams.update({
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'font.family': ['Helvetica', 'Arial', 'sans-serif'],
    'font.size': 13,
    'text.antialiased': True,
})

# Axes & Grid
plt.rcParams.update({
    'axes.edgecolor': 'black',
    'axes.labelcolor': 'black',
    'axes.labelpad': 10,
    'axes.titleweight': 'bold',
    'axes.titlesize': 14,
    'axes.titlepad': 15,
    'grid.color': '#E5E5E5',
    'grid.linestyle': '--',
    'grid.linewidth': 0.6,
    'grid.alpha': 0.3,
})

# Ticks
plt.rcParams.update({
    'xtick.color': 'black',
    'ytick.color': 'black',
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'xtick.major.size': 5,
    'ytick.major.size': 5,
    'xtick.major.width': 1,
    'ytick.major.width': 1,
})

# Legends
plt.rcParams.update({
    'legend.frameon': True,
    'legend.facecolor': 'white',
    'legend.framealpha': 0.95,
    'legend.edgecolor': '#CCCCCC',
    'legend.loc': 'upper right',
    'legend.borderaxespad': 0.5,
    'legend.labelspacing': 0.4,
    'legend.handlelength': 2.0,
    'legend.handletextpad': 0.5,
})

# Lines
plt.rcParams['lines.linewidth'] = 2



def set_spines(ax, top=True, right=True, left=True, bottom=True):
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)

