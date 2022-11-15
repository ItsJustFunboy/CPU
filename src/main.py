import ALU

def main():

    b1: ALU.byte

    b1.T1.state = 1
    b1.T2.state = 1
    b1.T3.state = 0
    b1.T4.state = 0
    b1.T5.state = 0
    b1.T6.state = 0
    b1.T7.state = 0
    b1.T8.state = 1

    b2: ALU.byte

    b2.T1.state = 1
    b2.T2.state = 1
    b2.T3.state = 0
    b2.T4.state = 0
    b2.T5.state = 0
    b2.T6.state = 0
    b2.T7.state = 0
    b2.T8.state = 0

    print("" + str(ALU.byteToInt(ALU.Add2(b1, b2, 0))))

