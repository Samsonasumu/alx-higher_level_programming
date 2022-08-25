#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    if len(sys.argv) == 1:
        print(0)
    elif len(sys.argv) == 2:
        print(sys.argv[1])
    else:
        sum = 0
        for i in range(1, len(sys.argv)):
            a = int(sys.argv[i])
            sum = sum + a
        print(sum)
