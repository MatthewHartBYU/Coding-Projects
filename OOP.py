class Lego:
    def __init__(self, color, dimensions, wellbeing):
        self.color = color
        self.dimensions = dimensions
        self.wellbeing = wellbeing
        self.timesSteppedOn = 0
    def build(self):
        return f"The {self.color} Lego brick is being played with. Current wellbeing is {self.wellbeing} HP."
    def step(self):
        self.wellbeing -= 1
        self.timesSteppedOn +=1
        return f"The {self.color} Lego brick was stepped on! Ouch. That's gotta hurt!"
    def getTimesSteppedOn(self):
        if self.timesSteppedOn == 1:
            return f"The {self.color} Lego brick has been stepped on 1 time."
        else:
            return f"The {self.color} Lego brick has been stepped on {self.timesSteppedOn} times."
brick1 = Lego("Red", "2x4", 100)
print(brick1.step())
print(brick1.step())
print(brick1.build())
print(brick1.getTimesSteppedOn())
