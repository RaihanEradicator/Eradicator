# Masukkan input seperti pada rumus di bawah ini
# a^2 = b^2 + c^2 - 2*b*c cos()

import math

print("------ ATURAN COSINUS ------")
b = int(input("Masukkan nilai Variable B :  "))
c = int(input("Masukkan nilai Variable c :  "))
teta = int(input("Masukkan nilai teta :   "))

if (teta == 0):
    cosTeta = 1
elif(teta == 30):
    cosTeta = 1 / 2 * math.sqrt(3)
elif (teta == 45):
    cosTeta = 1/2*math.sqrt(2)
elif (teta == 60):
    cosTeta = 0.5
elif (teta == 90):
    cosTeta = 0
else:
    print ("Maaf kami tidak menyediakan @Copyright konversi cos")

akarA = b**2 + c**2 - 2*b*c*cosTeta

print(akarA)
print(Copyright@Raihan2020)
