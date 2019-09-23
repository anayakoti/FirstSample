#In this program we will set a an event while series are numbers are entered until an event is pressed, The loops stops.
average=0.0;
total=0;
count=0;
print("Enter a grade (-1 will quit) :");
grade=int(input());
while(grade!=-1):
    total=total+grade;
    count=count+1;
    print("Enter a grade(-1 will quit):");
    grade=int(input());
    average=total/count;
print("Average grade:" +str(average));
