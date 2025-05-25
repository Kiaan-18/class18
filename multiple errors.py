try:
   num1=int(input("Enter a number:"))
   num2=int(input("Enter a second number:"))
   result=num1/num2
   print("Result is ",result)
   print("Result is ",result1)
except ZeroDivisionError:
   print("Division by zero is not allowed")
except ValueError:
   print("please enter a numerical value")
except NameError as ex:
   print("The exception happened",ex)
except:
   print("Some error occurred")
finally:
   print("I will execute no matter what happens")