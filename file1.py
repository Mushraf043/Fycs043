Python 3.11.4 (tags/v3.11.4:d2340ef, Jun  7 2023, 05:45:37) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> #addition of two numbers
>>> a=int(input("Enter First Number"))
Enter First Number
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    a=int(input("Enter First Number"))
ValueError: invalid literal for int() with base 10: ''
>>> KeyboardInterrupt
>>> a
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    a
NameError: name 'a' is not defined
>>> 
>>> a=10
>>> b=20
>>> print(a+b)
30
>>> if a>20:
...     print("Greater")
... else:
...     print("Error")
