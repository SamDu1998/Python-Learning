#!/usr/bin/env python3
# -*- coding: utf-8 -*-

'a test module'

__author__='Sam Du'

import sys

def test():
    args = sys.argv
    if len(args)==1:
        print('Hello World!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too manny arguments!')

if __name__=='__main__':
    test()



def _private_1(name):
    return 'Hello, %s' % name

def _private_2(name):
    return 'Hi, %s' % name

def greeting(name):
    if len(name) > 3:
        return _private_1(name)
    else:
        return _private_2(name)

print(greeting('Sam Du'))