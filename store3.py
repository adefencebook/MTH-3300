#******************************************************************************
# store3.py
#******************************************************************************
# Name: Duncan
#******************************************************************************
# Collaborators/outside sources used 
#(IMPORTANT! Write "NONE" if none were used):
#
# None
#
# Reminder: you are to write your own code.
#******************************************************************************
# Overall notes (not to replace inline comments):
#
#
# 
# 

class Store:
    def __init__(self, name):
        """
        Docstring for __init__
        
        :param self: the store
        :param name: the name of the store
        """
        self._name = name
        self._inventory = {}
    
    def show_inventory(self):
        """
        Docstring for show_inventory
        
        :param self: the store

        shows the inventory and getting the users input
        """
        print("The Store has the following items")
        for i in self._inventory:
            print(f'{i}: {self._inventory[i]._inv}', end=" ")
        print()
        user_input = input("Enter item name or PAY to end your order. ")
        return user_input

    def update_inventory(self, item):
        """
        Docstring for update_inventory
        
        :param self: the store
        :param item: updating or adding the item to the inventory of the store
        """
        self._inventory[item._name] = item

    def POS(self):
        """
        Docstring for POS
        
        :param self: the store

        This method allows the user to input various items and their quantity to buy them from the store
        such that the items are removed from the store and allows the user to know the price
        """
        ordering = True
        store_cost = 0
        pre_tax = 0

        #Getting the orders
        user_entry = self.show_inventory()
        while ordering:
            if user_entry != "PAY":
                try:
                    user_item = self._inventory[user_entry]
                    quant = int(input(f'How many {user_item._name}s are you buying? We have {user_item._inv} in stock: '))
                    #do we have enough of that item
                    if user_item._inv < quant:
                        print(f'Sorry we don\'t have enough {user_item._name}\'s')
                        quant = int(input(f'How many {user_item._name}s are you buying? We have {user_item._inv} in stock: '))
                    #updating sales info
                    store_cost += user_item._cost * quant
                    pre_tax += user_item._sales_price * quant
                    #updaint inventory
                    user_item._add_inv(quant*-1)
                    self.update_inventory(user_item)
                except KeyError:
                    print("That item doesn't exist please try again.")
                user_entry = self.show_inventory()
            else:
                ordering = False
        
        #Processing the orders
        tax = 1.08
        total = pre_tax * tax
        store_profit = total - store_cost
        print("We will now calculate your total order!")
        print(f'Your total before tax is ${pre_tax:.2f}')
        print(f'Your total with tax is ${total:.2f}')
        print(f'Your order cost {self._name} ${store_cost:.2f}')
        print(f'{self._name} made of profit of #{store_profit:.2f}')

    def sale(self, percent):
        """
        Docstring for sale
        
        :param self: the store
        :param percent: how much the item is on sale
        """
        for i in self._inventory:
            item = self._inventory[i]
            print(f'Old price of {item._name} was {item._sales_price}')
            new_price = item._sales_price * (1-percent)
            self._inventory[i]._change_sales_price(new_price)
            print(f'New price of {item._name} is {item._sales_price}')

class Item:
    def __init__(self, name, cost, sales_price, inv):
        """
        Docstring for __init__
        
        :param self: the item
        :param name: the name of the item
        :param cost: the cost the store paid to get the item
        :param sales_price: the price the customer will pay for the item
        :param inv: how many the store has of the item
        """
        self._name = name
        self._cost = cost
        self._sales_price = sales_price
        self._inv = inv

    def _add_inv(self, amount):
        """
        Docstring for _add_inv
        
        :param self: the item
        :param amount: the amount to change the inventory
        """
        self._inv += amount
    
    def _change_cost(self, cost):
        """
        Docstring for _change_cost
        
        :param self: the item
        :param cost: the new cost
        """
        self._cost = cost

    def _change_sales_price(self, sales_price):
        """
        Docstring for _change_sales_price
        
        :param self: the item
        :param sales_price: the new sales_price
        """
        self._sales_price = sales_price


#running stuff

def setting_up_store():
    """
    Docstring for setting_up_store

    ment to set up the store before shopping
    """
    set_up = input("Would you like the setup to be: STANDARD or CUSTOM: ")
    if set_up == "STANDARD":
        store_name = 'hell'
        bigStore = Store(store_name)
        print("populating the store with apples, bananas and cokes")
        bigStore.update_inventory(Item('Apple', 1, 1.50, 20))
        bigStore.update_inventory(Item('Banana', .50, 1, 50))
        bigStore.update_inventory(Item('Coke', .2, 1, 100))
    elif set_up == "CUSTOM":
        store_name = input("What should the store be named: ")
        bigStore = Store(store_name)
        
        #Getting and putting in items
        inputting = True
        while inputting:
            item_name = input("What should the item be named, DONE to finish: ")
            if item_name != "DONE":
                item_cost = float(input("How much does it cost: "))
                item_price = float(input("How much should the store sell it for: "))
                item_inv = int(input("How many does the store have: "))
                bigStore.update_inventory(Item(item_name,item_cost,item_price,item_inv))
            else:
                inputting = False
        print("The Store has been filled")
    else:
        print("you broke it")
    return bigStore

def main():
    bigStore = setting_up_store()
    print(f'Thank you for shopping at {bigStore._name}')
    sale = input("Do you think theirs a sale, YES or NO: ")
    if sale == "YES":
        print("Oh great it looks like were having a sale.")
        sale_amount = float(input("how much is it, i.e. (.20): "))
        bigStore.sale(sale_amount)
    else:
        print("Onto your shopping")
    bigStore.POS()

main()