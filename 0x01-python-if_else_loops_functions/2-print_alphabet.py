#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    print('{:c}'.format(i), end='')


3-print_alphabet.py

#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    if chr(i) != 'e' and chr(i) != 'q':
        print('{:c}'.format(i), end='')
