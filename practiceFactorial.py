print("Enter a number you wish to know the factorial of it");
num=int(input());
beginnerInaRange=1;
endOfaRange=0;
for multiplier in range(beginnerInaRange, num+1):
    beginnerInaRange=(multiplier*beginnerInaRange);
    
result=0;
result=beginnerInaRange;
print("The factorial is :" +str(result));

    
   
