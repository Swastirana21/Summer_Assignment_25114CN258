# To convert binary to decimal

binary=input("Enter a bianry number:")

decimal=0

for digit in binary:
    decimal=decimal*2+int(digit)

print("Decimal=",decimal)