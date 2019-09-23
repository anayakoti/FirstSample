#Creating a new file here using open() function 
dummyVariable=open('fakefile.txt','w');
#Here we are creating a filename and give two arguments one:filename and the other is 'w'
print("Enter a number");
storage=input();
while(storage!='*'):
    dummyVariable.write(storage+ "\n");
    print("Enter a number");
    storage=input();

dummyVariable.close();
    
