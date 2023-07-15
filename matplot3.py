#a. Create a bar chart using matplotlib to display the population of different cities in a country.

from matplotlib import pyplot as plt

cities = ['Pune', 'Tokyo', 'New York', 'Moscow', 'London']
populations = [4000000, 38000000, 8800000, 12600000, 9000000]

plt.bar(cities, populations)

plt.xlabel('Cities')
plt.ylabel('Population')
plt.title('Population of Cities in a Country')

plt.show()