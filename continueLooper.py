#writing a program that is event based and also use continue.
Denominator=0;
Numerator=0;

while(Denominator!=-1):
    print("Enter the Numerator");
    Numerator=float(input());
    print(("Enter the Denominator:"));
    Denominator=float(input());
    if(Denominator==0):
       continue;
    print(Numerator/Denominator);

