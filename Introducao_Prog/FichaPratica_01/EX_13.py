hora = int(input ("Informe as horas no formato 24h: "))
min = int(input ("informe os minutos: "))

if hora == 13:
    hora = 1 

elif hora == 14:
    hora = 2

elif hora == 15:
    hora = 3

elif hora == 16:
    hora = 4

elif hora == 17:
    hora = 5

elif hora == 18:
    hora = 6

elif hora == 19:
    hora = 7

elif hora == 20:
    hora = 8

elif hora == 21:
    hora = 9

elif hora == 22:
    hora = 10

elif hora == 23:
    hora = 11

print (f"hora atualizada {hora}:{min}")