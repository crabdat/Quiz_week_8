import matplotlib.pyplot as plt
import sqlite3


years = []
co2 = []
temp = []

connect = sqlite3.connect(r".\climate.db")
cursor = connect.cursor()

sql_cmd = """
SELECT years, co2, temp FROM C:/Users/Atticus/PycharmProjects/2810 quiz/Quiz_week_8/climate.db WHERE type='ClimateData';
"""
cursor.execute(sql_cmd)
res = cursor.fetchall()

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
plt.savefig("co2_temp_1.png") 
