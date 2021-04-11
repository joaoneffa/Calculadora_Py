def soma(n1, n2):
    try:
        if type(a) == type(1) and type(b) == type(1):
            return a+b
        else:
            raise Exception
    except:
        if type(a) != type(1) or type(b) != type(1):
            print ('1º e 2º números só podem ser números inteiros.')

def sub(n1, n2):
    try:
        if type(a) == type(1) and type(b) == type(1):
            return a-b
        else:
            raise Exception
    except:
        if type(a) != type(1) or type(b) != type(1):
            print ('1º e 2º números só podem ser números inteiros.')

def mult(n1, n2):
    try:
        if type(a) == type(1) and type(b) == type(1):
            return a*b
        else:
            raise Exception
    except:
        if type(a) != type(1) or type(b) != type(1):
            print ('1º e 2º números só podem ser números inteiros.')

def div(n1, n2):
    try:
        if type(a) == type(1) and type(b) == type(1):
            try:
                return a/b
            except ZeroDivisionError:
                print ('2º número não pode ser 0!')
        else:
            raise Exception
    except:
        if type(a) != type(1) or type(b) != type(1):
            print ('1º e 2º números só podem ser números inteiros.')

def raiz(num):
    from math import sqrt
    try:
        if type(num) == type(1):
            try:
                return (sqrt(num))
            except ValueError:
                print ('O número não pode ser negativo!')
        else:
            raise Exception
    except:
        print ('Apenas números inteiros podem ser calculados.')