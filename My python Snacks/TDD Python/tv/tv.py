class Tv:

    def __init__(self):
        # self.current_volume = None
        self.is_on = False
        self.channel: int = 1
        self.volume: int = 0


    def __get_is_on(self):
        return self.is_on

    def get_is_on(self):
        return self.__get_is_on()


    def turn_tv_on(self):
        self.is_on = True

    def turn_tv_off(self):
        self.is_on = False


    def get_tv_channel(self, channel: int):
        if self.is_on:
            self.channel = channel
            return self.channel

        else:
            raise ValueError("Tv is off")



    def set_tv_channel(self, channel: int):
        if self.is_on:
            if channel <= 0 or channel > 100:
                raise ValueError("invalid channel")

            if channel < 100:
                self.channel = channel
                return self.channel

        else:
            raise ValueError("Tv is off")


    def get_tv_volume(self, volume):
        if self.is_on:
            self.volume = volume
            return self.volume



    def set_tv_volume(self, volume):
        if self.is_on:
            if volume <= 0 or volume > 10:
                raise ValueError("invalid volume")

            self.volume = volume
            return self.volume

        else:
            raise ValueError("Tv is off")



    def set_tv_channel_up(self, current_channel):
        if self.is_on:
            if current_channel <= 0 or current_channel > 100:
                raise ValueError("invalid channel. Channel must be between 1 and 100")

            if current_channel < 100:
                self.channel = current_channel + 1
            else:
                self.channel = current_channel
            return self.channel

        else:
            raise ValueError("Tv is off")



    def set_tv_channel_down(self, current_channel):
        if self.is_on:
            if current_channel <=0 or current_channel > 100:
                raise ValueError("invalid channel. Channel must be between 1 and 100")

            if current_channel < 100:
                self.channel = current_channel - 1

            else:
                self.channel = current_channel
            return self.channel

        else:
            raise ValueError("Tv is off")



    def set_tv_volume_up(self, current_volume):
        if self.is_on:
            if current_volume <= 0 or current_volume > 10:
                raise ValueError("invalid volume. Volume must be between 1 and 10")

            if current_volume < 10:
                self.volume = current_volume + 1
                return self.volume

        else:
            raise ValueError("Tv is off")



    def set_tv_volume_down(self, current_volume):
        if self.is_on:
            if current_volume <=0 or current_volume > 10:
                raise ValueError("invalid volume. Volume must be between 1 and 10")

            if current_volume < 10:
                self.volume = current_volume - 1
                return self.volume

        else:
            raise ValueError("Tv is off")



    def mute_tv_volume(self, current_volume):
        if self.is_on:
            if current_volume < 1 or current_volume > 10:
                raise ValueError("invalid volume. Volume must be between 1 and 10")

            # if current_volume < 10:

            self.volume = 0
            return self.volume

        else:
            raise ValueError("Tv is off")



    def unmute_tv_volume(self, current_volume):
        if self.is_on:
            if current_volume < 0 or current_volume > 10:
                raise ValueError("invalid volume. Volume must be between 1 and 10")

            if self.volume == 0:
                self.volume = current_volume

            # if current_volume < 10:
            #     self.volume = current_volume

            return self.volume

        else:
            raise ValueError("Tv is off")
























