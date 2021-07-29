
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
Unicorn Tears """)

i=0
order=[]
count =0
menuList=['wings','cookies','spring rolls','salmon','steak','meat tornado','a literal garden','ice cream','cake','pie','coffee','tea','unicorn tears']
print("""***********************************
** What would you like to order? **
***********************************""")
while i>=0:
 order_item = input(">")
 order_item=order_item.lower()
 if order_item in menuList:
  order.append(order_item)
  count = order.count(order_item)
  print(f" ** {count} order of {order_item} have been added to your meal **")
 elif order_item == "quit":
     break
 else:
  print('** Your Order is not in the menu! Please choose from the above menu **')

     
print('your orders are : ')
for j in order :
    print(j)
    