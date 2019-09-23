#Calculating the average and when the user enters -1 it will break the loop
number=0;
total=0;
average=0;
count=0;
while True:
    print("Enter the number");
    number=float(input());
    if(number==-1):
        break;
    
    total=total+number;
    number=number+1;
    count=count+1;
    average=total/count;
print("The average of the entered numbers is:" +str(average));
