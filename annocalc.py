from tkinter import *

#GUI
root = Tk()
print("this is a new line for github")

prodT = Label(root, text="productivity:").grid(row=1, column=0)
modT = Label(root, text="module modifier:").grid(row=2, column=0)

item1 = Label(root, text="item 1").grid(row=0,column=1)

i1prod = Entry(root)
i1prod.grid(row=1, column=1)
i1mod = Entry(root)
i1mod.grid(row=2, column=1)

item2 = Label(root, text="item 2").grid(row=0,column=2)

i2prod = Entry(root)
i2prod.grid(row=1, column=2)
i2mod = Entry(root)
i2mod.grid(row=2, column=2)

item3 = Label(root, text="item 3").grid(row=0,column=3)

i3prod = Entry(root)
i3prod.grid(row=1, column=3)
i3mod = Entry(root)
i3mod.grid(row=2, column=3)

working_conditions_label = Label(root, text="working conditions:").grid(row=3,column=1)
working_conditions = Entry(root)
working_conditions.grid(row=3,column=2)

i1prod.insert(10,"0")
i1mod.insert(10,"0")
i2prod.insert(10,"0")
i2mod.insert(10,"0")
i3prod.insert(10,"0")
i3mod.insert(10,"0")
working_conditions.insert(1,"0")

tractorsBool = IntVar()
tractorCheckbox = Checkbutton(text="tractors", variable=tractorsBool)
tractorCheckbox.grid(row=3, column=0)

#base values for farm
basefields = 162
baseperiod = 60
p=100

def showValues():

    #tractor multiplicator from checkbox
    if tractorsBool.get() == 1:
        p+=200
        m=m+basefields*0.5

    #Calculation of neccessary values
    p = p+int(i1prod.get())+int(i2prod.get())+int(i3prod.get())
    modulemodifier = (100+int(i1mod.get())+int(i2mod.get())+int(i3mod.get()))/100
    m = basefields*modulemodifier

    t = baseperiod*100/p
    gpm = 60/t
    gpmpm = gpm/m

    #text output in shell
    print("productivity: " + str(p))
    print("modules: " + str(m))
    print("productivity per module: "+ str(round(p/m,2)))
    print("T: "+str(t))
    print("goods per minute: "+str(gpm))
    print("goods per minute per tile: "+str(gpmpm))

btn = Button(root, text="Calculate", command=showValues).grid(row=3,column=3)

root.mainloop()
