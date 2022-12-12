# Big O notation
import time

nemo = ['nemo']
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill',
            'bloat', 'nigel', 'squirt', 'darla', 'hank']


def findNemo(array):
    for i in range(len(array)):
        if array[i] == 'nemo':
            print('FOUND NEMO !')


findNemo(everyone)
