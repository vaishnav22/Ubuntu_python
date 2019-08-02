class Account():

    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def __str__(self):
        return "Account owner :{}\n Account balance: {}".format(self.owner,self.balance)


    def deposit(self,dep_amt):
        self.balance += dep_amt
        print('Deposit Accepeted')

    def withdraw(self,wd_amt):
        if self.balance >=wd_amt:
            self.balance -=wd_amt
            print('Withdrawl Accepted')

        else:
            print('Funds unavailale')


acct1 = Account('vaishnav', 10000)
print(acct1)

acct1.owner

acct1.balance

acct1.deposit(2000)

print(acct1.balance)

acct1.withdraw(10000)

print(acct1.balance)



