####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750


############################# Start Here! ##############################
cupcake_shop_name= "Cake pops"
cake_pops = {
    "vanilla":2,
    "chocolate":2,
    "strawberry":2,
    "caramel":2,
    "rasberry":2
    }
signature_flavors = {
    "tuna":2.750,
    "salmon":2.750,
    "red herring":2.750
}
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """

    # for item in menu:
      #  print("- %s (%s) % (item, menu[item]")


print("|  Menu               |   Price      ")
print("----------------------------------------")
for key, value in menu.items() :
    print ("|",key, " "*(18-len(key)), "|",value)

print ("")

def print_originals():
    print("Our original flavor cupcakes (KD %s each):" % original_price)
    print("", *original_flavors, sep = "\n - ")
    print ("")
""" for item in original _flavors:
       print ("- %s" % item)"""


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    # your code goes here!
    print ("")
    for key,value in signature_flavors.items():
        print("-",key)
    print ("\n")


def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!

    """ for item in menu:
        if item == order:
            return True

        if item== original_flavors:
            return True

        if item == signature_flavors:
            return True
         return False

    """
  
    if order in menu or order in cake_pops or order in signature_flavors:
        return True
    else:
        return False




def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    print ("What's your order? (Enter the exact spelling of the item you want. Type 'exit' to end your order.)","\n")
    order=""
    
    #n= is_valid_order(order)
    
    while True:
        order=input()
        order= order.lower()
        
        if order != "exit":
            n= is_valid_order(order)
            #print (n)
            if n ==  True:
                order_list.append(order)
            else:
                print ("The item does not exist")

        else:
            return order_list

""" 
order_list=[]
user_input= ""
user_input = input("What's your order? (Enter the exact spelling of the item you want. Type 'exit' to end your order.)","\n")
while user_input.lower()= "exit":
    if is_valid_order(user_input):
        order_list.append(user_input)
    user_input= input()
return order_list
"""

def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True
    else:
        return False

   #return total>=5
# seham listen when you write line 143, make sure to put it directly after you
# define the function to not get indentation error

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
     
    total = 0

    # your code goes here!

    for item in order_list:
        if item in menu:
            total += menu[item]

        elif item in original_flavors:
            total += original_price

        elif item in signature_flavors:
            total += signature_price

   #  order_list= total

    return total


def print_order(order_list):
    """
    Print the order of the customer.
    """
    total= get_total_price(order_list)
    print("\n TO CONFIRM YOUR ORDER!!! Your order is: \n")

    for order in order_list:
        print ("- %s" % order)

    print("\nYour total price is: KD %s" % total)

    if accept_credit_card(total):
        print("\nThis order is eligible for credit card payment!")
    else:
        print ("\nThis order is not eligible for credit card payment. We apologize for your inconvenience.")

    print ("\nThank you for shopping with us at %s \n" % cupcake_shop_name)


    """seham here also. you can set total= the total price function instead
    calling it twice...."""

    # your code goes here!
