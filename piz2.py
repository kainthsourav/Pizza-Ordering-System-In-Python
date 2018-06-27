REG_PIZZA = ["Meatlovers", "Hot 'n' Spicy", "BBQ Chicken", "Satay Chicken", "Super Supreme", "Deluxe"]
GOURM_PIZZA = ["Hawaiian", "Veg Deluxe", "Beef and Onion", "Ham and Cheese", "Pepperoni", "Cheese"]
numPizza = 0
selection = 0
totalCost = 0
deliverCost = 3

def orderPizza():

        global numPizza
        global selection 
        global order
        global totalCost   

pizzaOrder=0
order = []

if pizzaOrder < numPizza:
        print(" ")
        print(" ")
        print(" ")
        print("=======Regular Pizza's=======")
        print("Press 1 for " + REG_PIZZA[0] + " - $8.50")
        print("Press 2 for " + REG_PIZZA[1] + " - $8.50")
        print("Press 3 for " + REG_PIZZA[2] + " - $8.50")
        print("Press 4 for " + REG_PIZZA[3] + " - $8.50")
        print("Press 5 for " + REG_PIZZA[4] + " - $8.50")
        print("Press 6 for " + REG_PIZZA[5] + " - $8.50")
        print("=======Gourmet Pizza's=======")
        print("Press 7 for " + GOURM_PIZZA[0] + " - $5.00")
        print("Press 8 for " + GOURM_PIZZA[1] + " - $5.00")
        print("Press 9 for " + GOURM_PIZZA[2] + " - $5.00")
        print("Press 10 for " + GOURM_PIZZA[3] + " - $5.00")
        print("Press 11 for " + GOURM_PIZZA[4] + " - $5.00")
        print("Press 12 for " + GOURM_PIZZA[5] + " - $5.00")
        print("==========Exit Menu==========")
        print("Press 0 to Exit")
        print("=============================")        
        selection = raw_input("Enter your choice (0-12):  ")

        if selection == 0:
            sys.exit()
        elif selection == 1:
            print(REG_PIZZA[0], "- $8.50")
            order.append(REG_PIZZA[0])
            print(order)
            pizzaOrder = pizzaOrder + 1
            totalCost = totalCost + 8.50
            print(" ")
            print(" ")
            print(" ")
        elif selection == 2:
            print(REG_PIZZA[1], "- $8.50")
            order.append(REG_PIZZA[1])
            print(order)
            pizzaOrder = pizzaOrder + 1
            totalCost = totalCost + 8.50
            print(" ")
            print(" ")
            print(" ")
        elif selection == 3:
            print(REG_PIZZA[2], "- $8.50")
            order.append(REG_PIZZA[2])
            print(order)
            pizzaOrder = pizzaOrder + 1
            totalCost = totalCost + 8.50
            print(" ")
            print(" ")
            print(" ")
        elif selection == 4:
            print(REG_PIZZA[3], "- $8.50")
            order.append(REG_PIZZA[3])
            print(order)
            pizzaOrder = pizzaOrder + 1
            totalCost = totalCost + 8.50
            print(" ")
            print(" ")
            print(" ")  
        elif selection == 5:
            print(REG_PIZZA[4], "- $8.50")
            order.append(REG_PIZZA[4])
            print(order)
            pizzaOrder = pizzaOrder + 1
            totalCost = totalCost + 8.50
            print(" ")
            print(" ")
            print(" ")
        elif selection == 6:
            print(REG_PIZZA[5], "- $8.50")
            order.append(REG_PIZZA[5])
            print(order)
            pizzaOrder = pizzaOrder + 1
            totalCost = totalCost + 8.50
            print(" ")
            print(" ")
            print(" ")
        elif selection == 7:
            print(GOURM_PIZZA[0], "- $5.00")
            order.append(GOURM_PIZZA[0])
            print(order)
            pizzaOrder = pizzaOrder + 1
            totalCost = totalCost + 5.00
            print(" ")
            print(" ")
            print(" ")
        elif selection == 8:
            print(GOURM_PIZZA[1], "- $5.00")
            order.append(GOURM_PIZZA[1])
            print(order)
            pizzaOrder = pizzaOrder + 1
            totalCost = totalCost + 5.00
            print(" ")
            print(" ")
            print(" ")
        elif selection == 9:
                print(GOURM_PIZZA[2], "- $5.00")
                order.append(GOURM_PIZZA[2])
                print(order)
                pizzaOrder = pizzaOrder + 1
                totalCost = totalCost + 5.00
                print(" ")
                print(" ")
                print(" ")
                elif selection == 10:
                        print(GOURM_PIZZA[3], "- $5.00")
                        order.append(GOURM_PIZZA[3])
                        print(order)
                        pizzaOrder = pizzaOrder + 1
                        totalCost = totalCost + 5.00
                        print(" ")
                        print(" ")
                        print(" ")
                elif selection == 11:
                        print(GOURM_PIZZA[4], "- $5.00")
                        order.append(GOURM_PIZZA[4])
                        print(order)
                        pizzaOrder = pizzaOrder + 1
                        totalCost = totalCost + 5.00
                        print(" ")
                        print(" ")
                        print(" ")
                elif selection == 12:
                        print(GOURM_PIZZA[5], "- $5.00")
                        order.append(GOURM_PIZZA[5])
                        print(order)
                        pizzaOrder = pizzaOrder + 1
                        totalCost = totalCost + 5.00
                        print(" ")
                        print(" ")
                        print(" ")
                elif pizzaOrder == numPizza and numPizza == 1:
                        print("==Order Details==")
                        print(order)
                        print("Total Cost:", totalCost)
                        print("==Thank You", customerName + "==")
                elif pizzaOrder == numPizza and numPizza == 2:
                        print("==Order Details==")
                        print(order[0])
                        print(order[1])
                        print("Total Cost:", totalCost)
                        print("==Thank You", customerName + "==")
                elif pizzaOrder == numPizza and numPizza == 3:
                        print("==Order Details==")
                        print(order[0])
        print(order[1])
        print(order[2])
        print("Total Cost:", totalCost)
        print("==Thank You", customerName + "==")

    elif pizzaOrder == numPizza and numPizza == 4:
        print("==Order Details==")
        print(order[0])
        print(order[1])
        print(order[2])
        print(order[3])
        print("Total Cost:", totalCost)
        print("==Thank You", customerName + "==")

    elif pizzaOrder == numPizza and numPizza == 5:
        print("==Order Details==")
        print(order[0])
        print(order[1])
        print(order[2])
        print(order[3])
        print(order[4])
        print("Total Cost:", totalCost)
        print("==Thank You", customerName + "==")




def deliveryPickup():

    option = int(input("Delivery or Pickup? (1 - Delivery OR 2 - Pickup):   "))

    if option < 1 or option > 2:       
        print("That is not a valid input - Try Again")

    global numPizza  
    global totalCost

    if option == 1:

        totalCost = totalCost + 3
        customerAddress = raw_input("Enter your Address: ")
        customerPhone = raw_input("Enter your phone number: ")
        print("Thank you", customerName, "Your Address is", customerAddress, "and your phone    number is", customerPhone)
        print(" ")
        numPizza = raw_input("Enter number of Pizza's Wanted (Max 5):  ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        orderPizza()

    if option == 2:
        numPizza = raw_input("Enter number of Pizza's Wanted (Max 5):  ")
        print(" ")
        print(" ")
        print(" ")
        print(" ")
        orderPizza()


customerName = raw_input("Enter your name please: ")

deliveryPickup()
