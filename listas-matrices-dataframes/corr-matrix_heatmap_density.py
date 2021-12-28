# -*- coding: utf-8 -*-
"""
Plotting a correlation matrix with heatmap and density

Created on Tue Dec 28 13:23:33 2021

@author: Erick F.
"""
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import numpy as np

# read dataset
df = pd.read_csv('cereal.csv')# get correlations
df_corr = df.corr()# irrelevant fields
fields = ['rating', 'shelf', 'cups', 'weight']# drop rows
df_corr.drop(fields, inplace=True)# drop cols
df_corr.drop(fields, axis=1, inplace=True)
print(df_corr)

fig, ax = plt.subplots(figsize=(10, 8))# mask
mask = np.triu(np.ones_like(df_corr, dtype=np.bool))# adjust mask and df
mask = mask[1:, :-1]
corr = df_corr.iloc[1:,:-1].copy()# plot heatmap
sb.heatmap(corr, mask=mask, annot=True, fmt=".2f", cmap='Blues',
           vmin=-1, vmax=1, cbar_kws={"shrink": .8})# yticks
plt.yticks(rotation=0)
plt.show()

fig, ax = plt.subplots(1, figsize=(12,8))
sb.kdeplot(df.potass, df.fiber, cmap='Blues',shade=True, shade_lowest=False, clip=(-1,300))
plt.scatter(df.potass, df.fiber, color='orangered')





