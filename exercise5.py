import random
import math

# calculate 
def calculate_MD_nRE(m, n, p):
    MD_nRE = 0.0  # Initialize MD_nRE as a float for accurate division
    m = int(m)
    n = int(n)
    p = int(p)
    for _ in range(m):
        y = random.random() * m  # Generate random float between 0 and N
        y_hat = random.random() * m
        p_squared = y**(1/n) -y_hat** (1/n)
        MD_nRE += p_squared  # Accumulate the absolute errors
    MD_nRE /= m  # Divide the total error by N to get the mean
    return MD_nRE

# Input section
m = input("Please enter number of samples: ")
n = input("Please enter nth root: ")
p = input("Please enter the order of the loss function: ")

# Output results
print(f'{calculate_MD_nRE(m, n, p):.4f}')