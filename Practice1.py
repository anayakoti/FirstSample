createNewFile=open('dummy.txt', 'w');
grades=0;
print("Enter a rollnumber");
grades=input();
while(grades!='*'):
    createNewFile.write(grades +"\n");
    print("Enter a rollnumber");
    grades=input();

createNewFile.close();
                        
    
