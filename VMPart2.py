# Author: <LIUJIAJUN>
# Admin No: <211283E>
# when add drink type, it will capitalize the description input
# it checks for the quantity when buying drinks
goods = {'IM': {'description': 'Iced Milo', 'price': 1.5, 'quantity': 30},
         'IC': {'description': 'Iced Coffee', 'price': 1.5, 'quantity': 40},
         'CC': {'description': 'Coca cola', 'price': 1.3, 'quantity': 50},
         'HM': {'description': 'Hot Milo', 'price': 1.2, 'quantity': 50},
         '1P': {'description': '100 Plus', 'price': 1.1, 'quantity': 50},
         'HC': {'description': 'Hot Coffee', 'price': 1.2, 'quantity': 0}}
# To add drink type
def add_drink_type(drink_id, description, price, quantity):
    loop = True
    while loop:
        drink_id = input('Enter drink id: ').upper()
        product_info = goods.get(drink_id, 0)
        if product_info != 0:
            print('Drink id exist!')
            continue
        else:
            product_info = {}
            description = input("Enter description of drink: ").title()
            while True:
                try:
                    price = float(input("Enter price:$ "))
                    if price < 0:
                        continue
                    else:
                        break
                except:
                    print("Invalid input Try again")
            while True:
                try:
                    quantity = int(input("Enter quantity: "))
                    if quantity < 0:
                        continue
                    else:
                        break
                except:
                    print("Invalid input Try again")
        product_info['description'] = description
        product_info['price'] = price
        product_info['quantity'] = quantity
        goods[drink_id] = product_info
        loop = False
# replenish the drink
def replenish_drink(drink_id, quantity):
    for key in goods:
        if goods[key]['quantity'] != 0:
            print('{:<2}{:<3}{:<12}{:<1}{:<0}{:<3}{:<1}{:<3}'.format
                  (key, '.', goods[key]['description'], '(S$', goods[key]['price'], ')', 'Qty:',
                   goods[key]['quantity']))
        elif goods[key]['quantity'] == 0:
            goods[key]['quantity'] = '***Out of Stock***'
            print('{:<2}{:<3}{:<12}{:<1}{:<0}{:<3}{:<3}'.format
                  (key, '.', goods[key]['description'], '(S$', goods[key]['price'], ')',
                   goods[key]['quantity']))
            goods[key]['quantity'] = 0
    loop = True
    while loop:
        drink_id = input('Enter drink id: ').upper()
        if drink_id in goods:
            if goods[drink_id]['quantity'] > 5:
                print("No need to replenish. Quantity is greater than 5.")
                break
            else:
                while True:
                    try:
                        quantity = int(input("Enter quantity: "))
                        if quantity <= 0:
                            print("Invalid Input Try Again")
                            continue
                        elif quantity >= 0:
                            quantity = goods[drink_id]['quantity'] + quantity
                            goods[drink_id]['quantity'] = quantity
                            print(goods[drink_id]['description'], "has been top up")
                        break
                    except:
                        print("Invalid input Try again")
                break
        else:
            print("No drink with this drink id. Try again")
# use for restore the quantity of drinks when the payment cancelled
choice_list = []
# back to the loop when vendor or user finished their manipulation
vendors = True
while vendors == True:
    identity = input('Are you a vendor (Y/N)? ').upper()
    if identity == 'N':
        print('Welcome to ABC Vending Machine')
        print("Select from the following choices to continue:")
        for key in goods:
            if goods[key]['quantity'] != 0:
                print('{:<2}{:<3}{:<12}{:<1}{:<0}{:<3}{:<1}{:<3}'.format
                      (key, '.', goods[key]['description'], '(S$', goods[key]['price'], ')', 'Qty:',
                       goods[key]['quantity']))
            elif goods[key]['quantity'] == 0:
                goods[key]['quantity'] = '***Out of Stock***'
                print('{:<2}{:<3}{:<12}{:<1}{:<0}{:<3}{:<3}'.format
                      (key, '.', goods[key]['description'], '(S$', goods[key]['price'], ')',
                       goods[key]['quantity']))
                goods[key]['quantity'] = 0
        print('0.   Exit / Payment')
        drink = 0
        total = 0
        while True:
            choice = input("Enter choice: ").upper()
            if choice in goods:
                if goods[choice]['quantity'] == 0:
                    print(choice, 'is out of stock')
                else:
                    total += goods[choice]['price']
                    drink += 1
                    goods[choice]['quantity'] = goods[choice]['quantity'] - 1
                    print("No. of drinks selected: ", drink)
                    choice_list.append(choice)
            elif choice == '0':
                if drink == 0:
                    break
                else:
                    loop = True
                    while loop:
                        print('Please Pay: $%.2f' % total)
                        if drink >= 1:
                            print("Indicate your payment: ")
                            while True:
                                try:
                                    TenNote = int(input('Enter no. of $10 notes: '))
                                    if TenNote < 0:
                                        continue
                                    else:
                                        break
                                except:
                                    print('Invalid Input Try Again')
                            money = TenNote*10
                            if money >= total:
                                change = money - total
                                print('Please collect your change:$%.2f' % change)
                                print('Drinks paid. Thank you.')
                                choice_list.clear()
                            elif money < total:
                                while True:
                                    try:
                                        fiveNote = int(input('Enter no. of $5 notes: '))
                                        if fiveNote<0:
                                            continue
                                        else:
                                            break
                                    except:
                                        print("Invalid Input Try Again")
                                money = TenNote*10+fiveNote*5
                                change = money - total
                                if money >= total:
                                    print('Please collect your change:$%.2f' % change)
                                    print('Drinks paid. Thank you.')
                                    choice_list.clear() #//to clear the choice_list for the drink you paid
                                elif money < total:
                                    while True:
                                        try:
                                            twoNote = int(input('Enter no. of $2 notes: '))
                                            if twoNote<0:
                                                continue
                                            else:
                                                break
                                        except:
                                            print("Invalid Input Try Again")
                                    money = TenNote*10+fiveNote*5+twoNote*2
                                    change = money - total
                                    if money >= total:
                                        print('Please collect your change:$%.2f' % change)
                                        print('Drinks paid. Thank you.')
                                        choice_list.clear()
                                    elif change < 0:
                                        print('Not enough to pay for the drinks')
                                        print('Take back your cash!')
                                        opinion = input('Do you want to cancel the purchase? Y/N: ')
                                        if opinion == 'Y' or opinion == 'y':
                                            print('Purchase is cancelled. Thank you.')
                                            for i in range(len(choice_list)):
                                                goods[choice_list[i]]['quantity'] = goods[choice_list[i]][
                                                                                        'quantity'] + 1
                                        elif opinion == 'N' or opinion == 'n':
                                            loop = True
                                            continue
                            loop = False # it would not ask for payment when payment is enough
                break # break the loop when enter 0
            else:
                print("Invalid option")

    elif identity == 'Y':
        print('Welcome to ABC Vending Machine.')
        print('Select from following choices to continue:')
        print('1. Add Drink Type')
        print('2. Replenish Drink')
        print('0. Exit')
        while True:
            while True:
                try:
                    choice1 = int(input('Enter choice: '))
                    break
                except:
                    print("Invalid Input Try Again")
            if choice1 == 1:
                add_drink_type(goods, goods, goods, goods)
            elif choice1 == 2:
                replenish_drink(goods, goods)
            elif choice1 == 0:
                break