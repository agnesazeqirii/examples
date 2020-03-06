class Person:

    species='njeri'

    def __init__(self,first_name,last_name,birthdate,email):
        self.first_name=first_name
        self.last_name=last_name
        self.birthdate=birthdate
        self.email=email

    def eat(self,food):
        return "{} eats {} ".format(self.first_name,food)
    
    def sleep(self,hours):
        return "{} sleeps {} hours".format(self.first_name,hours)
    
    def walks(self,km):
        return "{} waalks {} km".format(self.first_name,km)
