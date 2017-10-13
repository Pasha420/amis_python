count = int(input('Please enter a number of minutes: '+"\n"))  #вводимо значення
while count>1400: #цикл 
	 count = count - 1440
hours = count//60 #рахуємо кількість годин
minutes = count%60 #рахуємо кількість хвилин
print("time is",hours,":",minutes) #виводимо значення
input()