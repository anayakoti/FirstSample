#In this program it will tell How many vowels are there in total
userInput="";
print("Enter the name to calculate the number of volwels you wanted to know :");
UserInput=input();
count=0;
for i in UserInput:
    if(i=='a' or i=='e' or i=='o' or i=='u'):
        count=count+1;

print("The number of vowels entered in your name are:\n" +str(count));

#Vowels are printed in a unique way. If there are two 'a's it doesnt count
        
