# Exception handling

#try block: code that may raise an exception
#except block: code that runs if an exception occurs
#else block: code that runs if no exception occurs
#finally block: code that runs regardless of whether an exception occurred or not
try: 
   a = 10/0 # division by zero error
   print(a)
except Exception as e: 
    print("Error: ", e)
else:
    print("No exception occurred")
finally:
    print("This will always execute")