pin = 0000
bal = 10000
attempts = 3
print('***Welcome to MMT Bank***')
while attempts>=0:
    x = int(input('Enter pin number:'))
    if x == pin:
        print('***Login Successful***')
        print('Please select a Service: \n'
              + "1.View Balance \n"
              + "2.Withdrawal \n")
        s = int(input("Select 1 or 2 to continue: "))

        if s == 1:
            print('Your Balance is:')
            print(bal)
        elif s == 2:
            w = int(input('Enter Withdrawal Amount:'))
            if w < bal:
                print('Withdrawal Successful') 
                bal = bal - w
            else:
                print('Insufficent Funds')
        #if auth==3:
            #dep=input('Enter Deposit Amount')
            #newbal=bal+dep
            #bal=newbal
            #print(bal)
         #else:
             #bal=bal
        else:
           print('***Successfully Logged Out***')
    else:
       print('Invalid Password')
       attempts=attempts-1
       if attempts==0:
         print('Account Blocked')
         break



