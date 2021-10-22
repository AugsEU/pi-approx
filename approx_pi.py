import math

a = 0.5
b = 1.0

for i in range(15):
    a = 0.5*(math.sqrt(1+a)-math.sqrt(1-a))
    b = (math.sqrt(b*b+1)-1)/b
    pi_a = 2**(i+2) * 3 * a
    pi_b = 2**(i+3) * b
    print("=====")
    print("Lower: " + str(pi_a))
    print("Upper: " + str(pi_b))
    print("Real: " + str(math.pi))