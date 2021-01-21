# Write your code here
def reduce_resources(water, milk, beans,money):
    global water_in
    global beans_in
    global money_in
    global milk_in
    global disposable_cups_in
    
    if milk == 1:
        milk = 0
    water_in -= water
    beans_in -= beans
    milk_in -= milk
    disposable_cups_in -= 1
    money_in += money
    

def resources(water, milk, beans,money):
    global water_in
    global beans_in
    global money_in
    global choice
    
    if milk == 0:
        milk = 1
    
    cups_water = water_in//water
    cups_milk = milk_in//milk
    cups_beans = beans_in//beans 

    max_cups = int(min(cups_beans,cups_milk,cups_water))  

    if max_cups == 0 :
        print("Sorry, not enough water!") 
        choice = input("\nWrite action (buy, fill, take, buy, remaining, exit):\n") 

    else:
        print("I have enough resources, making you a coffee!")
        reduce_resources(water, milk, beans, money)
        choice = input("\nWrite action (buy, fill, take, buy, remaining, exit):\n") 
    
    if choice == "buy":
        exit = buy()
        if exit:
            return True               
    elif choice == "fill":
        exit = fill()
        if exit:
            return True   
    elif choice == "take":
        exit = take()
        if exit:
            return True   
    elif choice == "remaining":
        exit = remaining()
        if exit:
            return True 
    else:
        return True                    

def espresso():
    exit = resources(water=250, milk=0, beans=16, money=4)
    if exit:
        return True
    
    
def latte():
    exit = resources(water=350, milk=75, beans=20 , money=7)
    if exit:
        return True
    
    
def cappuccino():
    exit = resources(water=200, milk=100, beans=12, money=6)
    if exit:
        return True


def buy():
    buy_choice = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:\n")
    if buy_choice == '1':
        exit = espresso()
        if exit:
            return True
    elif buy_choice == '2':
        exit = latte()
        if exit:
            return True
    elif buy_choice == '3':
        exit = cappuccino() 
        if exit:
            return True   
    else:
        choice = input("\nWrite action (buy, fill, take, buy, remaining, exit):\n") 
        if choice == "buy":
            exit = buy()
            if exit:
                return True               
        elif choice == "fill":
            exit = fill()
            if exit:
                return True   
        elif choice == "take":
            exit = take()
            if exit:
                return True   
        elif choice == "remaining":
            exit = remaining()
            if exit:
                return True 
        else:
            return True  
         

def fill():
    global water_in
    global beans_in
    global disposable_cups_in
    global milk_in
    global choice
    
    water = int(input("\nWrite how many ml of water do you want to add:\n"))
    milk = int(input("Write how many ml of milk do you want to add:\n"))
    beans = int(input("Write how many grams of coffee beans do you want to add:\n"))
    cups = int(input("Write how many disposable cups of coffee do you want to add:\n"))
    water_in += water
    beans_in += beans
    disposable_cups_in += cups
    milk_in += milk     
    choice = input("\nWrite action (buy, fill, take, buy, remaining, exit):\n") 
    
    if choice == "buy":
        exit = buy()
        if exit:
            return True               
    elif choice == "fill":
        exit = fill()
        if exit:
            return True   
    elif choice == "take":
        exit = take()
        if exit:
            return True   
    elif choice == "remaining":
        exit = remaining()
        if exit:
            return True 
    else:
        return True 
        
def take():
    global money_in
    global choice
    
    print(f"\nI gave you ${money_in}")
    money_in = 0
    choice = input("\nWrite action (buy, fill, take, buy, remaining, exit):\n") 
    
    if choice == "buy":
        exit = buy()
        if exit:
            return True               
    elif choice == "fill":
        exit = fill()
        if exit:
            return True   
    elif choice == "take":
        exit = take()
        if exit:
            return True   
    elif choice == "remaining":
        exit = remaining()
        if exit:
            return True 
    else:
        return True 

def remaining():
    global choice
       
    machine_in()
    choice = input("\nWrite action (buy, fill, take, remaining, exit):\n") 
    if choice == "buy":
        exit = buy()
        if exit:
            return True               
    elif choice == "fill":
        exit = fill()
        if exit:
            return True   
    elif choice == "take":
        exit = take()
        if exit:
            return True   
    elif choice == "remaining":
        exit = remaining()
        if exit:
            return True 
    else:
        return True

def machine_in():
    print(f"""\nThe coffee machine has:
{water_in} of water
{milk_in} of milk
{beans_in} of coffee beans
{disposable_cups_in} of disposable cups
${money_in} of money""")



water_in = int(400)    
milk_in = int(540)
beans_in = int(120)  
disposable_cups_in = int(9)
money_in = int(550)
 
choice = input("Write action (buy, fill, take, remaining, exit):\n") 

while True:    
        
    if choice == "buy":
        exit = buy()
        if exit:
            break                       
    elif choice == "fill":
        exit = fill()
        if exit:
            break       
    elif choice == "take": 
        exit = take()
        if exit:
            break     
    elif choice == "remaining":
        exit = remaining()
        if exit:
            break                 
    else:
        break
