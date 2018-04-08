class Lightbulb:
    brightness = 0
    power = 0

    def __init__(self, power):
        self.power = power

    def setBrightness(self, value):
        if value < 0 or value > 100:
            print("invalid value")
            return
        self.brightness = value
        print("Brightness is equal " + str(self.brightness))

    def showCurrentPower(self):
        print(str((self.brightness * self.power) / 100))