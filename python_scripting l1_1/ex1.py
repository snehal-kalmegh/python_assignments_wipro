import sys

def ruler(num=43):

        off = num % 10
        n = num // 10
        for i in range(1, n+1):
            print('{:>10}'.format(i), end='')
        print('\n')
        for i in range(n):
            print('1234567890', end='')
        for i in range(1, off+1):
            print(i, end='')
        print('\n')

def main():

    try:
        inp = int(input('Enter an integer!\n'))
    except TypeError('Only integers allowed!'):
        print('possible')
    ruler(inp)


if __name__ == '__main__':
    main()

