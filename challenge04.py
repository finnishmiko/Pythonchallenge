'''
Python challenge 4
'''


import urllib.request
import re


def main():
    urlBase = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='
    start = 12345
    # start=16044/2
    # start=63579
    number = str(start)
    i = 0
    while i < 400:
        with urllib.request.urlopen(urlBase + number) as url:
            page = url.read().decode('utf-8')
            print(page)
            number = re.search(r'\d+', page).group()
            print(number)
            i += 1


if __name__ == '__main__':
    main()
