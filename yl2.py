r = float (input("Sisesta ringi raadius: "))
import math
s = round (math.pi * r * r, 2)
p = round (2 * math.pi * r, 2)
print ("Ringi pindala:", s)
print ("Ringi ümbermõõt:", p)