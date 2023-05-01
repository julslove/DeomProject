'''
This is a file solving the palindrom problem
'''


def is_palindrom(src_str: str) -> bool:
     src = src_str.casefold()
     return src == src[::-1]

