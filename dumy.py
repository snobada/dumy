import random
number=random.randint(1,100)
diff=random.randint(1,25)


n=int(input("Guess the number:"))
count=7
hint_given=False
while count!=0:
    count-=1
    temp=count
    print("Attempts left",count)
   
    n=int(input("Guess the number:"))
    if not hint_given:
     if number<50:
        print("///Hint:the number is lower than 50///")
     else:
        print("Hint:the number is greater than 50")
        hint_given=True
    if count==1:
       break    

if n==number:
 print("///Your guess is correct,you beat the computer")
 if count==1:
   print("///You are out of attempts!///")
   print("///The number is ",number)
        
        
  



