'''
Movie suggestions - based on some conditions
'''
movie_y_n = input("Do you want to watch movie? Y/N: ")
if movie_y_n.lower() == 'y' or 'yes':
    select_genre = input("Select a genre for my recommendations: comedy/ other ")
    if select_genre.lower() == 'comedy':
        print("Watch the Hangover Trilogy")
    else:
        print("Watch Top Gun! Either Maverick or the 1990s classic")
else:
    print("Watch a TV series instead. I'd recommend the 3 Body Problem. ")

 
'''
Hotel suggestions - based on some conditions
'''
hotel_y_n = input("Do you want a hotel or resort?: ")
if hotel_y_n.lower() == 'resort':
    max_price = int(input("What's the max price for your budget?: $"))
    if max_price >= 350:
        print("Book 6 senses resort")
    else:
        print("Book 4 seasons hotel")
else:
    print("Go to the nearest Hilton.")

'''
Prices based on products and corresponding discounts
'''
product_one_price = int(input("Price of product 1: "))
product_two_price = int(input("Price of product 2: "))
product_three_price = int(input("Price of product 3: "))

total = (product_one_price + product_two_price + product_three_price)

if max(product_one_price, product_two_price, product_three_price ) == product_one_price:
    total = total * 0.34
    print(f"You got 66% off, and your new price is {total}")
elif max(product_one_price, product_two_price, product_three_price ) == product_three_price:
    total = total * 0.5
    print(f"You got 50% off, and your new price is {total}")
else:
    print(f"Total price is {total}")
    