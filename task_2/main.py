a = list(map(int,input("Числа - ").split())) #создание списка с вводом чисел через пробел
b = [x**2 for x in a]
print (b)