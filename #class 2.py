class restaurant:
    def __init__(self):
        self.menu_items={}
        self.book_table=[]
        self.customer_orders=[]
    def add_item_to_menu(self,item_name,price):
        self.menu_items[item_name]=price
        print(f"added:'{item_name}'to menu at{price}")
    def book_tables(self,table_num):
        if table_num not in self.book_table:
            self.book_table.append(table_num)
            print(f"table{table_num}booked successfully")
        else:
            print(f"table{table_num}alredy booked")
    def customer_order(self,table_num,order_items):
        if table_num in self.book_table:
            self.customer_orders.append(order_items)
            print(f"order take for table{table_num}:{order_items}")
        else:
            print(f"table{table_num}is not booked")
         
my_restaurant=restaurant()
my_restaurant.add_item_to_menu("dhosha",10)
my_restaurant.add_item_to_menu("putt",15)
my_restaurant.add_item_to_menu("poratta",12)
my_restaurant.book_tables(3)
my_restaurant.book_tables(5)
my_restaurant.book_tables(4)
my_restaurant.customer_order(3,["dhosha","putt"])
my_restaurant.customer_order(5,["poratta"])
my_restaurant.customer_order(6,["putt"])
my_restaurant.customer_orders
my_restaurant.menu_items

class restaurant:
    def __init__(self):
        self.menu_items={}
        self.book_table=[]
        self.customer_orders=[]
        self.bills=[]
    def add_item_to_menu(self,item_name,price):
        self.menu_items[item_name]=price
        print(f"added:'{item_name}'to menu at{price}")
    def book_tables(self,table_num):
        if table_num not in self.book_table:
            self.book_table.append(table_num)
            print(f"table{table_num}booked successfully")
        else:
            print(f"table{table_num}alredy booked")
    def customer_order(self,table_num,order_items):
        if table_num in self.book_table:
            self.customer_orders.append(order_items)
            print(f"order take for table{table_num}:{order_items}")
        else:
            print(f"table{table_num}is not booked")
    def bill(self,table_num,order_items):
        if table_num in self.book_table:
            self.bills.extend(order_items)
            total_price=0
            for items in order_items:
                price=self.menu_items.get(items,0)
                total_price+=price
                print(f"order taken fo table{table_num}:{order_items}")
                print(f"total bill:{total_price}")
        else:
            print(f"table{table_num}is not booked")

my_restaurant=restaurant()
my_restaurant.add_item_to_menu("dhosha",10)
my_restaurant.add_item_to_menu("putt",15)
my_restaurant.add_item_to_menu("poratta",12)
my_restaurant.book_tables(3)
my_restaurant.book_tables(5)
my_restaurant.book_tables(4)
my_restaurant.customer_order(3,["dhosha","putt"])
my_restaurant.customer_order(5,["poratta"])
my_restaurant.customer_order(6,["putt"])
my_restaurant.customer_orders
my_restaurant.menu_items
my_restaurant.bills
my_restaurant.bill(3,["dhosha","putt"])