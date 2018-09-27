# -*- coding: utf-8 -*-
"""
Created on Thu Sep 27 18:12:24 2018

@author: yash
"""

import numpy as np
import skfuzzy as fuzz
import pandas as pd
import matplotlib.pyplot as plt

train1=pd.read_excel("/home/yash/Work/training/df/UP4years.xlsx","Sheet1")
print(train1)

demand_data=np.array(train1.iloc[:,1].values,dtype=float)
demand_data

index=pd.DatetimeIndex(train1.iloc[:,0])
index

cols=['Demand']
temp_df=pd.DataFrame(demand_data,index,cols)
print(temp_df)

hourly = temp_df.resample('H').max()

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[10,5])

df =hourly
ax.plot(df.index,df['Demand'])

data = df['Demand']

from pyFTS.partitioners import Grid

fs = Grid.GridPartitioner(data=data,npart=10)

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=[15,5])

fs.plot(ax)

from pyFTS.models import chen

model = chen.ConventionalFTS("Conventional FTS",partitioner=fs)
model.fit(data)
print(model)

from pyFTS.common import Util as U

U.plot_rules(model, size=[5, 5], axis=None, rules_by_axis=None, columns=1)

print(model.predict([12000]))

fig = plt.figure(figsize=(15,15))

#calling subplot so to make various plots in same axis
ax1 = fig.add_subplot(111)


forecasts = model.predict(data)
forecasts.insert(0,None)

ax1.plot(data, label="Original data")
ax1.plot(forecasts, label="Forecasts")

#legend(handles=[orig, pred])