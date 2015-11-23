#! /usr/bin/env python3

t1 = {
    'A': 3,
    'B': 5,
}

t2 = {
    'C': 7,
    'D': 9,
}

# operation like this won't work
# https://stackoverflow.com/questions/38987/how-can-i-merge-two-python-dictionaries-in-a-single-expression
# t = t1 + t2
# print(t)

t3 = t1.copy()
t3.update(t2)

print(t3)
# {'B': 5, 'C': 7, 'A': 3, 'D': 9}
