# Super market using Python

# Items available in our super market
items=['cereals','flour','sugar','pasta','mixes','cheeses','eggs','milk','yogurt','butter','lunch meat','poultry','pork','waffles','vegetables','individual meals','ice cream','ll- purpose',' laundry detergent',' dishwashing liquid/detergent','paper towels','toilet paper','aluminum foil','sandwich bags','fruits','vegetables',' shampoo','soap','hand wash','shaving cream','coffee','tea','juice','soda','baby items','pet items','batteries','greeting cards']
slist=[]

# Introductory Greeting
def greet():
    print("Hi!,I am lexi -- your super market assistant ")
    print("how may I help you ?")

# The grocery is sorted accordingly
def grocerylist():
      print("Here's the list of groceries avalable in the store :")
      print("DRY GOODS     = cereals, flour, sugar, pasta, mixes")
      print("DAIRY         = cheeses, eggs, milk(1L), yogurt, butter")
      print("MEAT          = lunch meat, poultry, pork")
      print("FROZEN FOODS  = waffles, vegetables, individual meals, ice cream")
      print("CLEANERS      = all- purpose, laundry detergent, dishwashing liquid/detergent")
      print("PAPER GOODS   = paper towels, toilet paper, aluminum foil, sandwich bags")
      print("PRODUCE       = fruits, vegetables")
      print("PERSONAL CARE = shampoo, soap, hand wash, shaving cream")
      print("BEVERAGES     = coffee,tea, juice,soda")
      print("OTHERS        = baby items, pet items, batteries, greeting cards")
      print(" ")

# Display items in the cart
def viewcart():
    print('The number of items in the cart are : ',len(slist))
    while len(slist) != 0:
        print('Here are all the items available in the cart')
        for item in slist:
            for key, value in item.items():
                print(key, ':', value)
        break

# Creating a new cart
def newcart():
        item = {}
        item['name'] = input('Item name : ')
        while True:
            try:
                item['quantity'] = int(input('Item quantity : '))
                break
            except ValueError:
                print('Quantity should only be in digits')
        print('Item has been successfully added.')
        slist.append(item)

# Editing the items in the existing cart
def editcart():
    item_name = input('Enter the name of the item that you want to edit : ')
    for item in slist:
            if item_name.lower() == item['name'].lower():
                print('Here are the current details of ' + item_name)
                print(item)
                item['name'] = input('Item name : ')
                while True:
                    try:
                        item['quantity'] = int(input('Item quantity : '))
                        break
                    except ValueError:
                        print('Quantity should only be in digits')
                print('Item has been successfully updated.')
                print(item)
            else:
                print('Item not found')

# Search for an item in the supermarket
def search():
    find_item = input('Enter the item\'s name to search in inventory : ')
    if find_item in items:
        print(find_item,' is available')
    else:
        print(find_item,' is not available')

# Main function
if __name__== "_main_":

    greet()
    while True:
        query=input("User said :")
        if 'what are the groceries available ?'in query:
            grocerylist()
        elif 'add to cart'in query :
            newcart()
        elif'edit my cart' in query:
            editcart()
        elif 'view my cart' in query:
            viewcart()
        elif 'search' in query:
            search()
        elif 'exit' in query:
            print("Did you like shopping experience ? Please provide us your valuable feed back :)")
            feedback=input('')
            exit()
        else:
            print("sorry,I could not understand .could you please say that again?")