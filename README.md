# a1_bluu9.py
''' template for ops435 assignment 1 script
    put your script level docstring here...
    you can have more than one line of docstring.
    Please personlize the following author declaration:
-----------------------------------------------------------------------
OPS435 Assignment 1 - Winter 2021
Program: a1_bluu9.py (replace [Seneca_name] with your Seneca User name)
Author: Brandon luu
The python code in this file (a1_bluu9.py) is original work written by
brandon. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
'''
import os
import sys


        for slash in sys.argv[1] :
                if slash in '' :
                        dob = sys.argv[1]
                elif slash in '/' :
                        dob = sys.argv[1].replace('/', '')


                elif slash in '-' :
                        dob = sys.argv[1].replace('-', '')


                elif slash in '.' :
                        dob = sys.argv[1].replace('.', '')
