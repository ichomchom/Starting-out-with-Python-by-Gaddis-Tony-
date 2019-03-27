HOUR_PER_LABOR = 35

def main():
    walls = int(input('Please enter wall space: '))
    painted_price = float(input('Please enter paint price: '))
    paint_required = (walls/112) * 1
    labor_required = (walls/112) * 8
    paint_cost = painted_price * paint_required
    labor_charged = labor_required * 35
    total = labor_charged + paint_cost

    print('Paint required: ', paint_required )
    print('Labor required: ', labor_required)
    print('Paint cost: ', paint_cost)
    print('Labor charges: ', labor_charged)
    print('Total cost: ', total)
        
main()
