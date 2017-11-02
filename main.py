import matplotlib.pyplot as plt
import numpy as np


def val(f, x):
    new_f = f.replace('x', str(x))
    return eval(new_f)


def add_to_plot(x, y, color):
    plt.plot(x, y, color=color)


def paint():
    plt.xlabel('y')
    plt.ylabel('x')
    plt.grid(True)
    plt.show()


count = 1000


def inter(f, L, R, color):
    points = 4
    pow = 4
    x = []
    y = []
    for i in range(points + 1):
        x.append(L + (float)(R - L) / points * i)
        y.append(val(f, x[i]))
        print(x[i],y[i])

    a = []
    b = []
    for i in range(pow):
        a.append([])

    for i in range(0, pow):
        r = 0
        for j in range(0, points+1):
            r = r + y[j] * (x[j] ** i)
        b.append(r)

        for j in range(0, pow):
            r = 0
            for g in range(0, points+1):
                r = r + x[g] ** (i + j)

            a[i].append(r)

    res = np.linalg.solve(a, b)

    for i in range(pow):
       # for j in range(points+1):
        print(" ".join(map(str, a[i])))
    print(x)

    pol = np.poly1d(res[::-1])
    print(pol.coefficients)
    x = []
    y = []

    for i in range(count):
        s = L + (float)(i) * (R - L) / count
        x.append(s);
        y.append(pol(x[i]))

    print(x)
    add_to_plot(x, y, color)


def add(f, color,a,b,h):
    #l = 0
    #r = 10
    #inter(f, l, r, color2)
    tx = []
    ty = []
    while a<b:
        x = a + h/2
        y = val(f, x)
        tx.append(x)
        ty.append(y)
        a+=h
    add_to_plot(tx, ty, color)


def read():
    f = input('f(x):')
    add(f, 'red')

f = "0"
def gen_square_met(a,b,h):
    global  f
    #f = "x * np.sin(x) - 3/(x+1)"
    #f = "x**x"
    #f = "x*np.sin(x)+ 4/(x+1)"
    f = "1*np.sin(x)"
    add(f, "red",a,b,h)


# read()

h = 0.01
a = -10
b = 10

gen_square_met(a,b,h)
def squar(a,b,h):
    b = b * 1.
    integral = 0
    while a<b:
        q = a+h
        integral+= val(f,(a+q)/2)*h
        a = q
    return integral

def trapetia(a,b,h):
    b = b * 1.
    integral = 0
    while a < b:
        q = a + h
        integral += (val(f,a)+val(f,q)) / 2 * h
        a = q
    return integral

def Simson(a,b,h):
    b = b * 1.
    integral = 0
    x = [a]
    y = [0]
    while a < b:
        q = a + h
        integral += (val(f,a) + val(f,q) + 4*val(f,(a+q)/2)) / 6 * h
        a = q
        x.append(a);
        y.append(integral)

    add_to_plot(x,y,"green")
    return integral


x = squar(a,b,h)
y = trapetia(a,b,h)
z = Simson(a,b,h)
print("squars  ",x)
print("trapet  ",y)
print("Simpson ",z)
#'\n',y,'\n',z)
paint()