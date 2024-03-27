

def main():
      discount_code_check(discount_programme())
      

'''
Discount programme if business trip and price of trip is greater than 1200$
'''

def discount_programme():
      trip_type = input("What type of trip? Business or Non-Business?: ")
      trip_cost = int(input("Expected trip cost: "))
      
      if trip_type.lower() == "business" and trip_cost >= 1200:
            print("You get a discount!")
            return trip_cost
      else:
            print("Sorry! No discount for your trip.")

'''
Discount programme if special code winter23 is given, give them 20% off. 
'''

def discount_code_check(cost):
      code_entered = input("Enter your discount count: ")
      if code_entered.lower() == "winter23":
            discounted_price = cost * 0.80
            print(f"Discount code valid. New price: ${discounted_price}")
            return discounted_price
      else:
            print("Invalid discount, try again.")
            



if __name__ == "__main__":
      main()