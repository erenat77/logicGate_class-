import logicgate

#The outputs from the two AND gates (g1 and g2) are connected to the OR gate (g3) and that output is connected to the NOT gate (g4). 
#The output from the NOT gate is the output of the entire circuit

def main():
   g1 = AndGate("G1")
   g2 = AndGate("G2")
   g3 = OrGate("G3")
   g4 = NotGate("G4")
   c1 = Connector(g1,g3)
   c2 = Connector(g2,g3)
   c3 = Connector(g3,g4)
   print(g4.getOutput())

main()
