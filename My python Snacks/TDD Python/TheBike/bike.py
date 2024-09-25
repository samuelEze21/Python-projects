class Bike:

    def __init__(self, ignition_is_on, starting_speed):
        self.ignition_isOn = ignition_is_on
        self.starting_speed = starting_speed


def turn_bike_on(self, ignition_is_on):
    if ignition_is_on:
        return True
    print("Your Bike is Turned On Now, press gear to accelerate")



def turn_bike_off(self, ignition_is_off):
    if ignition_is_off:
        return True
    print("power_off")


def get_gear_level(self, gear_level):
    if gear_level == "gear_1":
        self.bike_speed = (0-20)

    elif gear_level == "gear_2":
        self.bike_speed = (21-30)

    elif gear_level == "gear_3":
        self.bike_speed = 31-40

    elif gear_level == "gear_4":
        self.bike_speed = 41-60
        return gear_level

    else:
        print("Speed limit not supported")


def accelerate_gear1(self, ignition_is_on, gear_level, bike_speed):
    gear_level_to_speed_limit = {
        "gear_1": (0, 20),

    }

    if ignition_is_on:
        for bike_speed in gear_level_to_speed_limit[gear_level]:
            if gear_level == "gear_1":
                bike_speed += 1
                return bike_speed


def accelerate_gear2(self, ignition_is_on, gear_level, bike_speed):
    gear_level_to_speed_limit = {
        "gear_1": (0, 20),
        "gear_2": (21, 30),
    }

    if ignition_is_on:
        for bike_speed in gear_level_to_speed_limit[gear_level]:
            if gear_level == "gear_2":
                bike_speed += 2
                return bike_speed

    return None


def accelerate_gear3(self, ignition_is_on, gear_level, bike_speed):
    gear_level_to_speed_limit = {
        "gear_1": (0, 20),
        "gear_2": (21, 30),
        "gear_3": (31, 40),
    }

    if ignition_is_on:
        for bike_speed in gear_level_to_speed_limit[gear_level]:
            if gear_level == "gear_3":
                bike_speed += 3
                return bike_speed

    return None


def accelerate_gear4(self, ignition_is_on, gear_level, bike_speed):
    gear_level_to_speed_limit = {
        "gear_1": (0, 20),
        "gear_2": (21, 30),
        "gear_3": (31, 40),
        "gear_4": (41, 50),
    }

    if ignition_is_on:
        for bike_speed in gear_level_to_speed_limit[gear_level]:
            if gear_level == "gear_4":
                bike_speed += 4
                return bike_speed

    return None