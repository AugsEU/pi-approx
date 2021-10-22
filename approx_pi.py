import math

a = 0.5
b = 1.0

for i in range(10):
    a = 0.5*(math.sqrt(1+a)-math.sqrt(1-a))
    b = (math.sqrt(b*b+1)-1)/b
    pi_a = 2**(i+2) * 3 * a
    pi_b = 2**(i+3) * b
    print("=====")
    print((pi_a/math.pi)-1)
    print((pi_b/math.pi)-1)
    print(0.5*(pi_b+pi_a)/math.pi -1)
    print(math.pi)