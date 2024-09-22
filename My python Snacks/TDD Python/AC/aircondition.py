class AirCondition:

    def __init__(self, is_power_on):
        self.is_power_on = is_power_on



def turn_on_ac(is_power_on, temperature):
    if is_power_on and temperature >= 24: # check to see if power is on and temperature is active
        return True


def turn_off_ac(power_off, temperature):
    if power_off and temperature < 0:
        return False


def increase_temperature(temperature, decrease_cooling):

    ac_on = True

    for temperature in range(16, 30):
        temperature += temperature
        for decrease_cooling in range(10):
            decrease_cooling -= 1

    return temperature, decrease_cooling


def decrease_temperature(temperature, increase_cooling):

    ac_on = True

    for temperature in range(24, 16):
        temperature -= temperature
        for increase_cooling in range(10):
            increase_cooling += 1

    return temperature, increase_cooling



