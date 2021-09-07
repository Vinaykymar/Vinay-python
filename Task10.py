a = int(input("Enter Starting number:"))
b = int(input("Enter Ending number:"))
def isEven(num):
     if num%2==0:
         return True
         

#print("Given number is ",isEven(n))
count = 0
for i in range(2,b+1):
    if isEven(i):
        print(i)
        count += 1
        print b ,count
     
