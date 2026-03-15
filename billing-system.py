class Shoping_cart:

    def __init__(self):
        self.cart = {}

    def add_item(self):
        item = input("Enter Item name:")

        try:
            price = float(input("Enter price : "))
            quantity = int(input("Enter Quantity : "))
        except ValueError:
            print("Enter a valid input ")
            return
        
        if item in self.cart:
            self.cart[item]["qty"] += quantity

        else:
            self.cart[item] = {"price" : price, "qty" : quantity}

        print(f"{item} added to cart")

    def remove_item(self):
        item = input("Enter item to remove : ")

        if item in self.cart:
            del self.cart[item]
            print("Item removed")
        else:
            print("Item not found")
            print("No items removed") 

    def view_cart(self):
        if not self.cart:
            print("Cart is empty")
            return
        
        print("\n------ YOUR CART ------")

        total = 0

        for item,data in self.cart.items():
            subtotal = data["price"] * data["qty"]
            total += subtotal
            print(f"{item} ({data["qty"]}) - ${subtotal:.2f} ")

        tax = total * 0.05
        final_total = total + tax

        
        print("------------------------")
        print(f"Subtotal: ${total:.2f}")
        print(f"Tax (5%): ${tax:.2f}")
        print(f"Total: ${final_total:.2f}")


    def run(self):
        while True:

            print("\n1. Add Item")
            print("2. Remove Item")
            print("3. View Cart")
            print("4. Exit")

            choice = input("Select option : ")

            if choice == "1":
                self.add_item()

            elif choice == "2":
                self.remove_item()

            elif choice == "3":
                self.view_cart()

            elif choice == "4":
                print("Thank you for shopping.")
                break

            else:
                print("Enter a valid option ")

cart = Shoping_cart()
cart.run()