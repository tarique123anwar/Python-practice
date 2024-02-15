#///////////////////////////////////////// 
# class bikeShop:
#     def __init__(self,stock):# This is a Constructor (__init__)
#         self.stock=stock
#     def displayBike(self):
#         print("Total Bike",self.stock)
#     def rentForBike(self,q):
#         if q<=0:
#             print("Enter the positive Value or greater than zero")
#         elif q>self.stock:
#                  print("Enter the Value (less than stock)")
#         else:
#             self.stock=self.stock-q
#             print("Total prices",q*100)
#             print("Total Bikes",self.stock)
# while True:
#     obj=bikeShop(100)
#     uc=int(input('''
# 1 Display Stocks
# 2 Rent a Bike 
# 3 Exit
#         '''))
#     if uc==1:
#         obj.displayBike()
#     elif uc==2:
#         n=int(input("Enter the Qty:----"))
#         obj.rentForBike(n)
#     else:
#         break

#//////////////////////////////////////////////////////////
    
# class c:
#     def __init__(self,s):
#         self.s=s
#     def dis(self):
#         print("Total Cars",self.s)
#     def renfcar(self,q):
#         try:
#             q=int(q)
#         except ValueError:
#             print("Please enter a valid integer.")
#             return
#         try:
#             if q<=0:
#                 print("Enter the v (greater than zero)")
#             elif q>self.s:
#                 print("Enter the v (less than stock)")
#             else:
#                 t=q*133
#                 self.s=self.s-q
#                 print("Total prices",t)
#                 print("Total Cars available ",self.s)
#         except Exception as e:
#             print(f"An unexpected error occurred: {str(e)}")
# while True:
#     o=c(133)
#     u=int(input('''
# 1---> Display Stocks
# 2---> Rent a Cars
# 3---> Exit.
#         '''))
#     if u==1:
#         o.dis()
#     elif u==2:
#         i=int(input("Enter the Qty:----"))
#         o.renfcar(i)
#     elif u==3:
#         pass
#     else:
#          print("Invalid choice. Please enter 1, 2, or 3.")

#//////////////////////////////////////////

# class Car:
#     def __init__(self, stock):
#         self.stock = stock

#     def display_stock(self):
#         print("Total Cars:", self.stock)

#     def rent_car(self, quantity):
#         try:
#             quantity = int(quantity)
#         except ValueError:
#             print("Please enter a valid integer for quantity.")
#             return

#         try:
#             if quantity <= 0:
#                 print("Enter a quantity greater than zero.")
#             elif quantity > self.stock:
#                 print("Enter a quantity less than or equal to stock.")
#             else:
#                 total_price = quantity * 133
#                 self.stock -= quantity
#                 print("Total price:", total_price)
#                 print("Remaining Cars:", self.stock)
#         except Exception as e:
#             print(f"An unexpected error occurred: {str(e)}")

# # Create an instance of the Car class outside the loop
# car_instance = Car(133)

# while True:
#     user_choice = input('''
# 1---> Display Stocks
# 2---> Rent a Car
# 3---> Exit
# Enter your choice: ''')

#     if user_choice == '1':
#         car_instance.display_stock()
#     elif user_choice == '2':
#         qty = input("Enter the Qty: ")
#         car_instance.rent_car(qty)
#     elif user_choice == '3':
#         pass
#     else:
#         print("Invalid choice. Please enter 1, 2, or 3.")

#/////////////////////////////////////////////////////////////////

class CarInventory:
    def __init__(self, stock):
        self.stock = stock

    def display_stock(self):
        print("Total Cars:", self.stock)

    def rent_car(self, quantity):
        try:
            quantity = int(quantity)
        except ValueError:
            print("Please enter a valid integer.")
            return

        try:
            if quantity <= 0:
                print("Enter a quantity greater than zero.")
            elif quantity > self.stock:
                print("Enter a quantity less than or equal to stock.")
            else:
                total_price = quantity * 133
                self.stock -= quantity
                print("Total prices", total_price)
                print("Total Cars available ", self.stock)
        except Exception as e:
            print(f"An unexpected error occurred: {str(e)}")

# Main loop
while True:
    car_inventory = CarInventory(133)
    user_choice = input('''
1---> Display Stocks
2---> Rent a Car
3---> Exit
Enter your choice: ''')

    if user_choice == '1':
        car_inventory.display_stock()
    elif user_choice == '2':
        quantity = input("Enter the Qty: ")
        car_inventory.rent_car(quantity)
    elif user_choice == '3':
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")

import sqlite3
con=sqlite3.connect("database.db")
con.execute('''
        
''')