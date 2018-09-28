num = input()

for i in range(1, int(num)+1):
    for j in range(0, i-1):
        print(' ', end='')
    for j in range(int(num)+1, i, -1):
        print('*', end='')
    print()
