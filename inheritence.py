class MobilePhone:
    def __init__(self,screenType, networkType,dualSim,fcamera,rcamera,ram,stroage):
        self.screenType = screenType
        self.networkType = networkType
        self.daulSim = dualSim
        self.fcamera = fcamera
        self.rcamera = rcamera
        self.ram = ram
        self.storage = stroage

    def make_a_call(self):
        pass
    def recieve_a_call(self):
        pass
    def take_a_picture(self):
        pass

class Apple(MobilePhone):
    def __init__(self,smart, Ai,screenType, networkType,dualSim,fcamera,rcamera,ram,stroage):
        self.smart = smart
        self.Ai = Ai
        MobilePhone.__init__(screenType, networkType,dualSim,fcamera,rcamera,ram,stroage)

class Samasung(MobilePhone):
    def __init_(self,flip, series,screenType, networkType,dualSim,fcamera,rcamera,ram,stroage):
        self.flip = flip
        self.series = series
        MobilePhone.__init__(screenType, networkType, dualSim, fcamera, rcamera, ram, stroage)

Type = MobilePhone('TouchScreen', 4, True, 12, 32, 4, 32)
print(Type)