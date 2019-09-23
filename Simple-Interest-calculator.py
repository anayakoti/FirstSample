balance=5000;
rate=2.02;
year=1;
while(year<=10):
    balance=balance*2.02;
    print("The balance of:" +str(year) +":" + "$"+str(round(balance)));
    year=year+1;

