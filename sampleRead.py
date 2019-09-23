#writing a Program to read the data in another file
outLine=open('grades.txt', 'w');
grades=0;
print("Enter a grade");
grades=input();
while(grades!='q'):
    #It creates a new file inside the directory and writes it
    print("Enter a grade");
    grades=input();
    outLine.write(grades+ '\n');

outLine.close();
