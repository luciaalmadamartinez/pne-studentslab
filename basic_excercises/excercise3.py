temperatures = [15.5, 17.2, 14.8, 16.0, 18.3, 20.1, 19.5]

#Get maximum temperature:
max_temp = temperatures[0]
for temperature in temperatures:
    if temperature > max_temp:
        max_temp = temperature
#Get minimum temperature:
min_temp = temperatures[0]
for temperature in temperatures:
    if temperature < min_temp:
        min_temp = temperature
#calculate average temperature:
total_number = 0
for temperature in temperatures:
    total_number += temperature
average = total_number / len(temperatures)
#Number of days above 17 degrees:
degrees = 17
days_above_17 = 0
for temperature in temperatures:
    if temperature > degrees:
        days_above_17 += 1


print("Temperature on wednesday:", temperatures[2])
print("The maximum temperature is:", max_temp)
print("The minimum temperature is:", min_temp)
print("The average temperature is:", round(average, 1))
print("Days above 17:", days_above_17)
print("The list sorted from lowest to highest is:", sorted(temperatures))