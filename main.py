import pandas as pd
import matplotlib.pyplot as plt


# Read your data from file
file = "data.csv"
df = pd.read_csv(file, sep=",", header=None, names=['Chrome', 'Explorer', 'Firefox'])

# Plot line series of data
# Get a list of numbers from 1 to 10
x = range(1, 11)
# Because plotting takes list arguments 
y = df['Chrome'].tolist() 
plt.plot(x, y)
plt.xlabel('measurements')
plt.ylabel('load time ms')
plt.title('Chrome load-time raw data')
plt.grid(True)


plt.show()
