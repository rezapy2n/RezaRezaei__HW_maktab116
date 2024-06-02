n = int (input (" number:"))
sum = 0
for i in range(1,n) :
   if n % i == 0 :
      sum+=i
if sum == n :
     print("YES", n, "is ok")
    else :
     print("NO", n, " is not ok")
     
     