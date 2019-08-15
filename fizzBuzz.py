
def fizzBuzz(n):
    for i in range(1,n+1):
        message = ""
        if i%3 ==0 and i%5 == 0:
            message = "Fizz Buzz"        
        elif i%3 == 0:
            message = "Fizz"
        elif i%5 == 0:
            message = "Buzz"
        else:
            message = i
        print(message)


fizzBuzz(20)