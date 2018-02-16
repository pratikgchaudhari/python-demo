class User(object):
    """An attempt to model user"""

    def __init__(self,first_name,last_name,date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth

    def describe_user(self):
        return (self.first_name + ' ' + self.last_name).title() + ' was born on ' + self.date_of_birth

    def greet_user(self):
        return 'Hi, ' + (self.first_name + ' ' + self.last_name).title()