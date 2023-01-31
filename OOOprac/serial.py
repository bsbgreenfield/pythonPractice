class SerialGenerator:
    def __init__(self, start):
        self.start = start
        self.incr = 0

    def generate(self):
        self.start += 1
        self.incr += 1
        print(self.start)

    def reset(self):
        self.start -= self.incr
        self.incr = 0


serial = SerialGenerator(100)

serial.generate()

serial.generate()

serial.generate()

serial.reset()

serial.generate()