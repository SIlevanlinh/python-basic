# Import decimal library
from decimal import*
# Implicit 27
getcontext().prec = 30

print(10 / 3)
d = Decimal(10) / 3
print(d)
print(type(d))