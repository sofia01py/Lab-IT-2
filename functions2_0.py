import re
import sys

from prototipe import *


def text_to_bits(txt, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(txt.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

def text_from_bits(decode, encoding='utf-8', errors='surrogatepass'):
    n = int(decode, 2)
    return n.to_bytes((n.bit_length() + 7) // 8, 'big').decode(encoding, errors) or '\0'

def testing_expression_summators(expression):
    symbols = "!@#$%^&*()_+=/><.,'№;:?"
    regexp = r"([a-zA-Z])"
    match = re.search(regexp, expression)
    if (match is None) and (symbols not in expression):
        return True
    else:
        return False

def testing_expression_positions(expression):
    symbols = "!@#$%^&*()+=/><.,'№;:?_4567890"
    regexp = r"([a-zA-Z])"
    match = re.search(regexp, expression)
    if (match is None) and (symbols not in expression):
        return True
    else:
        return False

def first(input_txt):
    input_txt = text_to_bits(input_txt)
    i = []
    for k, l in enumerate(input_txt):
        if int(l) == 1:
            i.append(k)



#decoder

def decode(code_word, file):
    import numpy as np
    txt_1 = np.polydiv(code_word, file)[0]
    txt_1 = "".join(map(str, txt_1))
    return txt_1



#def delite():
    #entry1.delete(0, END)
    #entry2.delete(0, END)
    #entry3.delete(0, END)
    #entry4.delete(0, END)
    #entry5.delete(0, END)
    #return

#bttn3 = Button(root, text="del", width = 15, command = delite)
#bttn3.grid(row=10, column = 2, columnspan=1)