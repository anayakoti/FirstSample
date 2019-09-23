#wiriting a program to take inputs as two operands and calculate based on the operation of the desired
operand1='';
operand2=0.0;
#we will assign the operation as an empty string because we don't know he users input
operation='';
while(operand1!= 'q'):
      print("Enter the first operand");
      operand1=input();
#we have written this to quit, otherwise an eeror is produced because q is string and it cannot be converted into a float.
      if(operand1=='q'):
          break;
      operand1=float(operand1);
      print("Enter the second operand that is less than the first operand");
      operand2=input();
      operand2=float(operand2);
      
#After collecting the two operands we will request the user to select the operation
      print("Please select the operation amonng these (*,+,/,-) ");
      operation=input();
      if(operation=='+'):
       print(operand1+operand2);
      elif(operation=='*'):
       print(operand1*operand2);
      elif(operation=='/'):
       print(operand1/operand2);
      elif(operation=='-'):
       print(operand1-operand2);
      else:
        print("We are unable to recognize the opearation" + "Sorry");
        
    
