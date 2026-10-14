```python
# Program to implement the 7 basic logic gates

A = int(input("Enter first input (0 or 1): "))
B = int(input("Enter second input (0 or 1): "))

# NOT gate uses only input A
print("\nNOT Gate:")
print("NOT A =", int(not A))

# AND gate
print("\nAND Gate:")
print("A AND B =", A & B)

# OR gate
print("\nOR Gate:")
print("A OR B =", A | B)

# NAND gate
print("\nNAND Gate:")
print("A NAND B =", int(not (A & B)))

# NOR gate
print("\nNOR Gate:")
print("A NOR B =", int(not (A | B)))

# XOR gate
print("\nXOR Gate:")
print("A XOR B =", A ^ B)

# XNOR gate
print("\nXNOR Gate:")
print("A XNOR B =", int(not (A ^ B)))
```
