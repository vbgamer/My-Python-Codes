#Write a python program finding the factorial of a given number using while loop.

num=int(input("Provide a number: "))
i=num
ans=1
while (i>=1):
  ans=ans*i
  i=i-1
print(ans)