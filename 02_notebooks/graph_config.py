# graph_config.py
import matplotlib.pyplot as plt
import seaborn as sns

plt.style.use('ggplot')

plt.rcParams.update({
    'figure.facecolor': 'white',
    'axes.facecolor': 'white',
    'font.family': 'Helvetica',
    'font.size': 13,
    'axes.edgecolor': 'black',
    'axes.labelcolor': 'black',
    'axes.titleweight': 'bold',
    'axes.titlesize': 14,
    'grid.color': '#E5E5E5',
    'grid.linestyle': '--',
    'grid.linewidth': 0.6,
    'xtick.color': 'black',
    'ytick.color': 'black',
    'xtick.direction': 'out',
    'ytick.direction': 'out',
    'legend.frameon': True,
    'legend.facecolor': 'white',
    'legend.framealpha': 0.95,
    'legend.edgecolor': '#CCCCCC',
    'legend.loc': 'upper right',
    'lines.linewidth': 2,
    'axes.prop_cycle': plt.cycler(color=[
        '#071D33',  # White men
        '#32A1D2',  # Men of color
        '#A2D6F9',  # Women of color
        '#4D5863',  # White women
    ])
})

def set_spines(ax, top=True, right=True, left=True, bottom=True):
    ax.spines['top'].set_visible(top)
    ax.spines['right'].set_visible(right)
    ax.spines['left'].set_visible(left)
    ax.spines['bottom'].set_visible(bottom)
