class Fraction:
    # See slideshow for a full discussion of this code.
    #
    def __init__(self, num, den):
        self.__n = num
        self.__d = den
    
    def getNum(self):
        return self.__n

    def getDen(self):
        return self.__d
    
    def setNum(self, num):
        self.__n = num
    
    def setDen(self, den):
        self.__d = den
    
    def __str__(self):
        return "{0}/{1}".format(self.__n, self.__d)
        
class Fraction2(Fraction):
    def check(self):
        print("Err: Denominator cannot be 0" if self.getDen() == 0 else "Denominator OK")

    def unreduce(self, factor):
        self.setNum(self.getNum() * factor)
        self.setDen(self.getDen() * factor)
    
# driver code
f = Fraction2(3, 4)
print("f:", f)
f.check()
f2 = Fraction2(5, 0)
print("f2:", f2)
f2.check()

f.unreduce(2)
print("f:", f)
