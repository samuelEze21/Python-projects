class Bike:

    def __init__(self):
        self.ignition_is_on = False
        self.starting_speed = 0



    def turn_bike_on(self):
        if not self.ignition_is_on:
            self.ignition_is_on = True
            print("Your Bike is Turned On Now, press gear to accelerate")
        return self.ignition_is_on


    def turn_bike_off(self):
        if self.ignition_is_on:
            self.ignition_is_on = False
            print("Power off")
        return not self.ignition_is_on



    def get_gear_level(self, gear_level):
        if gear_level == 1:
            self.bike_speed = (0 - 20)

        elif gear_level == 2:
            self.bike_speed = (21 - 30)

        elif gear_level == 3:
            self.bike_speed = (31 - 40)

        elif gear_level == 4:
            self.bike_speed = (41 - 60)

            return gear_level

        else:
            print("Speed limit not supported")



    def accelerate_gear_levels(self, gear_level):
        if not self.ignition_is_on:
            print("Bike is off. Turn it on first!")
            return None

        if gear_level == 1:
            self.bike_speed += 1

        elif gear_level == 2:
            self.bike_speed += 2

        elif gear_level == 3:
            self.bike_speed += 3

        elif gear_level == 4:
            self.bike_speed += 4

        else:
            print("Invalid gear level")

        return self.bike_speed



    def decelerate_gear_levels(self, gear_level):
        if not self.ignition_is_on:
            print("Bike is off. Turn it on first!")
            return None

        if gear_level == 1:
            self.bike_speed -= 1

        elif gear_level == 2:
            self.bike_speed -= 2

        elif gear_level == 3:
            self.bike_speed -= 3

        elif gear_level == 4:
            self.bike_speed -= 4

        else:
            print("Invalid gear level")

        return self.bike_speed




