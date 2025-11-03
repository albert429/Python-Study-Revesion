# #Question 1:
# class Vehicle:
#     total_vehicles = 0  # Class variable to track all vehicles

#     def __init__(self, vehicle_id, brand, model, rental_price_per_day, is_rented=False):
#         self.vehicle_id = vehicle_id
#         self.brand = brand
#         self.model = model
#         self.rental_price_per_day = rental_price_per_day
#         self.is_rented = is_rented
#         Vehicle.total_vehicles += 1

#     def rent(self):
#         if not self.is_rented:
#             self.is_rented = True

#     def return_vehicle(self):
#         if self.is_rented:
#             self.is_rented = False

#     def calculate_rental_cost(self, days):
#         return self.rental_price_per_day * days
    
#     def get_details(self):
#         status = "Rented" if self.is_rented else "Available"
#         return f"ID: {self.vehicle_id}, Brand: {self.brand}, Model: {self.model}, Yearly Price: {self.rental_year_price}, Status: {status}"
    
# class Car(Vehicle):
#     def __init__(self, vehicle_id, brand, model, rental_price_per_day, num_doors=4):
#         super().__init__(vehicle_id, brand, model, rental_price_per_day)
#         self.num_doors = num_doors
    
#     def get_details(self):
#         base_details = super().get_details()
#         return f"{base_details}\nNumber of Doors: {self.num_doors}\nType: Car"


# class Motorcycle(Vehicle):
#     def __init__(self, vehicle_id, brand, model, rental_price_per_day, engine_cc=500):
#         super().__init__(vehicle_id, brand, model, rental_price_per_day)
#         self.engine_cc=engine_cc

#     def calculate_rental_cost(self, days):
#         base_cost = super().calculate_rental_cost(days)
#         return base_cost * 0.7
    
#     def get_details(self):
#         base_details = super().get_details()
#         return f"{base_details}\nEngine: {self.engine_cc}cc\nType: Motorcycle"

        

# class Truck(Vehicle):
#     def __init__(self, vehicle_id, brand, model, rental_price_per_day, cargo_capacity_tons=5):
#         super().__init__(vehicle_id, brand, model, rental_price_per_day)
#         self.cargo_capacity_tons = cargo_capacity_tons

#     def calculate_rental_cost(self, days):
#         base_cost = super().calculate_rental_cost(days)
#         return base_cost * 1.5
    
#     def get_details(self):
#         base_details = super().get_details()
#         return f"{base_details}\nCargo Capacity: {self.cargo_capacity_tons} tons\nType: Truck"

# # Example usage:
# if __name__ == "__main__":
#     car = Car("V001", "Toyota", "Camry", 50, 4)
#     motorcycle = Motorcycle("V002", "Harley", "Street 750", 40, 750)
#     truck = Truck("V003", "Ford", "F-150", 80, 2.5)

#     car.rent()
#     print(car.is_rented)

#     cost = car.calculate_rental_cost(5)
#     print(f"Rental cost for 5 days: {cost}")

#     print(f"Total vehicles: {Vehicle.total_vehicles}")  

#====================================================================================================================



# # Question 2:
# class CustomRange:
#     def __init__(self, start, end=None, step=1):
#         if end is None:
#             self.start = 0
#             self.end = start
#         else:
#             self.start = start
#             self.end = end
#         self.step = step

#     def __iter__(self):
#         self.current = self.start
#         return self

#     def __next__(self):
#         if (self.step > 0 and self.current >= self.end) or (self.step < 0 and self.current <= self.end):
#             raise StopIteration
#         else:
#             value = self.current
#             self.current += self.step
#             return value
    
#     def reset(self):
#         self.current = self.start

# class EvenNumbers(CustomRange):
#     def __init__(self,start, end):
#         super().__init__(start, end)
#         self.step=2
    
#     def __iter__(self):
#         if self.start % 2 != 0:
#             self.current = self.start + 1
#         else:
#             self.current = self.start
#         return self

# if __name__ == "__main__":
#     for num in EvenNumbers(1, 20):     
#         print(num, end=" ")


#====================================================================================================================
# # Question 3:

# def read_file_lines(filename):
#     with open(filename, 'r') as file:
#         for line in file:
#             yield line

# def filter_lines(lines, keyword):
#     for line in lines:
#         words = line.split()
#         if keyword in words:
#             yield line

# def strip_lines(lines):
#     for line in lines:
#         yield line.strip()

# def number_lines(lines):
#     line_number = 1
#     for line in lines:
#         yield f"{line_number}: {line}"
#         line_number += 1

# def chunk_lines(lines, chunk_size):
#     chunk = []
#     for line in lines:
#         chunk.append(line)
#         if len(chunk) == chunk_size:
#             yield chunk
#             chunk = []
#     if chunk:
#         yield chunk

# if __name__ == "__main__":
#     lines = read_file_lines("contacts.csv")
#     filtered = filter_lines(lines, "Alice")
#     stripped = strip_lines(filtered)
#     numbered = number_lines(stripped)
#     for number in numbered:
#         print(number)


#====================================================================================================================
# Question 4:

import time
import functools

def timer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"[TIMER] Function '{func.__name__}' executed in {execution_time:.4f} seconds")
        return result
    return wrapper

def logger(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_str = ', '.join([repr(arg) for arg in args])
        kwargs_str = ', '.join([f"{k}={repr(v)}" for k, v in kwargs.items()])
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        
        print(f"[LOGGER] Calling function '{func.__name__}' with args=({all_args})")
        result = func(*args, **kwargs)
        print(f"[LOGGER] Function '{func.__name__}' returned: {repr(result)}")
        return result
    return wrapper

def count_calls(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        wrapper.count += 1
        result = func(*args, **kwargs)
        return result
    wrapper.count = 0
    return wrapper

def debug(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        args_repr = [repr(arg) for arg in args]
        kwargs_repr = [f"{k}={repr(v)}" for k, v in kwargs.items()]
        signature = ', '.join(args_repr + kwargs_repr)
        
        print(f"[DEBUG] Calling '{func.__name__}' with arguments: {signature}")
        result = func(*args, **kwargs)
        print(f"[DEBUG] '{func.__name__}' returned: {repr(result)}")
        return result
    return wrapper

#Test:
#main


#=================================================================================
#Question 5:
class Product:
    
    def __init__(self, product_id, name, price, stock, category):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category
    
    def add_stock(self, amount):
        self.stock += amount
    
    def reduce_stock(self, amount):
        if self.stock >= amount:
            self.stock -= amount
            return True
        return False
    
    def apply_discount(self, percentage):
        discount = self.price * (percentage / 100)
        self.price = self.price - discount
    
    @property
    def is_available(self):
        return self.stock > 0
    
    def __str__(self):
        return f"{self.name} ({self.product_id}) - ${self.price} - Stock: {self.stock}"
    
    def __repr__(self):
        return f"Product({self.product_id}, {self.name}, ${self.price})"
    
    def __eq__(self, other):
        return self.product_id == other.product_id
    
    def __hash__(self):
        return hash(self.product_id)


class Review:
    
    def __init__(self, user, rating, comment):
        self.user = user
        self.rating = rating
        self.comment = comment
    
    def is_positive(self):
        return self.rating >= 4


class ProductWithReviews(Product):
    
    def __init__(self, product_id, name, price, stock, category):
        super().__init__(product_id, name, price, stock, category)
        self.reviews = []
    
    def add_review(self, review):
        self.reviews.append(review)
    
    def average_rating(self):
        if len(self.reviews) == 0:
            return 0
        
        total = 0
        for review in self.reviews:
            total += review.rating
        
        return total / len(self.reviews)
    
    def get_review_summary(self):
        if len(self.reviews) == 0:
            return "No reviews"
        
        avg = self.average_rating()
        
        positive_count = 0
        for review in self.reviews:
            if review.is_positive():
                positive_count += 1
        
        return f"{len(self.reviews)} reviews - Average: {avg}/5 - {positive_count} positive"


class ShoppingCart:
    
    def __init__(self):
        self.items = {}
    
    def add_item(self, product, quantity=1):
        if product in self.items:
            self.items[product] += quantity
        else:
            self.items[product] = quantity
    
    def remove_item(self, product):
        if product in self.items:
            del self.items[product]
    
    def update_quantity(self, product, new_quantity):
        if product in self.items:
            self.items[product] = new_quantity
    
    def get_total(self):
        total = 0
        for product, quantity in self.items.items():
            total += product.price * quantity
        return total
    
    def clear(self):
        self.items = {}
    
    def __len__(self):
        total_items = 0
        for quantity in self.items.values():
            total_items += quantity
        return total_items
