
class OrderDetails:
    # this class would take user information and put it in an order database
    def __init__(self, customer, items, address, email):
        self.customer = customer
        self.items = items
        self.address = address
        self.email = email

    def storeInformation(self):
        print("Connected to database.")
        # insert into table of orders specifying address, customer name, items they ordered
        print("User information succesfully stored.")

class CalculateOrderCost:
    def __init__(self, customerItems, discountCode=None):
        self.discountCode = discountCode
        self.customerItems = customerItems
        self.taxRate = .0625
        self.grossTotal = 0.00
    
    def confirmDiscount(self):
        # connects to database, checks if the code exists, grabs the discount % it should apply and returns it
        # originally had a dummy sql db conn but thought it was better just to have the code runnable and print connect to db instead
        print("Connected to database!")
        # self.query = "SELECT discountAmount from discountTable WHERE discountCode = %s"
        # in an actual implementation, I would assume that there would be a database full of coupon codes and this function would compare their code to the ones in the db
        # instead, for this, I initalize an array and just compare the discountCode to the array

        couponCodes = ["free code!", 43579435] # mock db
        self.couponExists = False

        for eachCode in couponCodes:
            if self.discountCode == eachCode:
                self.couponExists = True
        
        if (self.couponExists):
            # code exists, apply 5% discount
            self.discountAmount = .05
            return self.discountAmount
        else:
            # code does not exist / is not entered
            self.discountAmount = 0.00
            return self.discountAmount
    
    def getItemPrices(self):
        #this function would check the item database for each item's prices. In an actual implementation, it would connect to the item database
        #and get the price where the item name is. For example, it would search for "Adidas Socks," and find the price of 7.99. Instead, I will
        #use an array as a mock db instead for this example.
        itemDatabase = ["Socks", "Shoes"]
        for itemInDB in itemDatabase:
            for purchasedItem in self.customerItems:
                if (itemInDB == purchasedItem):
                    self.grossTotal = self.grossTotal + 7.99


    def calculateOrderTotal(self) -> int:
        # calculate order total using grossTotal, possible discount, and tax rate
        if (self.discountAmount):
            self.total = self.grossTotal + (self.taxRate * self.grossTotal) - (self.grossTotal * self.discountAmount)
            return round(self.total, 2)
        else:
            self.total = self.grossTotal + (self.taxRate * self.grossTotal)
            return round(self.total, 2)
        
class OrderValidation:
        def __init__(self, buyer: OrderDetails):
            self.address = buyer.address
            self.items = buyer.items
        
        def verifyAddress(self):
            # use some sort of address matching to figure out if the address is a valid address
            addressValid = True
            if (addressValid):
                print(f"{self.address} is a valid address.")
            else:
                print(f"{self.address} is not a valid address.")
        
        def verifyStock(self):
            # search the stock database with each item one by one and check if their stock is >= to the amount purchased
            # (ex// if purchased two socks, check if stock is >= 2)
            print("Checking if items are in stock...")
            # this is where the database would be checked... the items purchased would be totalled of their quantity and then compared to the quantity in stock
            print("All items are in stock!")

class UpdateInventory:
    # after a purchase is successfully completed (verified + confirmation email sent), check what the user bought, total the quantity of each item
    # and decrement it as much as needed. On paper, this should work similarly to verifyStock() except the value of stock is being changed.
    def __init__(self, buyer: OrderDetails):
        self.items = buyer.items
    
    def updateStock(self):
        print("Item stock succesfully updated.")


class OrderConfirmation:
    def __init__(self, buyer: OrderDetails, orderTotal):
        self.customer = buyer.customer
        self.address = buyer.address
        self.email = buyer.email
        self.orderTotal = orderTotal
        
    def confirmationMessage(self):
        # print here, but this would email a confirmation message with these details
        print(f"TO {self.email}: Dear {self.customer}, Your order with total ${self.orderTotal} has successfully been confirmed and will be shipped to {self.address} within 7 days. Thank you! ")


def main():
    customerName = "Chase Poindexter"
    itemsPurchased = ["Socks", "Shoes"]
    address = "205 Stupendous Drive"
    email = "placeholder@gmail.com"
    
    # creates a customer object that stores their username, items purchased, address
    customer = OrderDetails(customerName, itemsPurchased, address, email)

    # verify stock and address
    customerOrderValidation = OrderValidation(customer)
    customerOrderValidation.verifyAddress()
    customerOrderValidation.verifyStock()

    # calculates the customer's order cost
    customerOrderCostDetails = CalculateOrderCost(customer.items)
    customerOrderCostDetails.confirmDiscount()
    customerOrderCostDetails.getItemPrices()
    customerOrderTotal = customerOrderCostDetails.calculateOrderTotal()

    # this typically wouldn't print but instead email, but for testing sake it is just a print statement
    customerOrderConfirm = OrderConfirmation(customer, customerOrderTotal)
    customerOrderConfirm.confirmationMessage()

    # finally, update the stock to reflect the purchases
    customerUpdateInventory = UpdateInventory(customer)  
    customerUpdateInventory.updateStock()  

if __name__ == "__main__":
    main()
    


    
        

