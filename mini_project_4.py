from mp_functions import space, read_csv_file, save_csv_file, append_dict, update_items, print_csv_file
from csv import DictWriter, DictReader
from pprint import pprint

print("""\033[1;32m\nHi there, welcome to your cafe ordering app\033[0m""")

products = []
couriers = []
orders = []

products = read_csv_file('products.csv', products)
couriers = read_csv_file('couriers.csv', couriers)
orders = read_csv_file('orders.csv', orders)

order_status = ['Preparing','Ready for collection','Out for delivery','Complete']

# Main Menu
def main_menu():
    print("""\033[33m\nMain Menu:\033[0m""")
    print("""
[0] - To Exit 
[1] - Product Menu
[2] - Courier Menu
[3] - Order Menu
""")
    
    option = int(input("""\033[33m\nEnter your option here: \033[0m"""))
    
    if option == 0:
        save_csv_file('products.csv', products)
        save_csv_file('couriers.csv', couriers)
        save_csv_file('orders.csv', orders)
        space()
        print('\tThanks for visiting!')
        space()
        exit()
    
    elif option == 1:
        product_menu()
        
    elif option == 2:
        courier_menu()
    
    elif option == 3:
        orders_menu()
        
    else:
        print('Please enter a valid option')
        space()
        main_menu()    
        
# Product Menu
def product_menu():
    print("""\033[33m\nProduct Options:\033[0m""")
    print('''
[0] - Return to Main Menu
[1] - View Menu
[2] - Create New Product
[3] - Update Existing Product    
[4] - Delete a Product''')
    space()
    user_input = int(input("""\033[33m\nEnter your choice here: \033[0m"""))
        
        
    if user_input == 0:
        main_menu()
    
    elif user_input == 1:
        space()
        pprint(products)
        space()
        product_menu()
    
    elif user_input == 2:
        space()
        print("""\033[33m\nThe current menu is: \033[0m""")
        print_csv_file('products.csv')
        space()
        new_product = input("""\033[33m\nWhat would you like to create?  \033[0m""")
        product_price = float(input("""\033[33m\nEnter a price:   \033[0m"""))
        new_product_dict = {}
        new_product_dict['Name'] = new_product
        new_product_dict['Cost'] = product_price
        products.append(new_product_dict)
        field_names = ['Name', 'Cost']
        append_dict('products.csv', new_product_dict, field_names)
        print("""\033[33m\nYour new product has been created!\033[0m""")
        print(new_product_dict)
        space()
        product_menu()
    
    elif user_input == 3:
        print("""\033[33m\nThe products available are:  \033[0m""")
        for value, key in enumerate(products):
            print(value, key)
            
        number_input = int(
            input("""\033[33m\nEnter the index number of the product you wish to replace: \033[0m"""))
        new_variable = products[number_input]
        update_items(new_variable)

        print("""\033[33m Here's the new updated products menu: ", \033[0m""") 
        pprint(products)
        space()
        product_menu()
        
    elif user_input == 4:
        print("""\033[33m\n\nLets delete a product\033[0m""")
        for key, value in enumerate(products):
                print(key, value)
        deleted_input = int(
            input("""\033[33m\nPlease Select The Number Of The Product You Want To Delete:  \033[0m"""))       
        del products[deleted_input]
        print("""\033[33m\nThe New Product List Is :\033[0m""") 
        pprint(products)
        space()
        product_menu()
        
    else:
        space()
        print ('Please enter a valid option')
        product_menu()

# Courier Menu
def courier_menu():
    print("""\033[33m\nCourier Menu:\033[0m""")
    print('''
[0] - Return to Main Menu
[1] - Courier List
[2] - Create New Courier
[3] - Update Courier
[4] - Delete Courier
                ''')
    user_input = int(input("""\033[33m\nEnter your choice here:  \033[0m"""))

    if user_input == 0:    
        space()
        print('Thanks for visiting!')
        space()
        main_menu()    
    
    elif user_input == 1:
        space()
        pprint(couriers)
        space()
        courier_menu()  
    
    elif user_input == 2:
        space()
        print("""\033[33m\nThe current courier list is: \033[0m""")
        print_csv_file('couriers.csv')
        space()
        new_courier_name = input("What's the name of the new courier?  ")
        new_courier_number = int(input("What is their number:  "))
        new_courier_dict = {}
        new_courier_dict['Name'] = new_courier_name
        new_courier_dict['Number'] = new_courier_number
        couriers.append(new_courier_dict)
        field_names = ['Name','Number']
        append_dict('couriers.csv', new_courier_dict, field_names)
        print("""\033[33m\nYour new courier has been created!\033[0m""")
        print(new_courier_dict)
        space()
        courier_menu()
    
    elif user_input == 3:
        print("""\033[33m\nThe couriers available are:  \033[0m""")
        for key, value in enumerate(couriers):
            print(key, value)
            
        number_input = int(
            input("""\033[33m\nSelect the number of the courier you wish to replace: \033[0m"""))
        new_variable = couriers[number_input]
        update_items(new_variable)

        print("""\033[33m\nHere's the new updated courier menu:  \033[0m""")
        pprint(couriers)
        space()
        courier_menu()  
    
    elif user_input == 4:
        print("""\033[33m\n\nLets delete a courier\033[0m""")
        for key, value in enumerate(couriers):
                print(key, value)
        deleted_input = int(
            input("""\033[33m\nSelect The Number Of The Courier You Wish To Delete : \033[0m"""))       
        del products[deleted_input]
        space()
        print("""\033[33m\nThe New Courier List Is :\033[0m""")
        pprint(couriers)
        space()
        courier_menu()
        
    else:
        space()
        print ('Please enter a valid option')
        courier_menu()  

# Orders Menu
def orders_menu():
    print("""\033[33m\nOrder Menu:\033[0m""")
    print('''
[0] - Return to Main Menu
[1] - View Order
[2] - Enter Details
[3] - Update Order Status  
[4] - Update Existing Order
[5] - Delete Order
''')
    user_input = int(input("""\033[33m\nEnter your choice here: \033[0m"""))
    
    
    if user_input == 0:
        main_menu()
    
    elif user_input == 1:
        space()
        # for order in orders:
        # print(order)
        pprint(orders)
        space()
        orders_menu()
    
    elif user_input == 2:
        customer_name = input("Enter your name: ")
        customer_address = input("Enter your address: ")
        customer_number = int(input("Enter your number: "))
        
        for value, index in enumerate(products):
            print(value, index)
        product_choice = input('Please select your products: ')
        
        for value, index in enumerate(couriers):
            print(value, index)
        courier_choice = int(input('Who would you like to deliver your order:?  '))
        
        entry = {}
        entry ['Customer Name'] = customer_name 
        entry ['Customer Address'] = customer_address
        entry ['Customer Phone Number'] = customer_number
        entry ['Courier'] = courier_choice
        entry ['Status'] = order_status[1]
        entry ['Products'] = product_choice
        
        titles = ['Customer Name', "Customer Address", 'Customer Phone Number','Courier', 'Status', "Products"]
        append_dict('orders.csv', entry, titles)
        
        print('Thank you for your order', entry)
        orders_menu()

    elif user_input == 3:
        for key, value in enumerate(orders):
            print(key, value)

        order_index = int(input("""\033[33m\nPlease select an order to update:   \033[0m"""))
        print('')

        for key, value in enumerate(order_status):
            print(key, value)

        status_input = int(
            input("""\033[33m\nChoose an order status to update on the order list:   \033[0m"""))
        order_to_update = orders[order_index]
        
        order_to_update['Status'] = order_status[status_input]
        print("""\033[33m\nOrder status has been updated\033[0m""")
        pprint(order_to_update)
        
    elif user_input == 4:
        for key, value in enumerate (orders):
            print(key, value)
        order_index = int(input(''' \033[33m\nSelect an order to update:    \033[0m'''))
        updated_order = orders[order_index] 
        old_order = updated_order.copy()
        for key, value in updated_order.items():
            print(key, value)
            chosen_order = input(f'\n{key} is currently {value}. Enter new details for {key}: ')
            if chosen_order == '':
                updated_order[key] = value
                print('\nNothing has been changed')
            else:
                updated_order[key] = chosen_order
        print(f'\n\tYour order has been updated from {old_order} to {updated_order}')
        orders_menu()

        
    elif user_input == 5:
        for key, value in enumerate(orders):
            print(key, value)
        delete_order = int(input('''
        \033[33m\nSelect an order to delete:    \033[0m''')) 
        orders.pop(delete_order)
        print('''
                \033[33m\nOrder was deleted successfully.
                
        Remaining Orders: 
            \033[0m''')
        print(orders)
        space()
        orders_menu()
main_menu()
