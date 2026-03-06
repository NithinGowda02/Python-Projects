#Car Class
class Car:  
    next_id = 1
    def __init__(self, brand, model, price_per_day):
        self.car_id = Car.next_id
        Car.next_id += 1
        self.brand = brand
        self.model = model
        self.price_per_day = price_per_day
        self.is_available = True

    def display_info(self):
        status = "Available" if self.is_available else "Rented"
        print(f"ID: {self.car_id} | {self.brand} | {self.model} | Price/day: {self.price_per_day} | {status}")

#class customer
class Customer:
    next_id = 1
    def __init__(self, name, phone, license_number):
        self.customer_id = Customer.next_id
        Customer.next_id += 1
        self.name = name
        self.phone = phone
        self.license_number = license_number

    def display_customer(self):
        print(f"Customer_ID : {self.customer_id} | Name : {self.name} | Phone Number : {self.phone} | License Number : {self.license_number}")

#class Rental 
class Rental:
    def __init__(self, rental_id, customer, car, days):
        self.rental_id = rental_id
        self.customer = customer
        self.car = car
        self.days = days
        self.total_price = self.calculate_price()

    def calculate_price(self):
        return self.car.price_per_day * self.days

    def display_rental(self):
        print(f"Rental_ID : {self.rental_id}")
        print(f"Customer : ", end="")
        self.customer.display_customer()
        print(f"Car : ", end="")
        self.car.display_info()
        print(f"Days : {self.days}")
        print(f"Total Price : {self.total_price}")

#class CarRentalSystem        

class CarRentalSystem:
    def __init__(self):
        self.cars = []
        self.customers = []
        self.rentals = []

    def add_car(self, car):
        self.cars.append(car)

    def add_customer(self, customer):
        self.customers.append(customer)  

    def show_available_car(self):
        if len(self.cars) == 0:
            print("No Cars Are Availaible First Add Cars [1: Add Cars]")
        for car in self.cars:
            if car.is_available:
                car.display_info()                

    def show_customer(self):
        if len(self.customers) == 0:
            print("Register To Enjoy The Services [2.Register Customer]")
        for customer in self.customers:
                customer.display_customer()                           

    def rent_car(self):
        car_id = int(input("Enter the Car ID : "))
        customer_id = int(input("Enter the Customer ID : "))
        days = int(input("Enter the Number of days : "))

        car = None
        customer = None 

        for c in self.cars:
            if c.car_id == car_id and c.is_available:
                car = c
                break

        for cust in self.customers:
            if cust.customer_id == customer_id:
                customer = cust
                break

        if car and customer:
            rental_id = len(self.rentals) + 1
            rental = Rental(rental_id, customer, car, days) 
            self.rentals.append(rental)
            car.is_available = False
            print("\n Car Rented Successfully! ")
            rental.display_rental()
        else:
            print("Car not available or customer Not found.")               

    def return_car(self):
        car_id = int(input("Enter the Car ID to return : "))

        for car in self.cars:
            if car.car_id == car_id:
                car.is_available = True
                print("Car Returned Successfully!")
                return
        print("Car Not Found")    

def main():
    system = CarRentalSystem()     

    while True:
        print("\n*******************************************")
        print("\n============ CAR RENTAL SYSTEM ============") 
        print("\n*******************************************")
        
        print("1. Add Cars ")
        print("2. Register Customers")
        print("3. Show Available Cars ")
        print("4. Show Registered Customers")
        print("5. Rent Car ")
        print("6. Return Car ")
        print("7. Exit ")

        choice = int(input("Enter your choice >> "))
        
        if choice == 1:
            brand = input("Enter the car brand >> ")
            model = input("Enter the Car model >> ")
            price_per_day = int(input("Enter the Car Rental Price Per Day >> "))
            system.add_car(Car(brand, model, price_per_day))
            print("Car Added Successfully.!")
            
            
        elif choice == 2:
            name = input("Enter the Customer Name >> ")
            phone = input("Enter the Phone Number >> ")
            license_number = input("Enter the Driving License Number >> ")
            system.add_customer(Customer(name, phone, license_number))
            print("Customer Added Successfully.!")

        elif choice == 3:
            system.show_available_car()

        elif choice == 4:
            system.show_customer()

        elif choice == 5:
            system.rent_car()

        elif choice == 6:
            system.return_car()

        elif choice == 7:
            break                

        else:
            print("Invalid Choice")

if __name__ == "__main__":
    main()                    


