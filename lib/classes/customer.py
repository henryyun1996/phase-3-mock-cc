class Customer:

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.reviews = []
        self.restaurants = []

    # @property
    # def first_name(self):
    #     return self._first_name
    
    # @first_name.setter
    # def first_name(self, first_name):
    #     if type(first_name) == str and (len(first_name) > 0 and len(first_name) < 26):
    #         self._first_name = first_name
    #     else:
    #         # print("Please input a name between 1 and 25 characters!")

    #         raise Exception("Please input a name between 1 and 25 characters!")

    def get_first_name(self):
        return self._first_name

    def set_first_name(self, first_name):
        if type(first_name) == str and ( len(first_name) > 0 and len(first_name) < 26 ):
            self._first_name = first_name
        else: 
            raise Exception("Please input a name between 1 and 25 characters!")
    
    first_name = property(get_first_name, set_first_name)

    # @property
    # def last_name(self):
    #     return self._last_name

    # @last_name.setter
    # def last_name(self, last_name):
    #     if type(last_name) == str and (len(last_name) > 0 and len(last_name) < 26):
    #         self.last_name = last_name
    #     else:
    #         # print("Please input a name between 1 and 25 characters!")

    #         raise Exception("Please input a name between 1 and 25 characters!")

    def get_last_name(self):
        return self._last_name

    def set_last_name(self, last_name):
        if type(last_name) == str and (len(last_name) > 0 and len(last_name) < 26):
            self._last_name = last_name
        else:
            raise Exception("Please input a name between 1 and 25 characters!")
        
    last_name = property(get_last_name, set_last_name)

    def get_full_name(self):
        return (f"{self._first_name} {self._last_name}")

    def get_num_reviews(self):
        return len(self.reviews)

    def add_review(self, restaurant, rating):
        # This prevents a circular import!
        # Don't worry about it right now, but check it out when you have the time!
        from classes.review import Review
        Review(self, restaurant, rating)

steve = Customer("Steve", "Wayne")
print(steve.get_full_name())