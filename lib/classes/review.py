from classes.customer import Customer
from classes.restaurant import Restaurant

class Review:
    
    def __init__(self, customer, restaurant, rating):
        self.customer = customer
        self.restaurant = restaurant
        self.rating = rating

        self.add_customer_to_restaurant()
        self.add_restaurant_to_customer()
        self.add_review_to_customer()
        self.add_review_to_restaurant()

    def get_customer(self):
        return self._customer
    
    def set_customer(self, customer):
        if isinstance(customer, Customer):
            self._customer = customer
        else:
            raise Exception("Customer is not an instance of class Customer.")
    
    customer = property(get_customer, set_customer)
 
    # def restaurant(self):
    #     # restaurant property goes here!
    #     pass

    def get_restaurant(self):
        return self._restaurant
    
    def set_restaurant(self, restaurant):
        if isinstance(restaurant, Restaurant):
            self._restaurant = restaurant
        else:
            raise Exception("Restaurant is not an instance of class Restaurant.")
    
    restaurant = property(get_restaurant, set_restaurant)

    def get_rating(self):
        return self._rating
    
    def set_rating(self, rating):
        if rating > 0 and rating < 6:
            self._rating = rating
        else:
            raise Exception("Rating must be a number between 1 and 5.")

    rating = property(get_rating, set_rating)

    def add_customer_to_restaurant(self):
        if self._customer not in self._restaurant.customers:
            self._restaurant.customers.append(self._customer)

    def add_review_to_restaurant(self):
        self._restaurant.reviews.append(self)

    def add_restaurant_to_customer(self):
        if self._restaurant not in self._customer.restaurants:
            self._customer.restaurants.append(self._restaurant)

    def add_review_to_customer(self):
        self._customer.reviews.append(self)
