N = int(input("Please write a count of students: ")) #студенти
K = int(input("Please write a count of apples: ")) #яблуки
count_apples =  K//N 
apples_left = K%N 
print("every student receiped", count_apples,"apples")  #виводимо результат
print("apples left:",apples_left)  #виводимо результат
input()
	
