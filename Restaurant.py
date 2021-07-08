class RestaurantTable: 

    menus={
        'pizza':5000,
        'cola':600,
        'apple juice':2000,
        'hamburger':1000,
        'fried potato':1500
    }

    def __init__(self) :
        self.total=0
        self.orders=[]

    def addOrder(self,order):
        self.orders.append(order)
        self.total+=self.menus[order]
    
    def printBill(self):
        for order in  self.orders:
            print(f'{order} : {self.menus[order]}')

        print(f'total price is {self.total}')

def startProgram() :
    table=RestaurantTable()

    while True :
        order=input('order : ')
        table.addOrder(order)

        another=input('order again ? y/n : ')

        if another == 'y' :
            continue;
        if another == 'n':
            table.printBill()
            break

startProgram() 