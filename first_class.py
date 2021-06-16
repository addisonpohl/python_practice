class Car:
    # class variables
    wheels = 4
    doors = 2
    engine = True

    # instance attributes
    def __init__(self, model, year, make="Ford"):
        self.model = model
        self.year = year
        self.make = make
        self.gas = 100
        self.is_moving = False

    def stop(self):
        """Checks if cars is moving and stops car"""
        if self.is_moving:
            print("the car has stopped")
            self.is_moving = False
        else:
            print("The car has already stopped")

    def go(self, speed):
        """Checks if cars is moving and sets speed"""
        if self.use_gas():
            if not self.is_moving:
                print("The car starts moving")
                self.is_moving = True
            print(f"The car is going {speed} MPH")
        else:
            print("You run out of gas")
            self.stop()

    def use_gas(self):
        """Determines the car has gas or not"""
        self.gas -= 50
        if self.gas >= 0:
            return False
        else:
            return True


car_one = Car("Camry", 2011, "Toyota")
car_two = Car("Model T", 1908)
