#In this program we are creating a program to create an hitogram on the grades.
#This is like a data representation.
bar='';
for grade in open('grades.txt'):
    for i in range(1,int(grade)):
        if(i%5==0):
         bar=bar+'*';
    print(bar, i);
    bar='';
                  

   
