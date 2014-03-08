from math import *

list = ["a","b","c",1,2,3]
dict = {"name":"value1", "name2":"value2","name3":3}

def func1(x,y):
  return x+y

if __name__ == '__main__':
    dict = {'type':'biconvex',
        'angle':60,
        'outer':0.93,
        'inner':0.82
    }
    angle = dict['angle']
    outer = dict['outer']
    inner = dict['inner']
    hangle = angle/2

    # Create two circles, separated by 2*outer_sigma - biconvex_width
    biconvex_width = 2*(outer - outer*cos(hangle*pi/180))
    print "biconvex width = ", biconvex_width


