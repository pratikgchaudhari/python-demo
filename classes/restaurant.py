class Restaurant(object):
    """An attempt to model a restaurant"""
    
    def __init__(self,restaurant_name,cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    
    def describe_restaurant(self):
        return self.restaurant_name + ' serves ' + self.cuisine_type
    
    def open_restaurant(self):
        return self.restaurant_name + ' is now open'