import matplotlib.pyplot as plt
import pandas as pd

csv = pd.read_csv(r".\climate.csv", index_col=0)

year_values = csv['Year']
co2_values = csv['CO2']
temp_values = csv['Temperature']

plt.subplot(2, 1, 1)
plt.plot(years, co2, 'b--')
plt.title("Climate Data")
plt.ylabel("[CO2]")
plt.xlabel("Year (decade)")

plt.subplot(2, 1, 2)
plt.plot(years, temp, 'r*-')
plt.ylabel("Temp (C)")
plt.xlabel("Year (decade)")
plt.show()
plt.savefig("co2_temp_2.png")

