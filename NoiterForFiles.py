#Lets create an iterator for files.
#We have already created grades.txt file.
filePuller=open('grades.txt','r');
print(next(filePuller));
