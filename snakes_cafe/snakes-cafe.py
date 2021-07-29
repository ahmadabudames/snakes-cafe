print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************

Appetizers
----------
Wings
Cookies
Spring Rolls

Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden

Desserts
--------
Ice Cream
Cake
Pie

Drinks
------
Coffee
Tea
Unicorn Tears

***********************************
** What would you like to order? **
***********************************

""")
menu = ['wings', 'cookies', 'spring rolls', 'salmon', 'steak', 'meat tornado',
        'a literal garden', 'ice Cream', 'cake', 'pie', 'coffee', 'tea', 'unicorn tears']

orders = []

names_of_order = []


def our_order():

    order = input('please write your order >')
    if order.lower() in menu:
        orders.append(order)
        if order not in names_of_order:
            names_of_order.append(order)
        print(
            f'** {orders.count(order)} order of {order} have been added to your meal **')
        our_order()
    
our_order()
