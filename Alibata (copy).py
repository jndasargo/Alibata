from Tkinter import *
from Tkinter import Label, Button, END
from Tkinter import *
from Tix import Tk, Control, ComboBox
import tkMessageBox
import os
from PIL import ImageTk, Image

def letter_type(ltr):
    if ltr in vow:
        ctp = 'v'
    else :
        ctp = 'c'
    return ctp
def Cut(a):
    global vow
    v = 'v'
    c = 'c'
    a = a+' '
    num = len(a)
    vow = 'AEIOUaeiou |{}[]".1234567890~`|,./?>< '
    i = 0
    stro1 = ''
    ltr = a[0]
    list = []
    while  i < num:
        ltr = a[i]
        if i != 0:
            pltr = a[i-1]    
        else:
            pltr = ''
        i = i+1
        if (letter_type(pltr)==letter_type(ltr)):
            list.append (stro1)
            stro1 = ''
        stro1 = stro1+ltr
        if (letter_type(ltr) == v):
            list.append (stro1)
            stro1 = ''
    for item in list:
        if item == '':
            list.remove(item)
    consonant = 'BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz'
    incr = 0
    for item in list:
        if len(item) == 2:
            if item[-1:] == ' ':
                l1 = item[:1]
                l2 = ' '
                list.remove(item)
                list.insert(incr, l1)
                list.insert(incr+1, l2)       
        incr = incr + 1
    incr = 0
    for incr in range(len(list)):
        try:
            if len(item) == 1:
                if list[incr] == 'n':
                    if ((list[incr+1]=='g')|(list[incr+1]=='ga')|(list[incr+1]=='ge')|(list[incr+1]=='gi')|(list[incr+1]=='go')|(list[incr+1]=='gu')):
##                        print list[incr]
                        list.remove(list[incr])
                        keys = 'n'+list[incr]
                        just = list[incr]
                        list.remove(just)
                        list.insert(incr, keys)
                        incr = incr - 1
        except:
            pass
        incr = incr + 1 
    try:
        if list[-1] == ' ':
            del list[-1]
        if list[21] == ' ':
            del list[21]
        if list[42] == ' ':
            del list[42]
        if list[63] == ' ':
            del list[63]
        if list[84] == ' ':
            del list[84]
        if list[105] == ' ':
            del list[105]
        if list[126] == ' ':
            del list[126]
    except:
        pass
    return list

def lala(letfind):
    try:
        if len(letfind)== 1:
            if ((letfind == 'A')|(letfind == 'a')):
                letret = 'letters\\a.png'
            elif ((letfind == 'e')|(letfind == 'i')|(letfind == 'E')|(letfind == 'I')):
                letret = 'letters\\e.png'
            elif ((letfind == 'o')|(letfind == 'u')|(letfind == 'O')|(letfind == 'U')):
                letret = 'letters\\o.png'
            elif ((letfind == 'B')|(letfind == 'b')):
                letret = 'letters\\b.png'
            elif ((letfind == 'C')|(letfind == 'c')):
                letret = 'letters\\k.png'
            elif ((letfind == 'D')|(letfind == 'd')):
                letret = 'letters\\d.png'
            elif ((letfind == 'F')|(letfind == 'f')):
                letret = 'letters\\p.png'
            elif ((letfind == 'G')|(letfind == 'g')):
                letret = 'letters\\g.png'
            elif ((letfind == 'H')|(letfind == 'h')):
                letret = 'letters\\h.png'
            elif ((letfind == 'J')|(letfind == 'j')):
                letret = 'letters\\d.png'
            elif ((letfind == 'K')|(letfind == 'k')):
                letret = 'letters\\k.png'
            elif ((letfind == 'L')|(letfind == 'l')):
                letret = 'letters\\l.png'
            elif ((letfind == 'M')|(letfind == 'm')):
                letret = 'letters\\m.png'
            elif ((letfind == 'N')|(letfind == 'n')):
                letret = 'letters\\n.png'
            elif ((letfind == 'P')|(letfind == 'p')):
                letret = 'letters\\p.png'
            elif ((letfind == 'S')|(letfind == 's')):
                letret = 'letters\\s.png'
            elif ((letfind == 'T')|(letfind == 't')):
                letret = 'letters\\t.png'
            elif ((letfind == 'W')|(letfind == 'w')):
                letret = 'letters\\w.png'
            elif ((letfind == 'Y')|(letfind == 'y')):
                letret = 'letters\\y.png'
            elif ((letfind == 'R')|(letfind == 'r')):
                    letret = 'letters\\l.png'
            elif ((letfind == 'Z')|(letfind == 'z')):
                    letret = 'letters\\s.png'
            elif ((letfind == 'V')|(letfind == 'v')):
                    letret = 'letters\\b.png'
            else:
                letret = 'letters\\blank.png'
        elif len(letfind) == 2:
            if (letfind[-1:]=='A')|(letfind[-1:]=='a'):
                if ((letfind[:1] == 'B')|(letfind[:1] == 'b')):
                    letret = 'letters\\ba.png'
                elif ((letfind[:1] == 'C')|(letfind[:1] == 'c')):
                    letret = 'letters\\ka.png'
                elif ((letfind[:1] == 'D')|(letfind[:1] == 'd')):
                    letret = 'letters\\da.png'
                elif ((letfind[:1] == 'F')|(letfind[:1] == 'f')):
                    letret = 'letters\\pa.png'
                elif ((letfind[:1] == 'G')|(letfind[:1] == 'g')):
                    letret = 'letters\\ga.png'
                elif ((letfind[:1] == 'H')|(letfind[:1] == 'h')):
                    letret = 'letters\\ha.png'
                elif ((letfind[:1] == 'J')|(letfind[:1] == 'j')):
                    letret = 'letters\\d.png'
                elif ((letfind[:1] == 'K')|(letfind[:1] == 'k')):
                    letret = 'letters\\ka.png'
                elif ((letfind[:1] == 'L')|(letfind[:1] == 'l')):
                    letret = 'letters\\la.png'
                elif ((letfind[:1] == 'M')|(letfind[:1] == 'm')):
                    letret = 'letters\\ma.png'
                elif ((letfind[:1] == 'N')|(letfind[:1] == 'n')):
                    letret = 'letters\\na.png'
                elif ((letfind[:1] == 'P')|(letfind[:1] == 'p')):
                    letret = 'letters\\pa.png'
                elif ((letfind[:1] == 'S')|(letfind[:1] == 's')):
                    letret = 'letters\\sa.png'
                elif ((letfind[:1] == 'T')|(letfind[:1] == 't')):
                    letret = 'letters\\ta.png'
                elif ((letfind[:1] == 'W')|(letfind[:1] == 'w')):
                    letret = 'letters\\wa.png'
                elif ((letfind[:1] == 'Y')|(letfind[:1] == 'y')):
                    letret = 'letters\\ya.png'
                elif ((letfind[:1] == 'R')|(letfind[:1] == 'r')):
                    letret = 'letters\\la.png'
                elif ((letfind[:1] == 'Z')|(letfind[:1] == 'z')):
                    letret = 'letters\\sa.png'
                elif ((letfind[:1] == 'V')|(letfind[:1] == 'v')):
                    letret = 'letters\\ba.png'
            elif (letfind[-1:]=='E')|(letfind[-1:]=='e')|(letfind[-1:]=='I')|(letfind[-1:]=='i'):
                if ((letfind[:1] == 'B')|(letfind[:1] == 'b')):
                    letret = 'letters\\be.png'
                elif ((letfind[:1] == 'C')|(letfind[:1] == 'c')):
                    letret = 'letters\\ke.png'
                elif ((letfind[:1] == 'D')|(letfind[:1] == 'd')):
                    letret = 'letters\\de.png'
                elif ((letfind[:1] == 'F')|(letfind[:1] == 'f')):
                    letret = 'letters\\pe.png'
                elif ((letfind[:1] == 'G')|(letfind[:1] == 'g')):
                    letret = 'letters\\ge.png'
                elif ((letfind[:1] == 'H')|(letfind[:1] == 'h')):
                    letret = 'letters\\he.png'
                elif ((letfind[:1] == 'J')|(letfind[:1] == 'j')):
                    letret = 'letters\\d.png'
                elif ((letfind[:1] == 'K')|(letfind[:1] == 'k')):
                    letret = 'letters\\ke.png'
                elif ((letfind[:1] == 'L')|(letfind[:1] == 'l')):
                    letret = 'letters\\le.png'
                elif ((letfind[:1] == 'M')|(letfind[:1] == 'm')):
                    letret = 'letters\\me.png'
                elif ((letfind[:1] == 'N')|(letfind[:1] == 'n')):
                    letret = 'letters\\ne.png'
                elif ((letfind[:1] == 'P')|(letfind[:1] == 'p')):
                    letret = 'letters\\pe.png'
                elif ((letfind[:1] == 'S')|(letfind[:1] == 's')):
                    letret = 'letters\\se.png'
                elif ((letfind[:1] == 'T')|(letfind[:1] == 't')):
                    letret = 'letters\\te.png'
                elif ((letfind[:1] == 'W')|(letfind[:1] == 'w')):
                    letret = 'letters\\we.png'
                elif ((letfind[:1] == 'Y')|(letfind[:1] == 'y')):
                    letret = 'letters\\ye.png'
                elif ((letfind[:1] == 'R')|(letfind[:1] == 'r')):
                    letret = 'letters\\le.png'
                elif ((letfind[:1] == 'Z')|(letfind[:1] == 'z')):
                    letret = 'letters\\se.png'
                elif ((letfind[:1] == 'V')|(letfind[:1] == 'v')):
                    letret = 'letters\\be.png'
            elif (letfind[-1:]=='O')|(letfind[-1:]=='o')|(letfind[-1:]=='U')|(letfind[-1:]=='u'):
                if ((letfind[:1] == 'B')|(letfind[:1] == 'b')):
                    letret = 'letters\\bo.png'
                elif ((letfind[:1] == 'C')|(letfind[:1] == 'c')):
                    letret = 'letters\\ko.png'
                elif ((letfind[:1] == 'D')|(letfind[:1] == 'd')):
                    letret = 'letters\\do.png'
                elif ((letfind[:1] == 'F')|(letfind[:1] == 'f')):
                    letret = 'letters\\po.png'
                elif ((letfind[:1] == 'G')|(letfind[:1] == 'g')):
                    letret = 'letters\\go.png'
                elif ((letfind[:1] == 'H')|(letfind[:1] == 'h')):
                    letret = 'letters\\ho.png'
                elif ((letfind[:1] == 'J')|(letfind[:1] == 'j')):
                    letret = 'letters\\d.png'
                elif ((letfind[:1] == 'K')|(letfind[:1] == 'k')):
                    letret = 'letters\\ko.png'
                elif ((letfind[:1] == 'L')|(letfind[:1] == 'l')):
                    letret = 'letters\\lo.png'
                elif ((letfind[:1] == 'M')|(letfind[:1] == 'm')):
                    letret = 'letters\\mo.png'
                elif ((letfind[:1] == 'N')|(letfind[:1] == 'n')):
                    letret = 'letters\\no.png'
                elif ((letfind[:1] == 'P')|(letfind[:1] == 'p')):
                    letret = 'letters\\po.png'
                elif ((letfind[:1] == 'S')|(letfind[:1] == 's')):
                    letret = 'letters\\so.png'
                elif ((letfind[:1] == 'T')|(letfind[:1] == 't')):
                    letret = 'letters\\to.png'
                elif ((letfind[:1] == 'W')|(letfind[:1] == 'w')):
                    letret = 'letters\\wo.png'
                elif ((letfind[:1] == 'Y')|(letfind[:1] == 'y')):
                    letret = 'letters\\yo.png'
                elif ((letfind[:1] == 'R')|(letfind[:1] == 'r')):
                    letret = 'letters\\lo.png'
                elif ((letfind[:1] == 'Z')|(letfind[:1] == 'z')):
                    letret = 'letters\\so.png'
                elif ((letfind[:1] == 'V')|(letfind[:1] == 'v')):
                    letret = 'letters\\bo.png'
            else:
                letret = 'letters\\ng.png'
        elif len(letfind) == 3:
            if (letfind[-1:] == 'E')|(letfind[-1:]=='e')|(letfind[-1:]=='I')|(letfind[-1:]=='i'):
                letret = 'letters\\nge.png'
            elif ((letfind[-1:] == 'A')|(letfind[-1:]=='a')):
                letret = 'letters\\nga.png'
            elif (letfind[-1:] == 'U')|(letfind[-1:]=='u')|(letfind[-1:]=='O')|(letfind[-1:]=='o'):
                letret = 'letters\\ngo.png'

    except:
        letret = 'letters\\blank.png'

    return letret

def h(*args):
    cc = Cut(line.get(1.0,END))
##    print cc
    newlist = []
    dd = []
    for item in cc:
        if (item == 'j')|(item[:1]== 'j'):
            dd = dd+[lala(item)]
            if len(item) == 1:
                dd = dd+['letters\\y.png']
            else:
                if (item[-1:] == 'A')|(item[-1:] == 'a'):
                    dd = dd+['letters\\ya.png']
                if (item[-1:] == 'E')|(item[-1:] == 'e')|(item[-1:] == 'I')|(item[-1:] == 'i'):
                    dd = dd+['letters\\ye.png']
                if (item[-1:] == 'O')|(item[-1:] == 'o')|(item[-1:] == 'U')|(item[-1:] == 'u'):
                    dd = dd+['letters\\yo.png']
        else:
            dd = dd+[lala(item)]
    imr1 = []
    i = 0
##    print dd
    
    indr=0
    for item in cc:
        if (item == 'j')|(item == 'ja')|(item == 'je')|(item == 'jo')|(item == 'ji')|(item == 'ju'):
            cc.insert(indr+1,' ')
##        print cc
        indr = indr + 1
    even = ['0','2','4','6','8','10','12','14']
    odd = ['1','3','5','7','9','11','13','15']
    try:
        for r in range(6):    
            for c in range(21):
                imr1 = imr1+[ImageTk.PhotoImage(Image.open(dd[i]))]
                Label(bottom1,image=imr1[i]).grid(row=r*2,column=c)
                Label(bottom1,text=cc[i]).grid(row=r*2+1,column=c)
                i = i + 1
    except:
        pass

    master.mainloop()

def clearpage(*args):
    global bottom1
    bottom1.destroy()
    bottom1 = Frame(bottom)
    bottom1.grid()
    
def clearbox(*args):
    line.delete(1.0,END)

def newpage(*args):
    os.startfile('main.exe')

global bottom1

master = Tk()
master.geometry('1250x700')
master.title('Alibata Translator Software')

menubar = Menu(master)
clearPage = Menu(menubar)
menubar.add_cascade(label='Clear Page',command=clearpage)
clearBox = Menu(menubar)
menubar.add_cascade(label='Clear Input',command=clearbox)
newPage = Menu(menubar)
menubar.add_cascade(label='New Page',command=newpage)
credit = Menu(menubar)
menubar.add_cascade(label='Credits')
master.config(menu=menubar)

toptop = LabelFrame(master)
top = Frame(toptop)
bottom = Frame(master)
##scrollbar = Scrollbar(bottom)
##scrollbar.pack(side=RIGHT,fill=Y)
bottom1 = Frame(bottom)
##scrollbar.config(command=bottom1.yview)

line = Text(top,height=5,width=75,wrap=WORD)
line.pack(padx=10,pady=5,side=LEFT)
Button(top,text='Convert',font='Algerian -15',width=20,height=3,command=h).pack(side=RIGHT,padx=75,pady=5)

top.pack(side=LEFT)
toptop.pack(fill=X)
bottom1.grid()
bottom.pack()
master.mainloop()
