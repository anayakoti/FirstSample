#Lets write a program to create a for loop to loop through the data

utha=0;
count=0;
for line in open('randomnumbers.txt'):
    print(line);
    line=int(line);
    utha=(line+utha);
    count=count+1;
    average=utha/count;
print( "The average of numbers is :" +str(average) + " "+ "by dividing :" +str(utha)+ " " +"by " +str(count));
