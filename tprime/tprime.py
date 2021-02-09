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
    
    # calculate the mean for each sample
    mean1 = np.mean(s1)
    mean2 = np.mean(s2)

    # output the means
    print("MEAN for Sample 1: ", mean1)
    print("MEAN for Sample 2: ", mean2)
    
    # find the standard deviation for each sample
    sdev1 = np.std(s1)
    sdev2 = np.std(s2)

    # print the standard deviations
    print("STANDARD DEVIATION for Sample 1: ", sdev1)
    print("STANDARD DEVIATION for Sample 2: ", sdev2)
    
    # calculate the standard uncertainty for each sample
    sunc1 = sdev1 / np.sqrt(count1)
    sunc2 = sdev2 / np.sqrt(count2)

    # output the standard uncertainty for each sample
    print("STANDARD UNCERTAINTY for Sample 1: ", sunc1)
    print("STANDARD UNCERTAINTY for Sample 2: ", sunc2)

    