"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    result = list(filter(lambda x: x in [3, 5, 7], result))
    return result