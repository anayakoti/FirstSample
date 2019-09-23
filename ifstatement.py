#writing a program to take two user inputs and run a script
print("Enter the number of hours you worked in this week");
UserInput=int(input());
Hourlyrate=25;

if(UserInput <=40):
  RegularTotalPay=0;
  RegularTotalPay=(UserInput*Hourlyrate);
  print(RegularTotalPay);
if(UserInput>40):
  OverTimePay=(Hourlyrate*1.5)*UserInput;
  print("Your total overtimepay is:" + " "+ str(OverTimePay));

