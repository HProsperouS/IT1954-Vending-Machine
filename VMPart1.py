# Author: <LIUJIAJUN>
# Admin No: <211283E>
while True:
    identity = input('Are you a vendor (Y/N)? ').upper()
    if identity == 'N':
        print('Welcome to ABC Vending Machine.')
        print('Select from following choices to continue:')
        print('IM. Iced Milo (S$1.5)')
        print('HM. Hot Milo (S$1.2)')
        print('IC. Iced Coffee (S$1.5)')
        print('HC. Hot Coffee (S$1.2)')
        print('1P. 100 Plus (S$1.1)')
        print('CC. Coca Cola (S$1.3)')
        print('0. Exit / Payment)')
        drink = 0
        total = 0
        while True:
            choice = input("Enter choice: ").upper()
            if choice == 'IM':
                product = "Iced Milo"
                product_price = 1.5

            elif choice == 'HM':
                product = "Hot Milo"
                product_price = 1.2

            elif choice == 'IC':
                product = "Iced Coffee"
                product_price = 1.5

            elif choice == 'HC':
                product = "Hot Coffee"
                product_price = 1.2

            elif choice == '1P':
                product = "100 Plus"
                product_price = 1.1

            elif choice == 'CC':
                product = "Coca Cola"
                product_price = 1.3

            elif choice == '0':
                if drink == 0:
                    break # break the loop when user not buying anything
                else:
                    loop = True
                    while loop:
                        print('Please Pay: $%.2f' % total)
                        if drink >= 1:
                            print("Indicate your payment: ")
                            while True:
                                try:
                                    TenNote = int(input('Enter no. of $10 notes: '))
                                    if TenNote<0 or TenNote == " ":
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
                            elif money < total:
                                while True:
                                    try:
                                        fiveNote = int(input('Enter no. of $5 notes: '))
                                        if fiveNote < 0 or fiveNote == '0':
                                            continue
                                        else:
                                            break
                                    except:
                                        print('Invalid input Try Again' )
                                money = TenNote*10+fiveNote*5
                                change = money - total
                                if money >= total:
                                    print('Please collect your change:$%.2f' % change)
                                    print('Drinks paid. Thank you.')
                                elif money < total:
                                    while True:
                                        try:
                                            twoNote = int(input('Enter no. of $2 notes: '))
                                            if twoNote < 0 or twoNote == " ":
                                                continue
                                            else:
                                                break
                                        except:
                                            print('Invalid Input Try Again')
                                    money = TenNote*10+fiveNote*5+twoNote*2
                                    change = money - total
                                    if money >= total:
                                        print('Please collect your change:$%.2f' % change)
                                        print('Drinks paid. Thank you.')
                                    elif change < 0:
                                        print('Not enough to pay for the drinks')
                                        print('Take back your cash!')
                                        opinion = input('Do you want to cancel the purchase? Y/N: ')
                                        if opinion == 'Y' or opinion == 'y':
                                            print('Purchase is cancelled. Thank you.')
                                            loop = False
                                        elif opinion == 'N' or opinion == 'n':
                                            continue
                        break  # to stop the loop when the money is enough to pay
                break # break the loop when user stop buying
            else:
                print("Invalid option")
                continue
            drink += 1
            total += float(product_price)
            print('No. of drinks selected = ', drink)
        break # to break the loop after user paid for drink
    elif identity == 'Y':
        print('Welcome to ABC Vending Machine.')
        print('Select from following choices to continue:')
        print('1. Add Drink Type')
        print('2. Replenish Drink')
        print('0. Exit')
        input('Enter choice: ')
        break
    else:
        print("Invalid Input, Try Again")
        continue