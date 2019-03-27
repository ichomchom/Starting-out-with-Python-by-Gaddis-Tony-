#DISCOUNT_PERCENTAGE is used as global
DISCOUNT_PERCENTAGE = 0.20

def main():
    #Get item reg price
    reg_price = get_regular_price()

    #Cal sale price
    sale_price = reg_price - discount(reg_price)

    #Display sale price
    print('The sale price is $', format(sale_price, ',.2f'), sep='')

#Def get regular price
def get_regular_price():
    price = float(input("Enter the item's regular price: "))
    return price

#Accepts item's price as an argument and return discont price
def discount(price):
    return price * DISCOUNT_PERCENTAGE

main()
