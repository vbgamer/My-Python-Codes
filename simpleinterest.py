#WAP to calculate simple interest.(Assuming rate of interest =7.5)
def simpint(p,r,t):
  ans=(p*r*t)/100
  print("Simple interest for given amount is= ",ans)
  print("The amount you will recieve after",t,"years is ",p+ans)

print("Simple interest")
p=int(input("Enter value for principle: "))
r=float(input("Enter value for rate of interest: "))
t=int(input("Enter value for time in years: "))

simpint(p,r,t)

