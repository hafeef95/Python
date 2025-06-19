class Bankaccount:
    def __init__(self,account_num,customer_name,balance,date_of_opening):
        self.account_num=account_num
        self.customer_name=customer_name
        self.balance=balance
        self.date_of_opening=date_of_opening
        
    def deposit(self,amount):
        if amount>0:
            self.balance+=amount
            print(f"deposited:{amount}. new balance:{self.balance}")
        else:
            print("deposit amount must be positive")
    def withdraw(self,amount):
        if amount>self.balance:
            print("insufficiant balance")
        else:
            self.balance-=amount
            print(f"withdraw:{amount}. new balance:{self.balance}")
    def check_balance(self,):
        print(f"account balance:{self.balance}")
        return self.balance
account=Bankaccount("9536472387","MUHAMMED SALMAN",1000,10/1/2010)        
account.deposit(500)
account.withdraw(300)
account.check_balance()

class inventory:
    def __init__(self):
        self.items={}
    def add_item(self,item_id,item_name,stock_count,price):
        self.items[item_id]={'item_name':item_name,'stock_count':stock_count,'price':price}
    def update_item(self,item_id,item_name,stock_count,price):
        if item_id in self.items:
            if item_name is not None:
                self.items[item_id]['item_name']=item_name
            if stock_count is not None:
                self.items[item_id]['stock_count']=stock_count
            if price is not None:
                self.items[item_id]['price']=price
            else:
                print("item not found")
    def check_item_details(self,item_id):
        return self.items.get(item_id,"item not found.")
inv=inventory()
inv.add_item(209,"laptop",50,35000)
inv.update_item(209,"laptop",34,36000)
details=inv.check_item_details(209)
print(details)

