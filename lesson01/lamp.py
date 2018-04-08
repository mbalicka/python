import lightbulb

class Lamp:
    def __init__(self, power1, power2):
        self.lightbulb1 = lightbulb.Lightbulb(power1)
        self.lightbulb2 = lightbulb.Lightbulb(power2)

    def setBrightness(self, value):
        self.lightbulb1.setBrightness(value)
        self.lightbulb2.setBrightness(value)

    def showCurrentPower(self):
        power1 = (self.lightbulb1.power * self.lightbulb1.brightness) / 100
        power2 = (self.lightbulb2.power * self.lightbulb2.brightness) / 100
        print(str(power1 + power2))