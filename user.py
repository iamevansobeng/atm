from sqlalchemy.orm import sessionmaker
import db
import msg

#mmmmmmmmmmmmmmmmmmmmm
#   CREATING A USER
#mmmmmmmmmmmmmmmmmmmmm
loginAttempt = 0
loginLimit = 3
mySession = sessionmaker(bind=db.engine)
appSession = mySession()

## -- THIS IS THE SELECTED USER AT THE MOMENT
quer = appSession.query(db.Atm).get(1)

#------- FUNCTION FOR CREATING A USER ---------
def createUser():
    user = db.Atm(id=1,name='Evans Obeng',em='me@you.we',bal=900,pin=8879)

    appSession.add(user)
    appSession.commit()
    appSession.close()


if __name__ == '__main__':
    createUser()




#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
#   FUNCTIONS
#mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm
def checkpin(ePin):
    correctPin = quer.pin
    if correctPin == ePin:
        return True
    else:
        print(msg.m['incPass'])

def checkBalance():
    return quer.bal

def deposit(amt):
    oldBal = checkBalance()
    newBal = oldBal + amt
    quer.bal = newBal
    appSession.commit()
    return print(f"\n Deposit of ${amt} made successful \n Your new Balance is ${newBal}\b")

def withdraw(amt):
    if amt > checkBalance():
        print("\n You don't have enought balance to complete the transcaction \n")
    elif checkBalance() - amt >= 50:
        quer.bal -= amt
        appSession.commit()
        print(f'\n You have Successfully withdrwan ${amt}, Your balance is ${checkBalance()}')
    elif checkBalance() - amt < 50:
        print("\n A minimum of $20 is required to keep your account open \n")

def trans(amt):
    if amt > checkBalance():
        print("\n You don't have enought balance to complete the Transfer \n")
    elif checkBalance() - amt >= 50:
        numQ = input('\n\n    Enter the number of the reciepient\n')

#checking if number has 10 characters, so you can't send to single digits(eg. 1,0)
        if len(numQ) == 10:
            quer.bal -= amt
            appSession.commit()
            print(f'\n Transfer of ${amt} Successfuly made to {numQ} Your balance is ${checkBalance()}')
        else:
            print(msg.m['invalNo'])
    elif amt == checkBalance():
        print("\n Transfer Failed , A minum of $50 is required to keep your account open \n")