import arcpy
import numpy
from Tkinter import *
import os
arcpy.env.workspace=r'C:\Users\Brahima\Desktop\cartes Maroc\s1.gdb'


#Button(root3,text='Quit', command=root3.quit).grid(row=3,column=0)

def ShowTable():
    root0 = Tk()
    root0['background'] = '#58F'
    T = Text(root0, height = 50, width = 50)
    T.pack()
    tables=arcpy.ListFeatureClasses()
    a=""
    for table in tables:
        a+=str(table)
        a+="\n"
    T.insert(END, a)
    root0.mainloop()

def ShowFeild():

    root1 = Tk()
    root1['background'] = '#58F'
    T = Text(root1, height = 50, width = 50)
    T.pack()
    path=r'C:\Users\Brahima\Desktop\cartes Maroc\s1.gdb'
    champ_table=arcpy.ListFields(os.path.join(path,str(e3.get())))
    for field in champ_table:
        f=(field.name+"\n")
        T.insert(END, f)
    root1.mainloop()



def ShowFeild_All_tables():

    root11 = Tk()
    root11['background'] = '#58F'
    root11.geometry("200x200")
    global e3

    Label(root11,
             text="Table").grid(row=0)


    e3 = Entry(root11)

    e3.grid(row=0, column=1)

    Button(root11,
              text='Show',
              command=ShowFeild).grid(row=3,column=0)


    root11.mainloop()






def ShowLine():

    print(str(e4.get()))
    print(str(e41.get()))

    root2 = Tk()
    root2['background'] = '#58F'
    T = Text(root2, height = 200, width = 50)
    T.pack()
    cursor = arcpy.da.SearchCursor(str(e4.get()), ("OBJECTID",str(e41.get()))) #suivant valeur 3
    a=""
    for row in cursor:
        for col in row:
            a+=str(col)
            a+="\t"
        a+="\n"
    T.insert(END, a)
    root2.mainloop()

def ShowLine_All_Line():

    root21 = Tk()
    root21['background'] = '#58F'
    root21.geometry("200x200")
    global e4
    global e41

    Label(root21,
             text="Table").grid(row=0)


    e4 = Entry(root21)

    e4.grid(row=0, column=1)



    Label(root21,
             text="Filed").grid(row=1)


    e41 = Entry(root21)

    e41.grid(row=1, column=1)

    Button(root21,
              text='Show',
              command=ShowLine).grid(row=3,column=0)


    root21.mainloop()

def ajout_field_save():

    print(str(e1.get()))
    print(str(e11.get()))
    arcpy.AddField_management(str(e1.get()),str(e11.get()),"LONG")
    print("Feild Ajouter")


def ajout_field():

    root3 = Tk()
    root3['background'] = '#58F'
    root3.geometry("200x200")
    global e1
    global e11
    Label(root3,
             text="Table").grid(row=0)


    e1 = Entry(root3)

    e1.grid(row=0, column=1)

    Label(root3,
             text="Fild").grid(row=1)


    e11 = Entry(root3)

    e11.grid(row=1, column=1)

    Button(root3,
              text='Save',
              command=ajout_field_save).grid(row=3,column=0)


    root3.mainloop()
def Delete_Field_save():
    print(str(e2.get()))
    print(str(e21.get()))
    arcpy.DeleteField_management(str(e2.get()),str(e21.get()))
    print("Field Deleted")

def Delete_Field():

    root4 = Tk()
    root4['background'] = '#58F'
    global e2
    Label(root4,
             text="Table").grid(row=0)


    e2 = Entry(root4)

    e2.grid(row=0, column=1)
    global e21
    Label(root4,
             text="Fild").grid(row=1)


    e21 = Entry(root4)

    e21.grid(row=1, column=1)

    Button(root4,
              text='Delete',
              command=Delete_Field_save).grid(row=3,column=0)


    root4.mainloop()



def ajout_Line_save():
    lll=[]
    for l_f in ll:
        lll.append(int(l_f.get()))
    print(lll)
    print(l)
    path=r'C:\Users\Brahima\Desktop\cartes Maroc\s1.gdb'
    cursor = arcpy.da.InsertCursor(os.path.join(path,str(e5.get())),l)
    cursor.insertRow(lll)
    print("line Ajouter")
def ajout_Line_suite():

    root51 = Tk()
    root51['background'] = '#58F'
    root51.geometry("200x200")
    print(str(e5.get()))
    global ll;
    global l;
    ll=[]
    l=[]
    path=r'C:\Users\Brahima\Desktop\cartes Maroc\s1.gdb'
    champ_table=arcpy.ListFields(os.path.join(path,str(e5.get())))
    for field in champ_table:
        l.append(str(field.name))
    l.remove('OBJECTID')
    l.remove('SHAPE')
    i=0
    for l_f in l:
        Label(root51, text=l_f).grid(row=i)
        e52 = Entry(root51)
        e52.grid(row=i, column=1)
        ll.append(e52)
        i=i+1
    Button(root51,
              text='Save',
              command=ajout_Line_save).grid(row=i+2,column=0)
    #arcpy.AddField_management(str(e1.get()),str(e11.get()),"LONG")

    print("Feild Ajouter")
    root51.mainloop()

def ajout_Line():

    root5 = Tk()
    root5['background'] = '#58F'
    root5.geometry("200x200")
    global e5
    global e51
    Label(root5,
             text="Table").grid(row=0)


    e5 = Entry(root5)

    e5.grid(row=0, column=1)



    Button(root5,
              text='Suivant',
              command=ajout_Line_suite).grid(row=3,column=0)


    root5.mainloop()

def Delete_Line_save():
    print(e6.get())
    print(e61.get())
    path=r'C:\Users\Brahima\Desktop\cartes Maroc\s1.gdb'
    cursor = arcpy.da.UpdateCursor(os.path.join(path,str(e6.get())),["OBJECTID"])
    for row in cursor:
        if row[0] == int(e61.get()):
            cursor.deleteRow()
def Delete_Line():

    root6 = Tk()
    root6['background'] = '#58F'
    global e6
    Label(root6,
             text="Table").grid(row=0)


    e6 = Entry(root6)

    e6.grid(row=0, column=1)
    global e61
    Label(root6,
             text="OBEJECTID").grid(row=1)


    e61 = Entry(root6)

    e61.grid(row=1, column=1)

    Button(root6,
              text='Delete',
              command=Delete_Line_save).grid(row=3,column=0)


    root6.mainloop()

def modifier_Line_save():
    lll=[]
    for l_f in ll:
        lll.append(int(l_f.get()))
    print(lll)
    print(l)
    path=r'C:\Users\Brahima\Desktop\cartes Maroc\s1.gdb'
    cursor=arcpy.da.UpdateCursor(os.path.join(path,str(e7.get())),l0)
    for row in cursor:
        if row[len(l0)-1]==int(e71.get()):
            for i in range(len(l0)-1):
                row[i]  =  lll[i]

            #row[1] ='pere'+str(row[0])
            cursor.updateRow(row)


def modifier_Line_Suivant():

    print(str(e7.get()))
    print(str(e71.get()))
    root71 = Tk()
    root71['background'] = '#58F'
    root71.geometry("200x200")
    global ll;
    global l0;
    global l;
    ll=[]
    ll0=[]
    l=[]
    path=r'C:\Users\Brahima\Desktop\cartes Maroc\s1.gdb'
    champ_table=arcpy.ListFields(os.path.join(path,str(e7.get())))
    for field in champ_table:
        l.append(str(field.name))
    l.remove('OBJECTID')
    l.remove('SHAPE')
    i=0
    l0=list(l)
    l0.append('OBJECTID')
    cursor = arcpy.da.SearchCursor(str(e7.get()), l0) #suivant valeur 3
    for row in cursor:
        if(row[len(l)]==int(e71.get())):
            ll0=list(row[0:len(l)])



    for l_f in l:
        Label(root71, text=l_f ).grid(row=i)
        name = StringVar(root71, value=ll0[i])
        e72 = Entry(root71, textvariable=name)
        e72.grid(row=i, column=1)
        ll.append(e72)
        i=i+1
    Button(root71,
              text='Save',
              command=modifier_Line_save).grid(row=i+2,column=0)
    #arcpy.AddField_management(str(e1.get()),str(e11.get()),"LONG")

    print("Feild")
    root71.mainloop()

def modifier_ligne():

    root7 = Tk()
    root7['background'] = '#58F'
    global e7
    Label(root7,
             text="Table").grid(row=0)


    e7 = Entry(root7)

    e7.grid(row=0, column=1)
    global e71
    Label(root7,
             text="OBEJECTID").grid(row=1)


    e71 = Entry(root7)

    e71.grid(row=1, column=1)

    Button(root7,
              text='Suivant',
              command=modifier_Line_Suivant).grid(row=3,column=0)


    root7.mainloop()

root = Tk()
root['background'] = '#58F'
root.geometry("500x500")
btn_height = Button(root, text="Show Feild",bg = "red",command=ShowFeild_All_tables)
btn_height.place(height=50,width=60, x=200, y=50)
btn_width = Button(root, text="Show Line",command=ShowLine_All_Line)
btn_width.place(height=50,width=60, x=50, y=50)
btn_relheight = Button(root, text="Ajouter Field",command=ajout_field)
btn_relheight.place(height=50,width=180, x=300, y=50)
btn_relwidth= Button(root, text="Delete Field" ,background = "#856ff8",command=Delete_Field)
btn_relwidth.place(height=50,width=240, x=5, y=150)
btn_relx=Button(root, text="Show Table",background = "yellow",command=ShowTable)
btn_relx.place(height=50,width=100, x=180, y=250)
btn_rely=Button(root, text="Ajout Line",background = "#856ff8",command=ajout_Line)
btn_rely.place(height=50,width=240, x=255, y=150)
btn_rely=Button(root, text="Delete Line",command=Delete_Line)
btn_rely.place(height=50,width=120, x=5, y=350)
btn_rely=Button(root, text="Modifier Ligne",command=modifier_ligne)
btn_rely.place(height=50,width=120, x=350, y=350)

root.mainloop()


