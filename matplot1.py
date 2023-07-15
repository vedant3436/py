# a. Generate a line chart using matplotlib to visualize the monthly sales of a product over a year.

from matplotlib import pyplot as plt

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
sales = [15000,18000,22000,24000,21000,19000,23000,25000,28000,30000,32000,35000]

plt.plot(months, sales, marker='o', linestyle='-',color='b')

plt.title('Monthly sales of a product X')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)

plt.show()