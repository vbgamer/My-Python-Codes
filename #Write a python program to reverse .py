#Write a python program to reverse a number using a while loop.
num=int(input("Provide a number: "))
rev=0
while(num>0):
  rem=num%10
  rev=rev*10 +rem
  num//=10
print("Reverse= ",rev)