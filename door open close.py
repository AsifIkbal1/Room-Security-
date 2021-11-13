doorpassword='open@door' #ORGINAL PASSWORD
doorpassword=input("Enter The Password: ") #User input
count=0

while doorpassword!='open@door':
    count=count+1
    print('Wrong Password try Again')
    print('You have left...',3-count,'please Enter the valid password ') #you have three chance.

    doorpassword=input('Enter The Password: ')
    if count==2 and doorpassword!='open@door':
        print('max try = 3 is over ! the door is locked !')
        break
if doorpassword == 'open@door':
    print('Welcome to this room')
