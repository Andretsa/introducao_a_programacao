#Faça um programa que mostre as tabuadas dos números de 1 a 10.

#percorre o numeros de 1 a 10, multiplicando-os por valores de 1 a 10.
for tabuada in range(1, 11):
    for count in range(10):
        print("%d x %d = %d" % (tabuada, count + 1, tabuada * (count+1)))
