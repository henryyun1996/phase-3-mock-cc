class Restaurant:
    all = []

    def __init__(self, name):
        if type(name) == str:
            self._name = name
            Restaurant.all.append(self)
        else:
            raise Exception("Invalid input - please input a restaurant name.")
        self.reviews = []
        self.customers = []

    @property
    def name(self):
        return self._name

    def get_average_rating(self):
        sum = 0

        for review in self.reviews:
            sum += review.rating
        
        average = sum / len(self.reviews)

        return average

    @classmethod
    def get_all_restaurants(cls):
        return cls.all

restaurant = Restaurant("Mels")
restaurant2 = Restaurant("Chipotle")
restaurant3 = Restaurant("Mickey Ds")
print(Restaurant.all)