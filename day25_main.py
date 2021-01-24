# Import libraries
# import numpy as np

# Define path
data1 = 6270530
data2 = 14540258
# data_1 = 5764801
# data_2 = 17807724
# data = "463528179"

# Auxiliary variables
prime = 20201227

# Data to list
num = 1
loop2 = 0
while num % prime != data1:
    num = (num * 7) % prime
    loop2 += 1
num = 1
loop1 = 0
while num % prime != data2:
    num = (num * 7) % prime
    loop1 += 1

# Obtain encryption key
ran = (loop1 * loop2) % (prime - 1)
num = 1

# Use one of the congruences
if loop1 < loop2:
    loop = loop1
    data = data2
else:
    loop = loop2
    data = data1

# Apply the congruence with the smaller loop
while ran > loop:
    ran -= loop
    num = num * data % prime

# Apply the remaining range
for i in range(ran):
    num = (num * 7) % prime

print("Encrytpion key:" + str(num))
