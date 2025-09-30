import math

def area_circulo(radio):
    area=math.pi*radio*radio
    print(area) 

ans=int(input("ingrese el área del circulo "))
area_circulo(ans)