try:
    # user input for item buy
    total_item = input("Enter total number of item added: ")
    total_item = int(total_item) #type-casting to int
    total = 0 # initial price
    for i in range(0,total_item):# iterate to get all items price
        item_price = input("Enter the price of item: ") #user input for items price
        total += float(item_price) # Type-casting to float and adding in total to get total price at last
    print("Total price is ",total)
except ValueError: # Handling excpetion if wrong input occur
    print("Invalid price format. Please use numbers only.")