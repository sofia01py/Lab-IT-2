from tkinter import *
from tkinter import messagebox
from functions import *
import re

root = Tk()
root.title("convolutional code")
root.configure(bg="#ffcdd2")
root.geometry('500x250')

def C_C():
    global max
    global fi1e
    try:
        if (CC_entry != "") or (CC1_entry != "") or (CC2_entry != ""):
            fi1e = CC_entry.get()
            txt_bits = text_to_bits(fi1e)
            i = []

            for k, l in enumerate(txt_bits):
                if int(l) == 1:
                    i.append(k)

            expression = CC1_entry.get()

            if testing_expression_summators(expression) == True:
                summators = int(expression)
                g = []
                m = []
                expression = CC2_entry.get()
                if testing_expression_positions(expression) == True:
                    while expression != '':
                        if expression.find(" ") != -1:
                            m.append(expression[:expression.find(" ")])
                            expression = expression[expression.find(" ") + 1:]
                        else:
                            regexp = r"(\d+)"
                            a = re.search(regexp, expression)
                            m.append(a[0])
                            expression = ''

                    count = 0
                    for j in range(len(m)):
                        count +=1
                        t = list(m[j])
                        g.append(t)
                    if count != summators:
                        messagebox.showerror('error', 'Something went wrong!')
                        return
                else:
                    messagebox.showerror('error', 'Something went wrong!')
                for k, m in enumerate(g):
                    for l, n in enumerate(g[k]):
                        g[k][l] = int(g[k][l]) - 1
                c = []
                for k, m in enumerate(g):
                    a = []
                    for l, n in enumerate(g[k]):
                        for p, q in enumerate(i):
                            d = int(n) + int(q)
                            a.append(d)
                            a.sort()
                    c.append(a)
                count = -1
                code_word = []
                for o in range(len(c)):
                    for k in range(len(c[o]) - 1):
                        if (c[o][k] == c[o][k + 1]) or (c[o][k] == count):
                            count = c[o][k]
                            c[o][k] = -1
                            c[o][k] = -1
                for o in range(len(c)):
                    while c[o].count(-1) != 0:
                        c[o].remove(-1)
                max = max(map(max, c))
                for k, m in enumerate(c):
                    min = 0
                    while min != max:
                        if min in c[k]:
                            code_word.append(1)
                        else:
                            code_word.append(0)
                        min += 1
                txt_1 = "".join(map(str, code_word))
                label_uno(txt_1)
                file = perform_viterbi_decoding(txt_1)

            else:
                messagebox.showerror('error', 'Something went wrong!')
        else:
            messagebox.showerror('error', 'Something went wrong!')
    except:
        messagebox.showerror('error', 'Something went wrong!')

def label_uno(CC):
    lbl3["text"] = CC

def label_duo(CC):
    lbl4["text"] = CC

def DC_C():
    try:
        label_duo(fi1e)
    except:
        messagebox.showerror('error', 'Something went wrong!')


lbl=Label(root, text="Введите слово:", fg="#000000", bg="#ffcdd2", width = 35)
lbl.grid(row=0, column = 0, columnspan=5)
CC_entry = Entry(root, width = 82)
CC_entry.grid(row=1, column=0, columnspan=5)
lbl1=Label(root, text="Введите кол-во сумматоров:", fg="#000000", bg="#ffcdd2")
lbl1.grid(row=2, column = 0, columnspan=1)
CC1_entry = Entry(root, width = 35)
CC1_entry.grid(row=2, column=3, columnspan=1)
lbl2=Label(root, text="Введите их позиции:", fg="#000000", bg="#ffcdd2", width = 35)
lbl2.grid(row=3, column = 0, columnspan=1)
CC2_entry = Entry(root, text="", fg="#000000", bg="#ffcdd2", width = 35)
CC2_entry.grid(row=3, column = 3, columnspan=1)
bttn = Button(root, text="КОДИРОВАТЬ", width = 50, command = C_C)
bttn.grid(row=4, column = 0, columnspan=5)
lbl3=Label(root, text="", fg="#000000", bg="#ffcdd2", width = 70)
lbl3.grid(row=5, column = 0, columnspan=5)
bttn1 = Button(root, text="ДЕКОДИРОВАТЬ", command =DC_C, width = 50)
bttn1.grid(row=6, column = 0, columnspan=5)
lbl4=Label(root, text="", fg="#000000", bg="#ffcdd2", width = 70)
lbl4.grid(row=7, column = 0, columnspan=5)

root.mainloop()