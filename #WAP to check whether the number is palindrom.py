#WAP to check whether the number is palindrom or not
num=int(input("Provide a number: "))
numm=num
rev=0
while(num>0):
  rem=num%10
  rev=rev*10 +rem
  num//=10
print("Reverse= ",rev)
if(numm==rev):
  print(numm," is a palindrome")
else:
  print(numm," is not a palindrom")