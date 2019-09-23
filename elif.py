#Wrritign an elif program to make one decison based on a large range of Possible inputs
#Author:Anudeep Nayakoti
print("We will print the category of grade which you fall into based on your total marks");
UserInput=int(input());
if(UserInput>=500):
  print("Your grade is: 'A' ");
elif(UserInput>=450):
  print("your grade is: 'B'");
elif(UserInput>=360):
  print("Your grade is : 'C'");
elif(UserInput>270):
  print("Your grade is : 'D' ");
elif(UserInput<270):
  print("Your grade is : 'F' ");
else:
  print("You have entered a value that's beyond the standards of grading");
#**************************End of the Program****************