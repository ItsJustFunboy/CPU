import bit as BT
import ALU
 
class byte:

    #
    #
    # Layout
    #
    # T8 T7 T6 T5 T4 T3 T2 T1 (states)
    #
    #
    
    signed: bool
    
    T1: BT.bit
    T2: BT.bit
    T3: BT.bit
    T4: BT.bit
    T5: BT.bit
    T6: BT.bit
    T7: BT.bit
    T8: BT.bit
    
    def __init__(self, t1S, t2S, t3S, t4S, t5S, t6S, t7S, t8S: bool):
        self.T1 = t1S
        self.T2 = t2S
        self.T3 = t3S
        self.T4 = t4S
        self.T5 = t5S
        self.T6 = t6S
        self.T7 = t7S
        self.T8 = t8S
    
    def eval(self):

        if not self.signed:
            T1Val = 1 * ALU.boolToInt(self.T1.state)
            T2Val = 2 * ALU.boolToInt(self.T2.state)
            T3Val = 4 * ALU.boolToInt(self.T3.state)
            T4Val = 8 * ALU.boolToInt(self.T4.state)
            T5Val = 16 * ALU.boolToInt(self.T5.state)
            T6Val = 32 * ALU.boolToInt(self.T6.state)
            T7Val = 64 * ALU.boolToInt(self.T7.state)
            T8Val = 128 * ALU.boolToInt(self.T8.state)

            sum: int
            sum = T1Val + T2Val + T3Val + T4Val + T5Val + T6Val + T7Val + T8Val

            return sum
        elif self.signed: 
            T1Val = 1 * ALU.boolToInt(self.T1.state)
            T2Val = 2 * ALU.boolToInt(self.T2.state)
            T3Val = 4 * ALU.boolToInt(self.T3.state)
            T4Val = 8 * ALU.boolToInt(self.T4.state)
            T5Val = 16 * ALU.boolToInt(self.T5.state)
            T6Val = 32 * ALU.boolToInt(self.T6.state)
            T7Val = 64 * ALU.boolToInt(self.T7.state)
            T8Val = 128 * -ALU.boolToInt(self.T8.state)

            sum: int
            sum = T1Val + T2Val + T3Val + T4Val + T5Val + T6Val + T7Val + T8Val

            return sum
        else:
            print("GetValueError();")
            return 0

    

