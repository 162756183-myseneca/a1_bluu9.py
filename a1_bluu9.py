#!/usr/bin/env python3
''' 
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
	
	
    


def leap_year(obj):
	leap = int(obj[0:4])
	if(leap%400 == 0) : 
		return True 
	elif(leap%100 == 0) : 
		return False 
	elif(leap%4 == 0) : 
		return True 
	else : 
		return False 

    

def sanitize(obj1,obj2):
    '''
    put your function level docstring here ...
    '''
    ...
    
	return results

def size_check(obj):
 
	month_int = obj[4:6]
	day_int= obj[6:] 
	month_check = 0 
	
	if month_int in '01,03,05,07,08,10,12' 
		month_check = 31 
		


	elif month_int in '02' : 
		month_check=28
	
	else : 
		month_check = 30 
	

	if day_int > month_check : 
		status = False 
	
	else 
		status = True 	


	return status

def range_check(obj1, obj2):
	obj1_int = int(obj1) 
		
	if obj_int < obj2[0] : 
		status = False 
	else 
		status = True 

	return status
    
def usage():    
	' Please type your date of birth in YYYYMMDD into the command line ' 
	 
	return status

if __name__ == "__main__":
   # step 1
   if len(sys.argv) != 2:
      print(usage())
      sys.exit()
   # step 2
   month_name = ['Jan','Feb','Mar','Apr','May','Jun',
                 'Jul','Aug','Sep','Oct','Nov','Dec']
   days_in_month = {1:31, 2:28, 3:31, 4:30, 5:31, 6:30,
                    7:31, 8:31, 9:30, 10:31, 11:30, 12:31}
   user_raw_data = sys.argv[1]
   # step 3
   allow_chars = '0123456789'
   dob = sanitize(user_raw_data, allow_chars)
   print('Sanitized user data:', dob)
   # setp 4
   result = size_check(dob)
   if result == False:
       print("Error 09: wrong data entered")
       sys.exit()
   # step 5
   year = int(dob[0:4])
   month = int(dob[4:6])
   day = int(dob[6:])
   # step 6
   result = range_check(year,(1900,9999))
   if result == False:
       print("Error 10: year out of range, must be 1900 or later")
       sys.exit()
   result = range_check(month,(1,12))
   if result == False:
       print("Error 02: Wrong month entered")
       sys.exit()
   result = leap_year(year)
   if result == True:
       days_in_month[2] = 29
   result = range_check(day, (1, days_in_month[month]))
   if result == False:
       print("Error 03: wrong day entered")
       sys.exit()
   # step 7
   new_dob = str(month_name[month - 1])+' '+ str(day)+', '+str(year)
   # step 8
   print("Your date of birth is:", new_dob)  
