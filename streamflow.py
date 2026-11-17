import matplotlib.pyplot as plt
import numpy as np

# Read the CSV file
data = np.genfromtxt('June-2021-Provo-River-Streamflow-Rates.csv', delimiter = ',', skip_header = 1, dtype = str)

# Slice the array
x = data[:, 0]
y_1 = data[:, 1].astype(float)
y_2 = data[:, 2].astype(float)
y_3 = data[:, 3].astype(float)
y_4 = data[:, 4].astype(float)
y_5 = data[:, 5].astype(float)

# Convert dates
x = x.astype('datetime64[D]')

plt.figure(figsize=(12, 6))

plt.plot(x, y_1, label = '10163000', color = 'purple')
plt.plot(x, y_2, label = '10155200', color = 'blue')
plt.plot(x, y_3, label = '10155500', color = 'green')
plt.plot(x, y_4, label = '10154200', color = 'yellow')
plt.plot(x, y_5, label = '10155000', color = 'orange')

plt.title('Provo River Streamflow Data (2021)')
plt.xlabel('Date')
plt.ylabel('Flowrate (cfs)')

plt.legend(title = 'Site Numbers')
plt.grid()
plt.tick_params(axis = 'x', rotation = 45)
plt.show()