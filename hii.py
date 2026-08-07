print("*****Traffic Signal Rule*****")
Signal=input("Enter the signal colour:")

if Signal=="red":
   print("action: stop")

elif Signal=="yellow":
    print("action: wait")

elif Signal=="green":
     print("action: Go")
    
else:
    print("Invalid Signal")
