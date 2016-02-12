'''
Python challenge 4
'''

# Third Party Imports
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

import urllib
import re

def main():
    url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    start=44827
    start=16044/2
    start=63579
    number = str(start)
    i=0
    while i<400:
        response = urllib.urlopen(url + number)
        page = response.read()
        print page
        number = re.search(r'\d+', page).group()
        print number
        i+=1
     
    
if __name__ == '__main__':
    main()


