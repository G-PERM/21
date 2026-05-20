import math
from decimal import Decimal, getcontext
getcontext().prec = 80000000
pi = 1/((2*Decimal(2).sqrt()/Decimal(9801))*sum(Decimal((math.factorial(4*n)*(1103+26390*n)))/Decimal(((math.factorial(n)**4)*(396**(4*n)))) for n in range(0,10000000)))
print(pi)