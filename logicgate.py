#When designing classes, 
#it is very important to distinguish between those that have the IS-A relationship (which requires inheritance) and
#those that have HAS-A relationships (with no inheritance)
class LogicGate:

    def __init__(self,n):
        # name of the gate
        self.name = n
        self.output = None

    def getLabel(self):
        #call name of the particular gate
        return self.name

    def getOutput(self):
        self.output = self.performGateLogic()
        return self.output

#Logic gate class is the parent class of binaryGate and UnaryGate
class BinaryGate(LogicGate):

    def __init__(self,n):
        super(BinaryGate, self).__init__(n)

        self.pinA = None
        self.pinB = None

    def getPinA(self):
        if self.pinA == None:
            return int(input("Enter Pin A input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinA.getFrom().getOutput()

    def getPinB(self):
        if self.pinB == None:
            return int(input("Enter Pin B input for gate "+self.getLabel()+"-->"))
        else:
            return self.pinB.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pinA == None:
            self.pinA = source
        else:
            if self.pinB == None:
                self.pinB = source
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")


class AndGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==1 and b==1:
            return 1
        else:
            return 0

class OrGate(BinaryGate):

    def __init__(self,n):
        BinaryGate.__init__(self,n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==1 or b==1:
            return 1
        else:
            return 0
class NandGate(BinaryGate):

    def __init__(self,n):
        super(NandGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a ==0 and b==0:
            return 1
        else:
            return 0

class NorGate(BinaryGate):

    def __init__(self,n):
        super(NorGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if a==0 and b==0:
            return 0
        else:
            return 1
        
class XorGate(BinaryGate):

    def __init__(self,n):
        super(XorGate,self).__init__(n)

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()
        if (a==0 and b==1) or (a==1 and b==0):
            return 1
        else:
            return 0
        
class UnaryGate(LogicGate):

    def __init__(self,n):
        LogicGate.__init__(self,n)

        self.pin = None

    def getPin(self):
        if self.pin == None:
            return int(input("Enter Pin input for gate "+self.getLabel()+"-->"))
        else:
            return self.pin.getFrom().getOutput()

    def setNextPin(self,source):
        if self.pin == None:
            self.pin = source
        else:
            print("Cannot Connect: NO EMPTY PINS on this gate")


class NotGate(UnaryGate):

    def __init__(self,n):
        UnaryGate.__init__(self,n)

    def performGateLogic(self):
        if self.getPin():
            return 0
        else:
            return 1

#The two gate instances within each connector object will be referred to as the fromgate and the togate,
#recognizing that data values will “flow” from the output of one gate into an input line of the next
class Connector:

    def __init__(self, fgate, tgate):
        self.fromgate = fgate
        self.togate = tgate

        tgate.setNextPin(self)

    def getFrom(self):
        return self.fromgate

    def getTo(self):
        return self.togate

class HalfAdder(BinaryGate):
    def __init__(self,n):
        super(HalfAdder,self).__init__(n)

        self.bits, self.carry = None, None
        self.xor = XorGate('XO')
        self.and_ = AndGate('A')

    def performGateLogic(self):

        a = self.getPinA()
        b = self.getPinB()

        self.xor.setNextPin(a)
        self.xor.setNextPin(b)
        self.and_.setNextPin(a)
        self.and_.setNextPin(b)

        self.bits = 1 if (self.xor.pinA==1 and self.xor.pinB==0) or (self.xor.pinA==0 and self.xor.pinB==1) else 0
        self.carry = 1 if (self.and_.pinA==1 and self.and_.pinB ==1) else 0
        return self.bits + self.carry
