#!/usr/bin/env python
# -*- coding: utf-8 -*-
# the above line is to avoid 'SyntaxError: Non-UTF-8 code starting with' error

'''
Created on 
Course work: 
@author: raja
Source:
    https://pugsql.org/
'''

# Import necessary modules
import pugsql


def startpy():
    
    # Create a module of database functions from a set of sql files on disk.
    queries = pugsql.module('resources/sql')

    # Point the module at your database.
    queries.connect('sqlite:///test.db')

    # Invoke parameterized queries, receive dicts!
    city = queries.get_city(name='Theni')

    print(city)

    # -> { 'user_id': 42, 'username': 'mcfunley' }


if __name__ == '__main__':
    startpy()