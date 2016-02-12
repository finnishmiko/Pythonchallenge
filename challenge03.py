'''
Python challenge 3
'''

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

#print "Pandas Version", pd.__version__


def main():
    d=[]
    counter=0
    
    # read text file
    with open ("challenge03.txt", "r") as myfile:
        data = myfile.read().replace('\n', '')
        print data
    #print type(data)
    # Find event
    #print data.find(data.istitle())

    prev=0
    i=0
    index=0
    result=[]
    for x in data:
        if x.isupper() == True and i<3:
            #d.append(x)
            #d.append(data[index])
            i+=1
            #print x
        elif i==4 and x.isupper() == True:
            i=3
        elif i == 3 and x.isupper() == False:
            i=5
            #d.append(x)
        elif i > 4 and x.isupper() == True:
            i+=1
            #d.append(x)
        else:
            i=0
            #d = []
        if i == 8: #and x.isupper() == False:
            #print d
            if data[index-7].isupper() == False and data[index+1].isupper() == False:
                print data[index-7:index+2]
                result+=data[index-3]
                counter+=1
            i=3
            
            #d=[]
        prev=x
        index+=1
    print "Total: ", counter
    print result
        
     
    
if __name__ == '__main__':
    main()


