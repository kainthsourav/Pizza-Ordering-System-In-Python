def choose_pizza(pizza,menu):
  print("Let me help you order a pizza. Here are the choices:")
  for (pizzaname,prize),menuitem in zip(pizza.iteritems(),menu.keys()):
    print("(%s) %s $%.2f" % (menuitem,pizzaname,prize))
  choice=raw_input("Please enter %s: " % (" or ".join(menu.keys())))
  if choice not in menu:
    return None
  return choice
def choose_qty():
  qty=raw_input("How many would you like?: ")
  iqty=None
  try: iqty=int(qty)
  except ValueError: return None
  return iqty
def main():
  pizza={'small':7.99,'medium':14.99,'large':18.99}
  menu={'a':'small','b':'medium','c':'large'}
  choice=None
  while not choice:
    choice=choose_pizza(pizza,menu)
  print("Ok, %s, that is $%.2f each." % (menu[choice],pizza[menu[choice]]))
  qty=None
  while not qty:
    qty=choose_qty()
  print("Your total is $%.2f." % (pizza[menu[choice]]*qty))
  print("Press <enter> to exit.")
  raw_input()
main()

