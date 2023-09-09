from ownable import Ownable
class Cart(Ownable):
    from item_manager import show_items
    def __init__(self, owner):
        super().__init__() 
        self.set_owner(owner)
        self.items = []
    def items_list(self):
        return self.items

    def add(self, item):
        self.items.append(item)

    def total_amount(self):
        price_list = []
        for item in self.items:
            price_list.append(item.price)
        return sum(price_list)
    
    def clear_cart(self):
        self.items = []
    def check_out(self):
        if self.owner.wallet.balance > self.total_amount():
            self.owner.wallet.balance -= self.total_amount()
            self.owner.cart.owner.wallet.deposit(self.total_amount())  
            for item in self.items:
                
                item.set_owner(self.owner)
            self.clear_cart() 
        else:
            print("No puedes comprarlo")