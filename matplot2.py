# b. Plot multiple lines on the same chart to compare the sales of different products over time.

from matplotlib import pyplot as plt

months = ['jan','feb','mar','apr','may','jun','jul','aug','sep','oct','nov','dec']
sales_product1 = [15000, 18000, 22000, 24000, 21000, 19000, 23000, 25000, 28000, 30000, 32000, 35000]
sales_product2 = [20000, 21000, 19000, 24000, 23000, 25000, 22000, 26000, 28000, 29000, 31000, 33000]
sales_product3 = [18000, 19000, 21000, 22000, 24000, 25000, 23000, 27000, 29000, 31000, 33000, 36000]

plt.plot(months, sales_product1, marker='o', linestyle='-', color='b', label='Product 1')
plt.plot(months, sales_product2, marker='o', linestyle='-', color='r', label='Product 2')
plt.plot(months, sales_product3, marker='o', linestyle='-', color='g', label='Product 3')

plt.title('Monthly sales Comparison')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.grid(True)
plt.legend()

plt.show()