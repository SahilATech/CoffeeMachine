water_reserve = 400
milk_reserve = 540
beans_reserve = 120
disposable_cups = 9
cash_flow = 550
continuePr = True
def processCoffee(deductwater, deductmilk, deductbean, deductcup, addcash):
    global water_reserve
    global milk_reserve
    global beans_reserve
    global disposable_cups
    global cash_flow
    shouldcontinue = True
    if water_reserve < deductwater:
        lackResource('water')
        shouldcontinue = False
    if milk_reserve < deductmilk:
        lackResource('milk')
        shouldcontinue = False
    if beans_reserve < deductbean:
        lackResource('bean')
        shouldcontinue = False
    if disposable_cups < deductcup:
        lackResource('cups')
        shouldcontinue = False
    if shouldcontinue:
        water_reserve = water_reserve - deductwater
        milk_reserve = milk_reserve - deductmilk
        beans_reserve = beans_reserve - deductbean
        disposable_cups = disposable_cups - deductcup
        cash_flow = cash_flow + addcash
        enoughResource()
        
def processAddCoffee(addwater, addmilk, addbean, addcup):
    global water_reserve
    global milk_reserve
    global beans_reserve
    global disposable_cups
    global cash_flow
    water_reserve = water_reserve + addwater
    milk_reserve = milk_reserve + addmilk
    beans_reserve = beans_reserve + addbean
    disposable_cups = disposable_cups + addcup

def deductCash():
    global cash_flow
    cash_flow = 0
 
def enoughResource():
    print('I have enough resources, making you a coffee!')  
 
def lackResource(item):
    print('Sorry, not enough ' + item +'!') 

def processBuy():
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
    inp = input()
    if inp == 'back':
        mainmenu()
    else:
        coffee_type = int(inp)
        if coffee_type == 1:
            processCoffee(250, 0, 16, 1, 4)
        elif coffee_type == 2:
            processCoffee(350, 75, 20, 1, 7)
        elif coffee_type == 3:
            processCoffee(200, 100, 12, 1, 6)
        #printInfo()

def processFill():
    print('Write how many ml of water do you want to add:')
    wateradd = int(input())
    print('Write how many ml of milk do you want to add:')
    milkadd = int(input())
    print('Write how many grams of coffee beans do you want to add:')
    coffeeadd = int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    cupadd = int(input())
    processAddCoffee(wateradd, milkadd, coffeeadd, cupadd)
    #printInfo()

def processTake():
    print('I gave you $', cash_flow)
    deductCash()
    #print()
    #printInfo()

def printInfo():
    print('The coffee machine has:')
    print(water_reserve, ' of water')
    print(milk_reserve,  ' of milk')
    print(beans_reserve, ' of coffee beans')
    print(disposable_cups, ' of disposable cups')
    print(cash_flow, ' of money')

#printInfo()
def mainmenu():
    print("Write action (buy, fill, take, remaining, exit):")
    user_action = str(input())
    if user_action == 'buy':
        processBuy()
    elif user_action == 'fill':
        processFill()
    elif user_action == 'take':
        processTake()
    elif user_action == 'remaining':
        printInfo()
    elif user_action == 'exit':
        global continuePr
        continuePr = False

while continuePr:   
    mainmenu()
    
class CoffeeMachine:
    water_reserve = 400
    milk_reserve = 540
    beans_reserve = 120
    disposable_cups = 9
    cash_flow = 550
    continuePr = True
    action = None
    def __init__(self, action):
        self.action = action
        
    def printInfo(self):
        print('The coffee machine has:')
        print(self.water_reserve, ' of water')
        print(self.milk_reserve,  ' of milk')
        print(self.beans_reserve, ' of coffee beans')
        print(self.disposable_cups, ' of disposable cups')
        print(self.cash_flow, ' of money')
        
    def deductCash(self):
        self.cash_flow = 0
        
    def processTake(self):
        stm = 'I gave you $ {}'.format(self.cash_flow)
        self.deductCash()
        return stm
            
#machine = CoffeeMachine("printinfo")
machine = CoffeeMachine("processTake")
print(machine.processTake())
