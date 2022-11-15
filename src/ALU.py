
#
#                                                                               ALU by ItsJustFunboy
#
#   Bytes are made of 8 bit values, in the order of {8 7 6 5 4 3 2 1}
#
#
#   More than 1 Byte is considered a byte array, having syntax of byte BARR(#of bytes, n)[]]= {byte Bn, byte Bn-1, ... byte B2, byte B1}.
#
#   For example, < byte BARR4[4] = {byte B4, byteB3, byte B2, byte B1}>
#
#
#
#

import byte as BY
import bit as BI


class ALU:

    # Convertions

    def boolToInt(input: bool):

        if input:
            return 1
        else:
            return 0

    def intToBool(input: int):
        if input == 1:
            return 1;
        else:
            return 0;

    # Gates

    def NOT(A: bool):
        if A == 1:
            return 0
        elif A == 0:
            return 1


    def AND(A: bool, B: bool):
        if A == 1:
            return 1
        elif B == 1:
            return 1
        else:
            return 0
    
    def NAND(A: bool, B: bool):
        return ALU.NOT(ALU.AND(A, B))

    def OR(A: bool, B: bool):
        return ALU.NAND(ALU.NOT(A), ALU.NOT(B))

    def XOR(A: bool, B: bool):
        return ALU.AND(ALU.NAND(A, B), OR(A, B))

    def NOR(A: bool, B: bool):
        return ALU.NOT(ALU.OR(A, B))


    def XNOR(A: bool, B: bool):
        return ALU.NOT(ALU.XOR(A, B))


    # Basic Math

    # ADD

    def Add16(A: BY.byte, B: BY.byte, carryIn: bool):

        # CARRY = o1p
        # SUM = x2p

        x1a: bool = ALU.XOR(A.T1.state, B.T1.state);
        a1a: bool = ALU.AND(A.T1.state, B.T1.state);
        x2a: bool = ALU.XOR(x1a, carryIn);
        a2a: bool = ALU.AND(carryIn, x1a);
        o1a: bool = ALU.OR(a1a, a2a);

        x1b: bool = ALU.XOR(A.T2.state, B.T2.state);
        a1b: bool = ALU.AND(A.T2.state, B.T2.state);
        x2b: bool = ALU.XOR(x1b, o1a);
        a2b: bool = ALU.AND(o1a, x1b);
        o1b: bool = ALU.OR(a1b, a2b);

        x1c: bool = ALU.XOR(A.T3.state, B.T3.state);
        a1c: bool = ALU.AND(A.T3.state, B.T3.state);
        x2c: bool = ALU.XOR(x1c, o1b);
        a2c: bool = ALU.AND(o1b, x1c);
        o1c: bool = ALU.OR(a1c, a2c);

        x1d: bool = ALU.XOR(A.T4.state, B.T4.state);
        a1d: bool = ALU.AND(A.T4.state, B.T4.state);
        x2d: bool = ALU.XOR(x1d, o1c);
        a2d: bool = ALU.AND(o1c, x1d);
        o1d: bool = ALU.OR(a1d, a2d);

        x1e: bool = ALU.XOR(A.T5.state, B.T5.state);
        a1e: bool = ALU.AND(A.T5.state, B.T5.state);
        x2e: bool = ALU.XOR(x1e, o1d);
        a2e: bool = ALU.AND(o1d, x1e);
        o1e: bool = ALU.OR(a1e, a2e);

        x1f: bool = ALU.XOR(A.T6.state, B.T6.state);
        a1f: bool = ALU.AND(A.T6.state, B.T6.state);
        x2f: bool = ALU.XOR(x1f, o1e);
        a2f: bool = ALU.AND(o1e, x1e);
        o1f: bool = ALU.OR(a1f, a2f);

        bool x1g = XOR(A.T7.state, B.T7.state);
        bool a1g = AND(A.T7.state, B.T7.state);
        bool x2g = XOR(x1g, o1f);
        bool a2g = AND(o1f, x1g);
        bool o1g = OR(a1g, a2g);

        bool x1h = XOR(A.T8.state, B.T8.state);
        bool a1h = AND(A.T8.state, B.T8.state);
        bool x2h = XOR(x1h, o1g);
        bool a2h = AND(o1g, x1h);
        bool o1h = OR(a1h, a2h);

        bool x1i = XOR(A.T9.state, B.T9.state);
        bool a1i = AND(A.T9.state, B.T9.state);
        bool x2i = XOR(x1i, o1h);
        bool a2i = AND(o1h, x1i);
        bool o1i = OR(a1i, a2i);

        bool x1j = XOR(A.T10.state, B.T10.state);
        bool a1j = AND(A.T10.state, B.T10.state);
        bool x2j = XOR(x1j, o1i);
        bool a2j = AND(o1i, x1j);
        bool o1j = OR(a1j, a2j);

        bool x1k = XOR(A.T11.state, B.T11.state);
        bool a1k = AND(A.T11.state, B.T11.state);
        bool x2k = XOR(x1k, o1j);
        bool a2k = AND(o1j, x1k);
        bool o1k = OR(a1k, a2k);

        bool x1l = XOR(A.T12.state, B.T12.state);
        bool a1l = AND(A.T12.state, B.T12.state);
        bool x2l = XOR(x1l, o1k);
        bool a2l = AND(o1k, x1l);
        bool o1l = OR(a1l, a2l);

        bool x1m = XOR(A.T13.state, B.T13.state);
        bool a1m = AND(A.T13.state, B.T13.state);
        bool x2m = XOR(x1m, o1l);
        bool a2m = AND(o1l, x1m);
        bool o1m = OR(a1m, a2m);

        bool x1n = XOR(A.T14.state, B.T14.state);
        bool a1n = AND(A.T14.state, B.T14.state);
        bool x2n = XOR(x1n, o1m);
        bool a2n = AND(o1m, x1n);
        bool o1n = OR(a1n, a2n);

        bool x1o = XOR(A.T15.state, B.T15.state);
        bool a1o = AND(A.T15.state, B.T15.state);
        bool x2o = XOR(x1o, o1n);
        bool a2o = AND(o1n, x1o);
        bool o1o = OR(a1o, a2o);

        bool x1p = XOR(A.T16.state, B.T16.state);
        bool a1p = AND(A.T16.state, B.T16.state);
        bool x2p = XOR(x1p, o1o);
        bool a2p = AND(o1o, x1p);
        bool o1p = OR(a1p, a2p);

        byte returnedBytes[2] = {byte B2, byte B1};

        returnedBytes[1].T1.state = x2a;
        returnedBytes[1].T2.state = x2b;
        returnedBytes[1].T3.state = x2c;
        returnedBytes[1].T4.state = x2d;
        returnedBytes[1].T5.state = x2e;
        returnedBytes[1].T6.state = x2f;
        returnedBytes[1].T7.state = x2g;
        returnedBytes[1].T8.state = x2h;
        returnedBytes[1].CarryOut.state = NULL;

        returnedBytes[0].T1.state = x2i;
        returnedBytes[0].T2.state = x2j;
        returnedBytes[0].T3.state = x2k;
        returnedBytes[0].T4.state = x2l;
        returnedBytes[0].T5.state = x2m;
        returnedBytes[0].T6.state = x2n;
        returnedBytes[0].T7.state = x2o;
        returnedBytes[0].T8.state = x2p;
        returnedBytes[0].CarryOut.state = o1p;

        return returnedByte;

    }



    # SUB

    byte HalfSub(bit A, bit B) {


        bool sum = XOR(A.state, B.state);
        bool carry = AND(NOT(A.state), B.state);

        byte returnedByte;

        returnedByte.T1.state = sum;
        returnedByte.CarryOut.state = carry;

        return returnedByte;

    }

    byte Sub1(byte A, byte B, bool borrowIn) {

        bool x1 = XOR(A.T1.state, B.T1.state);
        bool a1 = AND(NOT(A.T1.state), B.T1.state);
        bool x2 = XOR(x1, borrowIn);
        bool a2 = AND(borrowIn, NOT(x1));
        bool o1 = OR(a1, a2);

        if (o1) {
            byte returnedByte;

            returnedByte.T1.state = 0;
            returnedByte.T2.state = 0;
            returnedByte.T3.state = 0;
            returnedByte.T4.state = 0;
            returnedByte.T5.state = 0;
            returnedByte.T6.state = 0;
            returnedByte.T7.state = 0;
            returnedByte.T8.state = 0;

            printf("WARNING::SUB1BYTE_OVERFLOW; BYTE RESET.\n");

            return returnedByte;

        }
        else {

            byte returnedByte;
            returnedByte.T1.state = x2;

            return returnedByte;
        }

    }