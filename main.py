import math as m


def pitagoras(x,y):
    xmax= m.sqrt(x*2+y*2)
    return round(xmax,2)

def angulobase(pit,y):
    ab=m.asin(y/pit)
    return ab

def angulocompas(pit):
    for i in range (45,91):
        compa=round((5.3**2*m.sin(2*m.radians(i)))/9.8,2)
        print(f"{i}° = {compa} m")



def main():

    #primero hay que pedir los datos de "x" y "y"
    num1=float(input('Ingrese el valor en x en cm: '))
    num2=float(input('Ingrese el valor en y en cm: '))
    x=num1/100
    y=num2/100
    pit=pitagoras(x,y)
    print(f"el objetivo esta a: {pit} metros, el angulo de la base es de {angulobase(pit,y)}")
    print(f'y el angulo de elevacion sera el mas cercano a la distancia que este el objetivo entre los siguientes:')
    {angulocompas(pit)}

if __name__ == "__main__":
    main()