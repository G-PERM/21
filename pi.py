import math
from decimal import Decimal, getcontext
k = int(input("k = "))
getcontext().prec = 14*k
pi = Decimal(1)/((Decimal(10005).sqrt()/Decimal(4270934400))*sum(Decimal((math.factorial(6*n)*(13591409+545140134*n)))/Decimal(((math.factorial(3*n))*(math.factorial(n)**3)*((-1)**n)*(640320**(3*n)))) for n in range(0,k)))
print(pi)