#for num in  range (531, 751, 2):
 #   print (num)

# seguindo a msm logica do anterior, escolhemos um range de numeros e depois da segunda virgula, determinei a quantidade de casas que deve saltar
# a partir do primeiro numero, sendo o primeiro numero impar, o proximo a aparecer tb será. 

num = 531

while num <= 750:
    if num % 2 == 1:
        print (num)
    num += 1