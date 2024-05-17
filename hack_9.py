"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1, 2, 3]
    output_list = []
    i = 0
    while i < len(result):
        output_list.append(result[i])
        output_list.append('@')
        i += 1
    return output_list
s = fn_hack_9()
print(s)