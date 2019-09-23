#Write a program to work with iterators in a dictionary
rollNumbers={'Anudeep':'08RE1A1202', 'Adarsh':'08RE1A1201', 'Anwesh':'08RE1A1203'};
for It in rollNumbers:
    print(It, rollNumbers[It]);

print(">>>>>>>>>>>>>>>>>>>>>>");
#Lets try another program to work with loops using next();
#lets create a new dictionary to avoid confusion.
names={'anudeep':'1202', 'karnakar':'1206', 'Rakesh':'1226'};
#using iter();
item=iter(names);
print(next(item));
print(">>>>>>>>>>>>>>>>>>>>");
print(names.keys());
print(names.values());


