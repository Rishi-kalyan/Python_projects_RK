"""
- 3 flavours of coffee
   flavour         requirement                       price
1.espresso- 50ml water + 18g coffee                 -$1.5
2.latte-  200ml water + 24g coffee + 50ml milk      -$2.5
3.cappuccino- 250ml water + 24g coffee + 100ml milk -$3.0

coin operated:
penny - $0.01
dime - $0.1
nickel- $0.05
quarter - $0.25

-print report on how much of resources left
-check if resources are sufficient when user orders drink
-take users order
-take the values of each coin and add the total.
-check if it adds up to the price of coffee if not rfund the money and take next order..
-update the resources.
"""
menu= {
    "espresso": {
        "water": 50,
        "coffee": 18,
        "milk":0,
        "price":1.5
    },
    "latte":{
        "water": 200,
        "coffee": 24,
        "milk":50,
        "price":2.5
    },
    "cappuccino":{
        "water": 250,
        "coffee": 24,
        "milk":100,
        "price":3.0
    }
}
resource={
    "water": 300,
    "milk":200,
    "coffee":100,
    "money":0
}
def coin_check(order):
    penny=int(input("Enter penny coins:"))
    nickel=int(input("Enter nickel coins:"))
    dime=int(input("Enter dime coins:"))
    quarter=int(input("Enter quarter coins:"))
    c=(penny*0.01)+(nickel*0.05)+(dime*0.1)+(quarter*0.25)
    if(c==menu[order]["price"]):
        return True
    else:
        return False

    

def check_resources(order):
    if(menu[order]["water"]<=resource["water"] and menu[order]["coffee"]<=resource["coffee"] and menu[order]["milk"]<=resource["milk"]):
        return True
    else:
        return False

def machine():
    switch=input("press any key to ORDER or type 'off' to TURN-OFF the machine:")
    while(switch!="off"):
        print(""" MENU: 
                    ESPRESSO  - $1.5
                    LATTE     - $2.5
                    CAPPUCCINO- $3""")
        order=input(f"Enter Your Order:")
        if(check_resources(order)):
            print("""Coin conversion:
            penny is 0.01 USD
            Nickel is 0.05 USD
            dime is 0.1 USD
            quarter is 0.25 USD """)
            if(coin_check(order)):
                print(f"Total change is {menu[order]['price']}")
                resource["water"]=resource["water"]-menu[order]["water"]
                resource["coffee"]=resource["coffee"]-menu[order]["coffee"]
                resource["milk"]=resource["milk"]-menu[order]["milk"]
                resource["money"]=resource["money"]+menu[order]["price"]
                print(f"enjoy your {order}")
                switch=input("press any key to ORDER or type 'off' to TURN-OFF the machine:")
            else:
                switch=input("press any key to ORDER or type 'off' to TURN-OFF the machine:")
        else:
            print("Resources aren't sufficient")
            switch=input("please type 'off' to turn the machine off: ")
machine()