from sqlalchemy.orm import sessionmaker
import db
import user
import msg

def startAtm():
    while user.loginAttempt < user.loginLimit:
        getPass = int(input(msg.m['askPass']))
        if user.checkpin(getPass):
            print(msg.m['welcome'])
            m_opt = int(input(msg.m['mainMenu']))

            if m_opt == 1:
                print(f"Your Account Balance is ${user.checkBalance()}")
            elif m_opt == 2:
                depositAmount = float(input(msg.m['dpAmt']))
                user.deposit(depositAmount)
            elif m_opt == 3:
                widAmount = float(input(msg.m['wAmt']))
                user.withdraw(widAmount)
            elif m_opt == 4:
                transferAmount = float(input(msg.m['transAmt']))
                user.trans(transferAmsount)
        else:
            user.loginAttempt += 1
    print(msg.m['acBlocked'])

mySession = sessionmaker(bind=db.engine)

appSession = mySession()

startAtm()

appSession.close()

