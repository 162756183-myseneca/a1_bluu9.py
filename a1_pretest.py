Please enter your email user id:
== Preliminary A1 Test Run Report for bluu9==
The following is your preliminary test run report for assignment 1. Please review the report and fix all the errors identified before submitting your algorithm, python script, and test report to blackboard using the assignment 1 submission link which will be available on Monday, October 16 2020.

========================================
Test run command 1 : python3 a1_bluu9.py 2020-10-10
--test failed--
---- expect: Oct 10, 2020
----  given: Sanitized user data: 20201010
Your date of birth is: Oct 10, 2020
Test run command 2 : python3 a1_bluu9.py 2020-10-09
--test failed--
---- expect: Oct 9, 2020
----  given: Sanitized user data: 20201009
Your date of birth is: Oct 9, 2020
Test run command 3 : python3 a1_bluu9.py 2020-06-30
--test failed--
---- expect: Jun 30, 2020
----  given: Sanitized user data: 20200630
Your date of birth is: Jun 30, 2020
Test run command 4 : python3 a1_bluu9.py 20201010
--test failed--
---- expect: Oct 10, 2020
----  given: 
Test run command 5 : python3 a1_bluu9.py 2020/10/10
--test failed--
---- expect: Oct 10, 2020
----  given: Sanitized user data: 20201010
Your date of birth is: Oct 10, 2020
Test run command 6 : python3 a1_bluu9.py 2020.02.29
--test failed--
---- expect: Feb 29, 2020
----  given: Sanitized user data: 20200229
Your date of birth is: Feb 29, 2020
Test run command 7 : python3 a1_bluu9.py 2019.02.29
--test failed--
---- expect: Error 03: wrong day entered
----  given: Sanitized user data: 20190229
Your date of birth is: Feb 29, 2019
Test run command 8 : python3 a1_bluu9.py 2019.13.12
--test failed--
---- expect: Error 02: wrong month entered
----  given: Sanitized user data: 20191312
Test run command 9 : python3 a1_bluu9.py 2019.06.31
--test failed--
---- expect: Error 03: wrong day entered
----  given: Sanitized user data: 20190631
Your date of birth is: Jun 31, 2019
Test run command 10 : python3 a1_bluu9.py 201802
--test failed--
---- expect: Error 09: wrong date entered
----  given: 
Test run command 11 : python3 a1_bluu9.py 18981225
--test failed--
---- expect: Error 10: year out of range, must be 1900 or later
----  given: 
Test run command 12 : python3 a1_bluu9.py 19981299
--test failed--
---- expect: Error 03: wrong day entered
----  given: 
Test run command 13 : python3 a1_bluu9.py 189802
--test failed--
---- expect: Error 09: wrong date entered
----  given: 
Test run command 14 : python3 a1_bluu9.py 20201010 2020/10/10
--test failed--
---- expect: Usage: a1_bluu9.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD
----  given: None
Test run command 15 : python3 a1_bluu9.py 
--test failed--
---- expect: Usage: a1_bluu9.py YYYYMMDD|YYYY/MM/DD|YYYY-MM-DD|YYYY.MM.DD
----  given: None
Test Results: {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0, 10: 0, 11: 0, 12: 0, 13: 0, 14: 0, 15: 0}
Total test run marks:  0.0
Total marks for script (max. 30): 0.0
