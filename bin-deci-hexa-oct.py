def print_formatted(number):
    #your code goes here
    width = len(bin(number)[2:]) 
    for i in range(1, number + 1):
        decimal = str(i)
        octal = oct(i)[2:]
        hexadecimal = hex(i)[2:].upper()
        binary = b
        int(i)[2:]

        print("{0:>{width}} {1:>{width}} {2:>{width}} {3:>{width}}".format(decimal, octal, hexadecimal, binary, width=width))

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)