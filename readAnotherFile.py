#In this Program we are writing a program to read another file.
FindFile=open('name.txt','r');
#  'fake.txt ' file has been already created in the previous program.
#The above variable will locate the 'fake.txt' in order to print the data. We need another variable that stores the data of it.
contentInsideTheFile=FindFile.readline();
print(contentInsideTheFile);
