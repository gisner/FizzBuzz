#Fizz Buzz for n numbers
import sys
<<<<<<< HEAD
n=30
=======
n=20
>>>>>>> 2d15a712f51c625e80cee0c4efe467343d7fc6a3
try:
    print("n value given: {}".format(sys.argv[1]))
    n=int(sys.argv[1])
except (IndexError,ValueError):  
    try:
        n=int(input("n is improper/non-numeric,Enter a numeric value for n: "))
    except ValueError:
        print("Again n is improper/non-numeric. Default value is taken: ",n)
for i in range(1,n+1):
    if i%15==0:
        print("fizzbuzz")
    elif i%3==0:
        print("fizz")
    elif i%5==0:
        print("buzz")
    else:
        print(i)
        
