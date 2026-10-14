def _check(*bits):
    for b in bits:
        if b not in (0, 1):
            raise ValueError(f"Logic gate inputs must be 0 or 1, got {b}")


def AND(a, b):
    _check(a, b)
    return a & b

def OR(a, b):
    _check(a, b)
    return a | b

def NOT(a):
    _check(a)
    return 1 - a

def NAND(a, b):
    _check(a, b)
    return NOT(AND(a, b))

def NOR(a, b):
    _check(a, b)
    return NOT(OR(a, b))

def XOR(a, b):
    _check(a, b)
    return a ^ b

def XNOR(a, b):
    _check(a, b)
    return NOT(XOR(a, b))


def print_truth_table():
    print("A B | AND OR NAND NOR XOR XNOR")
    print("-" * 42)
    for a in (0, 1):
        for b in (0, 1):
            print(f"{a} {b} |  {AND(a, b)}   {OR(a, b)}   {NAND(a, b)}    {NOR(a, b)}   {XOR(a, b)}    {XNOR(a, b)}")
    print()
    print("A | NOT")
    print("-" * 9)
    for a in (0, 1):
        print(f"{a} |  {NOT(a)}")


if __name__ == "__main__":
    print_truth_table()
