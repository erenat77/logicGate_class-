import logicgate

def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   g5 = XorGate("G5")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   c4 = Connector(g4,g5)
   c5 = Connector(g2,g5)
   print(g5.getOutput())

main()
