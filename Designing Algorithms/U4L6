class char:
    def __init__(self, c : str):
        # A value of None is used if the the current node is the head, otherwise it's the first character
        self.ch = None if c == None else c[0]
        # Initilize the next value as None as well
        self.next = None
    
    def __str__(self):
        return self.ch

class myStr:
    def __init__(self, s: str):
        self.__s = s
        self.__head = char(None)
        chCount = 0
        for c in self.__s:
            # Adding the first character as a "next" of the head node
            if chCount == 0:
                self.__head.next = char(c)
                self.__C = self.__head.next
            else:
                self.__C.next = char(c)
                self.__C = self.__C.next
            chCount += 1
        self.__len = chCount
    
    # Modify 1
    def __str__(self):
        self.__C = self.__head.next
        myStr = ""

        while(self.__C):
            myStr += self.__C.ch
            self.__C = self.__C.next
        
        return myStr

    # Modify 2
    def length(self):
        return self.__len

    def isascii(self):
        asciiState = True
        self.__C = self.__head.next

        # The loop will end early if any character is not ascii
        while(self.__C and asciiState):
            # Check if each character is ascii, assign to asciiState
            asciiState = self.__C.ch.isascii()
            self.__C = self.__C.next
        
        return asciiState

    def isalpha(self):
        alphaState = True
        self.__C = self.__head.next

        # Loop will end early if any character is not alpha
        while(self.__C and alphaState):
            chOrd = ord(self.__C.ch)
            # Check if each character counts as a lower or upper case letter, assign to alphaState
            alphaState = chOrd in range(65,91) or chOrd in range(97,123)
            self.__C = self.__C.next
        
        return alphaState

    # Modify 3
    def transformUpper(self):
        self.__C = self.__head.next
        myStr = ""

        while(self.__C):
            chOrd = ord(self.__C.ch)
            # If the character is an upper case letter...
            if chOrd in range(97, 123):
                # Add the lower case version to the string
                myStr += chr(chOrd - 32)
            # Otherwise just add the character
            else:
                myStr += self.__C.ch
            
            # myStr += chr(chOrd - 32) if chOrd in range(97, 123) else self.__C.ch

            self.__C = self.__C.next
        
        return myStr

    def transformLower(self):
        self.__C = self.__head.next
        myStr = ""

        while(self.__C):
            chOrd = ord(self.__C.ch)
            # If the character is a upper case letter...
            if chOrd in range(65, 91):
                # Add the lower case version to the string
                myStr += chr(chOrd + 32)
            # Otherwise just add the character
            else:
                myStr += self.__C.ch

            self.__C = self.__C.next

        # myStr += chr(chOrd + 32) if chOrd in range(65, 91) else self.__C.ch
        
        return myStr

# Driver code
S = myStr("Hello")
print(S)
print("String len:", S.length())
print("S is ascii:", S.isascii())
print("S is alpha:", S.isalpha())
print("Uppercase:", S.transformUpper())
print("Lowercase:", S.transformLower())
