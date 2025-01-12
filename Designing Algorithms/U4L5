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

    def mult(self, frac2):
        newNum = self.getNum() * frac2.getNum()
        newDen = self.getDen() * frac2.getDen()
        return Fraction2(newNum, newDen)
    
    def add(self, frac2):
        tempDen = self.getDen()
        self.unreduce(frac2.getDen())
        frac2.unreduce(tempDen)

        newNum = self.getNum() + frac2.getNum()
        return Fraction(newNum, self.getDen())
    
# driver code
f = Fraction2(3, 4)
f2 = Fraction2(5, 6)
print("f:", f)
print("f2:", f2)

f3 = f.mult(f2)
f4 = f.add(f2)
print("f*f2:", f3)
print("f+f2:", f4)
