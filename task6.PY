from math import ceil  #імпортуємо ceil із math
count1 = int(input('Please enter a number of students in 1 group: '+"\n")) #вводимо значення
count2 = int(input('Please enter a number of students in 2 group: '+"\n")) #вводимо значення
count3 = int(input('Please enter a number of students in 3 group: '+"\n")) #вводимо значення
result = ceil(count1/2)+ceil(count2/2)+ceil(count3/2) #обчислюємо результат
print(result ,"- number of tables") #виводимо результат
input()


