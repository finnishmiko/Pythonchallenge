'''
Python challenge 2
'''

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#print "Pandas Version", pd.__version__


def main():
    d = {}
    
    # read text file
    with open ("challenge02.txt", "r") as myfile:
        data = myfile.read().replace('\n', '')
        print(data)
        
    # count symbols in data 
    for x in data:
        d[x] = data.count(x)

    # print the result
    for y in d:
        print (y + ': ' + str(d[y]))
        
    
if __name__ == '__main__':
    main()


