#In this program we are writing a program to guess the name within three tries
tries=0;
answer="anudeep";
while(tries<=3):
#since the tries is '0' and is less than or equal to 3, it will enter the loop
 print("what is the name?");
 response=input();
 tries=tries+1;
 if(response=="anudeep"):
    print("Your guess is right");
    break;
 elif(tries==3):
    print("Your out of luck and the answer is: anudeep");
    break;
else:
    print("Better luck next time");
    
