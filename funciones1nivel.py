def normal(x):
    return x

def cuadrado(x):
    return x*x

def cubo(x):
    return x**3

def sumaTodos(limitTo, f):
    resultado = 0
    for i in range(0, limitTo+1):
        resultado += f(i)
        
    return resultado


if __name__ == '__main__':
    print(sumaTodos(100, normal))
    print(sumaTodos(3, cuadrado))
