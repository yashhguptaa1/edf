from __future__ import print_function
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from keras.layers.core import Dense, Activation, Dropout
from keras.layers.recurrent import LSTM
from keras.models import Sequential

#importing the dataset
df = pd.read_excel('UP4years.xlsx' , indexcol = 'Date and Time')


demand_data=np.array(df.iloc[0:19968,1].values,dtype=float)
date_time=pd.DatetimeIndex(df.iloc[0:19968,0])


temp_df= pd.DataFrame(demand_data,date_time)

hourly = temp_df.resample('H').max()
X_train = hourly[0:4968]
X_test = hourly[4968:4993]

hourly.plot(title='daily', color='red') 
plt.tight_layout()
plt.show()

X_test.plot(title = 'test' ,color = 'red')
plt.tight_layout()
plt.show()

training_set = X_train.iloc[:,0:1].values

from sklearn.preprocessing import Imputer
training_set = Imputer().fit_transform(training_set)

from sklearn.preprocessing import MinMaxScaler
sc = MinMaxScaler(feature_range = (0,1))
reframed = sc.fit_transform(training_set)

#timesteps
x_train = []
y_train = []
for i in range (60,4968):
    x_train.append(reframed[i-60:i,0])
    y_train.append(reframed[i,0])
x_train,y_train = np.array(x_train),np.array(y_train)

#reshape
x_train = np.reshape(x_train,(x_train.shape[0],x_train.shape[1],1))


regressor = Sequential()


regressor.add(LSTM(units = 50, return_sequences = True, input_shape = (x_train.shape[1], 1)))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units = 50, return_sequences = True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units =50))
regressor.add(Dropout(0.2))

regressor.add(Dense(units = 1))

regressor.compile(optimizer = 'adam', loss = 'mean_squared_error')

regressor.fit(x_train, y_train, epochs = 50, batch_size = 32)


real_stock_price = X_test.iloc[:, 0:1].values

dataset_total = pd.concat((X_train[0], X_test[0]), axis = 0)
inputs = dataset_total[len(dataset_total) - len(X_test) - 60:].values.reshape(-1,1)
from sklearn.preprocessing import Imputer
inputs = Imputer().fit_transform(inputs)
inputs = sc.transform(inputs)
new_test = []
for i in range(60,84):
    new_test.append(inputs[i-60:i, 0])
new_test = np.array(new_test)
new_test = np.reshape(new_test, (new_test.shape[0], new_test.shape[1], 1))
predicted = regressor.predict(new_test)
predicted = sc.inverse_transform(predicted)

plt.plot(real_stock_price, color = 'red', label = 'Demand_time')
plt.plot(predicted, color = 'blue', label =  'Predicted demand')
plt.title('DMD' + '0.031= MSE')
plt.xlabel('Time')
plt.ylabel('Demand')
plt.tight_layout()
plt.show()