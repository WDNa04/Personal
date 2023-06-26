import sys
def Hanoi(number, start, target, help):
    if number == 1:
        print(start, "→", target)
    elif number >= 2:
        Hanoi(number-1, start, target, help)
        print(start, "→", target)
        Hanoi(number -1, help, target, start)

a = 0
def Hanoi_n(number, start, target, help):
    global a
    if number == 1:
        a += 1
    else:
        Hanoi_n(number-1, start, target, help)
        a += 1
        Hanoi_n(number -1, help, target, start)

number = int(sys.stdin.readline())
Hanoi(number,'A', 'B', 'C')
Hanoi_n(number, 'A', 'B', 'C')
print("The number of movements is {}.". format(a))

