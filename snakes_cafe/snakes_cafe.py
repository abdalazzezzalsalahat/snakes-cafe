from textwrap import dedent

def welcome():
  message = """
  **************************************
  **    Welcome to the Snakes Cafe!   **
  **    Please see our menu below.    **
  **                                  **
  ** To quit at any time, type "quit" **
  **************************************
  """
  print(dedent(message))

def menu():
  menu = """ 
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
  """
  print(dedent(menu))

def order():
    order_messsage = """
    ***********************************
    ** What would you like to order? **
    *********************************** 
    """
    print(order_messsage)
    Snake_cafe = {
      'Wings' : 0,
      'Cookies' : 0,
      'Spring Rolls' : 0,
      'Salmon' : 0,
      'Steak' : 0,
      'Meat Tornado' : 0,
      'A Literal Garden' : 0,
      'Ice Cream' : 0,
      'Cake' : 0,
      'Pie' : 0,
      'Coffee' : 0,
      'Tea' : 0,
      'Unicorn Tears' : 0
    }
    while True:
        user_order = input('> ')
        if user_order == 'quit':
            break
        if user_order.capitalize() in Snake_cafe:
            Snake_cafe[user_order.capitalize()] += 1
            print( f'** {Snake_cafe[user_order.capitalize()]} order of {user_order.capitalize()} have been added to your meal **')  
        elif user_order.capitalize() not in Snake_cafe:
            print('sorry , we dont have your order in our menu !!')

welcome()
menu()
order()
