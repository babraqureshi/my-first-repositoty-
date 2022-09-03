Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
num1=4.5
num2=6.9
sum=num1+num2
print ('The sum of {0} and {1} is {2}.format (num1 , num2 , sum))
       
SyntaxError: unterminated string literal (detected at line 1)
print ('The sum of {0} and {1} is {2}'.format (num1 , num2 , sum))
       
The sum of 4.5 and 6.9 is 11.4
num1=1000
       
num2=2000
       
sub=num2-num1
       
print("the subtract of{0} and {1} is{2}".format(num2,num1,sub))
       
the subtract of2000 and 1000 is1000
number=100*4
       
print('the product is: ',number)
       
the product is:  400
number=300/5
       
print ('the division is : "number)
       
SyntaxError: unterminated string literal (detected at line 1)
print ('the division is : ',number)
       
the division is :  60.0
