import matplotlib.pyplot as plt

temperature=[17,20,24,30,32,35,40]
precipitation=[300,200,200,250,240,320,330]

plt.xlabel('temperature in degree centigrades')
plt.ylabel('precipitation in centimeters')

plt.scatter(temperature, precipitation)
plt.show()


plt.xlabel('temperature in degree centigrades')
plt.ylabel('precipitation in centimeters')

plt.plot(temperature,precipitation)
plt.show()