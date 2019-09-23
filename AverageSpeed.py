#writing a program to calculate the average speed of a bolwer per over.
average=0;
total=0;
count=0;
print("Enter the speed of the bowler ( entering* will quit and calculate the average:");
Speed=int(input());
while(Speed!=-1):
 total=total+Speed;
 count=count+1;
 print("Enter the speed of the bowler ( entering* will quit and calculate the average:");
 Speed=int(input());
 average=(total/count);

print("The average speed of the bowler per over is :" +str(average));


