from tkinter import *
from random import randint
from tkinter import ttk

root = Tk()
root.title("Tahvel")
root.geometry("500x700")
tahvel = Canvas(root, width=500, height=700)
tahvel.grid()
#Pildid
kivi = PhotoImage(file='graafika/kivi.gif')
paber = PhotoImage(file='graafika/paber.gif')
Käärid = PhotoImage(file='graafika/k22rid.gif')

pildi_list = [kivi, paber, Käärid] #Lisab pildid listi

valiku_number = randint(0,2) #Valib random numbri nullist kaheni
# img = tahvel.create_image(0, 0, anchor=NW, image=pildi_list[valiku_number])

image_label = Label(root, image=pildi_list[valiku_number])
image_label.place(x=0, y=0,anchor=NW, width=500)
# võidu_kiri = Label(root, text="")
def keeruta():
    suvaline_number = randint(0,2)
    image_label.config(image=pildi_list[suvaline_number])
    
    if kasutaja_valik.get() == "Kivi":
        kasutaja_valik_value = 0
    elif kasutaja_valik.get() == "Paber":
        kasutaja_valik_value = 1    
    else:
        kasutaja_valik_value = 2
        
    if kasutaja_valik_value == 0: #väärtus on kivi
        if suvaline_number == 0:
            võidu_kiri.config(text="Jäid viiki, keeruta uuesti")
        elif suvaline_number == 1: # väärtus on paber
            võidu_kiri.config(text="Paber alistab kivi, Sa kaotasid")
        elif suvaline_number == 2: # väärtus on Käärid
            võidu_kiri.config(text="Kivi alistab Käärid, Sa võitsid")
            
    if kasutaja_valik_value == 1: #väärtus on paber
        if suvaline_number == 1:
            võidu_kiri.config(text="Jäid viiki, keeruta uuesti")
        elif suvaline_number == 0: # väärtus on kivi
            võidu_kiri.config(text="Paber alistab kivi, Sa võitsid!")
        elif suvaline_number == 2: # väärtus on Käärid
            võidu_kiri.config(text="Käärid alistab paberi, Sa kaotasid!")
    
    if kasutaja_valik_value == 2: #väärtus on Käärid
        if suvaline_number == 2:
            võidu_kiri.config(text="Jäid viiki, keeruta uuesti")
        elif suvaline_number == 0: # väärtus on kivi
            võidu_kiri.config(text="Kivi alistab Käärid, Sa kaotasid!")
        elif suvaline_number == 1: # väärtus on paber
            võidu_kiri.config(text="Käärid alistab paberi, Sa võitsid!")
            
kasutaja_valik = ttk.Combobox(root, value=("Kivi", "Paber", "Käärid"))#Teed valiku
kasutaja_valik.current(0)
kasutaja_valik.place(x=165, y=570, width=170)
#kasutaja_valik.pack(pady=20)

keeruta_nupp = ttk.Button(root, text="Keeruta!", command=keeruta)#Loob keerutamis nupu
keeruta_nupp.place(x=165, y=600, width=170)
#keeruta_nupp.pack(pady=10)


võidu_kiri = Label(root, text="")#Näitab, kas võitisid või mitte
võidu_kiri.place(x=165, y=550, width=170)
#võidu_kiri.pack(pady=50)

root.mainloop()