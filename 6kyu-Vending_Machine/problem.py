class VendingMachine():
    def __init__(self, items, money):
        self.items=items
        self.money=money

    def vend(self, selection, insertedMoney):
        item={}
        for i in self.items:
            if (i['code']==selection):
                item=i
        if(item):
            if(insertedMoney < item['price']): return 'Not enough money!'
            if(item['quantity']<=0): return item['name']+': Out of stock!'
            else:
                self.money+=item['price']
                if(item['price']==insertedMoney): return 'Vending '+item['name']
                else: return 'Vending '+item['name']+' with '+"{:.2f}".format(insertedMoney - item['price'])+' change.'
        else: return 'Invalid selection! : Money in vending machine = '+"{:.2f}".format(self.money)