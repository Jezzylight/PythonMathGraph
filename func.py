#%matplotlib inline

func = '1 s-similar'

def s_similar(x,a,b):
    if x <= a:
        return 0
    elif a <= x <= ((a + b) / 2):
        return (2 * ((x - a) ** 2)) / ((b - a) ** 2))
    elif (a + b) / 2 <= x <= b:
        return 1 - (2 * ((x - a) ** 2)) / ((b - a) ** 2))
    else:
        return 1
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(s_similar(i,5,15))
    i += 0.1
plt.plot(x,y)
plt.grid(True)



func = '2 pi-similar'


def pi_similar(x,a,b,c):
    if x < b:
        return s_similar(x, a, b)
    if b <= x <= c:
        return 1
    if x > c:
        return 1 - s_similar(x, c, c + b - a)

import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(pi_similar(i,5,10,15))
    i += 0.1
plt.plot(x,y)
plt.grid(True)
       
 func = '3 triangle'


def triangle(x,a,b,c):
    if x <= a:
        return 0
    if a < x <= c:
        return (x - c) / (c - a)
    if c < x <= b:
        return (b - x) / (b - c)
    if x >= b:
        return 0
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(triangle(i,5,10,15))
    i += 0.1
plt.plot(x,y)
plt.grid(True)

func = '4 trapeze '

def trapeze(x,a,b,c,d):
    if x <= a:
        return 0
    if a < x < c:
        return (x - a) / (c - a)
    if c <= x <= d:
        return 1
    if d < x < b:
        return (b - x) / (b - d)
    if x >= b:
        return 0
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(trapeze(i,5,10,15))
    i += 0.1
plt.plot(x,y)
plt.grid(True)




func = '5 sigm'
import math

def sigm(x,a,b):
    return 1 / (1 + math.exp(-a * (x - b)))
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(sigm(i,5,10))
    i += 0.1
plt.plot(x,y)
plt.grid(True)

func = '6 z-similar'

def z_similar(x,a,b,c):
    if x <= c:
        return 1
    elif x > c:
        return 1/(1+(a*(x-c))**b)
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(z_similar(i,5,10,15))
    i += 0.1
plt.plot(x,y)
plt.grid(True)
   


func = '7 Gauss'
import math

def Gauss(x,a,b):
    return math.exp((-1) * (((x - a) ** 2) / (2*(b ** 2))))
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(Gauss(i,5,10))
    i += 0.1
plt.plot(x,y)
plt.grid(True)



func = 'bell-shaped 8'
import math

def bell_shaped(a,b,x):
    return 1 / (1 + math.fabs(((x - c) / a) ** (2 * b))
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(bell_shaped(i,5,10))
    i += 0.1
plt.plot(x,y)
plt.grid(True)


func = '9 diff-sigm'
import math

def diff_sigm(x,a1,b1,a2,b2):
    return (1 / (1 + math.exp(-a1 * (x - b1))))-(1 / (1 + math.exp(-a2 * (x - b2))))
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(diff_sigm(i,5,10,8,12))
    i += 0.1
plt.plot(x,y)
plt.grid(True)


func = '10 bilatetal-Gauss'
import math


if c1<c2:
    def bilatetal_Gauss(x,a1,c1,a2,c2):
     if x < c1:
        return math.exp((x-c1)**2)/((-2*a1)**2)
    elif c1 <= x <= c2:
        return 1
    elif if x > c2:
        return math.exp((x-c2)**2)/((-2*a2)**2)
elif c1>c2:
    def bilatetal_Gauss(x,a1,c1,a2,c2):
     if x < c2:
        return math.exp((x-c1)**2)/((-2*a1)**2)
    elif c2 <= x <= c1:
        return (math.exp((x-c1)**2)/((-2*a1)**2))*(math.exp((x-c2)**2)/((-2*a2)**2))
    elif if x > c1:
        return math.exp((x-c2)**2)/((-2*a2)**2)
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(bilatetal_Gauss(i,5,10,8,12))
    i += 0.1
plt.plot(x,y)
plt.grid(True)


func = '11 comp-sigm'
import math

def comp_sigm(x,a1,b1,a2,b2):
    return (1 / (1 + math.exp(-a1 * (x - b1))))*(1 / (1 + math.exp(-a2 * (x - b2))))
import matplotlib.pyplot as plt
import numpy as np
x=[]
y=[]
i = 0
while i < 50:
    x.append(i)
    y.append(comp_sigm(i,5,10,8,12))
    i += 0.1
plt.plot(x,y)
plt.grid(True)
