# -*- coding: utf-8 -*-
"""
Created on Mon Jan 18 18:22:28 2021

@author: zackg
"""

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

population = np.random.rand(100)
Area = np.random.randint(100,600,100)
continent =['North America','Europe', 'Asia', 'Australia']*25

df = pd.DataFrame(dict(population=population, Area=Area, continent = continent))

fig, ax = plt.subplots()

colors = {'North America':'red', 'Europe':'green', 'Asia':'blue', 'Australia':'yellow'}

# Get Unique continents
color_labels = df['continent'].unique()

# List of colors in the color palettes
rgb_values = sns.color_palette("Set3", 4)

# Map continents to the colors
color_map = dict(zip(color_labels, rgb_values))

# Finally use the mapped values
rng = np.random.RandomState(0)
x = df['population']
y = df['Area']
colors = {'North America':'red', 'Europe':'green', 'Asia':'blue', 'Australia':'yellow'}

ax.set_xlabel('Date')
ax.set_ylabel('Preice (USD)')
ax.set_title("Dummy Data")

plt.style.use('dark_background')

plt.scatter(x, y, s=100*df['population'], alpha=0.3,
            c= df['continent'].map(colors),
            cmap='viridis')

plt.colorbar();
 
plt.savefig('test.png', dpi=600)
plt.show()