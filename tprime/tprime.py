# Kayla Marcantonio

import numpy as np

if __name__ == "__main__":
    count1 = int(input("Enter the number of observations in Sample 1: "))
    
    # samples
    s1 = []
    s2 = []

    # take input for sample 1
    print("Enter the data for Sample 1:")
    for x in range(count1):
        s1.append(float(input()))

    print("Sample 1: ", s1)

    count2 = int(input("Enter the number of observations in Sample 2: "))

    # take input for sample 2
    print("Enter the data for Sample 2:")
    for x in range(count2):
        s2.append(float(input()))

    print("Sample 2: ", s2)
