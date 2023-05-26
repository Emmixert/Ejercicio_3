from tkinter import Tk,Frame,Label,PhotoImage,Button

root=Tk()
root.geometry("1740x865")
root.config(bg="Green")
root.resizable(0,0)
root.iconbitmap("favicon1.ico")
root.title("SPAI 4.0")

settings=PhotoImage(file= r"lel.png")
green=PhotoImage(file= r"green.png")
red=PhotoImage(file= r"red.png")
red_meter=PhotoImage(file= r"red_meter.png")
water_meter=PhotoImage(file= r"water_tank.png")
green_meter=PhotoImage(file= r"green_meter.png")
yellow_meter=PhotoImage(file= r"yellow_meter.png")
graph=PhotoImage(file= r"graph.png")

#Frames

#Main Frame
frMain=Frame(root)
frMain.place(x=0,y=100,width=1890,height=765)
frMain.config(bg="Black")

#Frame 1
fr1=Frame(frMain)
fr1.place(x=150,y=10,width=270,height=400)
fr1.config(bg="Gray",bd=2,relief="ridge")

#Frame 2
fr2=Frame(frMain)
fr2.place(x=430,y=10,width=490,height=400)
fr2.config(bg="Gray",bd=2,relief="ridge")

#Frame 3
fr3=Frame(frMain)
fr3.place(x=150,y=420,width=380,height=335)
fr3.config(bg="Gray",bd=2,relief="ridge")

#Frame 4
fr4=Frame(frMain)
fr4.place(x=540,y=420,width=380,height=335)
fr4.config(bg="Gray",bd=2,relief="ridge")

#Frame 5
fr5=Frame(frMain)
fr5.place(x=930,y=10,width=670,height=550)
fr5.config(bg="Gray",bd=2,relief="ridge")



#Labels

#Title Label 1
ttLbl1=Label(fr1,text="Indicadores Digitales")
ttLbl1.place(x=10,y=10)
ttLbl1.config(bg="Gray",fg="Cyan",font=("Calibri",20,"bold"))

#Title Label 2
ttLbl2=Label(fr2,text="Temperaturas")
ttLbl2.place(x=10,y=10)
ttLbl2.config(bg="Gray",fg="Cyan",font=("Calibri",20,"bold"))

#Title Label 3
ttLbl3=Label(fr3,text="Velocidad Bomba")
ttLbl3.place(x=90,y=40)
ttLbl3.config(bg="Gray",fg="White",font=("Calibri",20,"bold"))

#Title Label 4
ttLbl4=Label(fr4,text="Nivel De Tanque")
ttLbl4.place(x=10,y=10)
ttLbl4.config(bg="Gray",fg="Cyan",font=("Calibri",20,"bold"))

#Title Label 5
ttLbl5=Label(fr5,text="Produccion")
ttLbl5.place(x=10,y=10)
ttLbl5.config(bg="Gray",fg="Cyan",font=("Calibri",20,"bold"))


#Inside Frame 1 Labels
line1=Label(fr1,text="Linea 1:")
line1.place(x=10,y=70)
line1.config(bg="Gray",fg="White",font=("Calibri",15))

line2=Label(fr1,text="Linea 2:")
line2.place(x=10,y=120)
line2.config(bg="Gray",fg="White",font=("Calibri",15))

line3=Label(fr1,text="Linea 3:")
line3.place(x=10,y=170)
line3.config(bg="Gray",fg="White",font=("Calibri",15))

desk=Label(fr1,text="Gabinete:")
desk.place(x=10,y=220)
desk.config(bg="Gray",fg="White",font=("Calibri",15))

alarm1=Label(fr1,text="Alarm 1:")
alarm1.place(x=10,y=270)
alarm1.config(bg="Gray",fg="White",font=("Calibri",15))

alarm2=Label(fr1,text="Alarm 2:")
alarm2.place(x=10,y=320)
alarm2.config(bg="Gray",fg="White",font=("Calibri",15))

on_off1=Label(fr1,text="On")
on_off1.place(x=130,y=70)
on_off1.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))

on_off2=Label(fr1,text="On")
on_off2.place(x=130,y=120)
on_off2.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))

on_off3=Label(fr1,text="On")
on_off3.place(x=130,y=170)
on_off3.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))

on_off4=Label(fr1,text="Abierto")
on_off4.place(x=130,y=220)
on_off4.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))

on_off5=Label(fr1,text="On")
on_off5.place(x=130,y=270)
on_off5.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))

on_off6=Label(fr1,text="Off")
on_off6.place(x=130,y=320)
on_off6.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))

green_red1=Label(fr1,image=green)
green_red1.place(x=220,y=70)
green_red1.config(bg="Gray")

green_red2=Label(fr1,image=green)
green_red2.place(x=220,y=120)
green_red2.config(bg="Gray")

green_red3=Label(fr1,image=green)
green_red3.place(x=220,y=170)
green_red3.config(bg="Gray")

green_red4=Label(fr1,image=red)
green_red4.place(x=220,y=220)
green_red4.config(bg="Gray")

green_red5=Label(fr1,image=red)
green_red5.place(x=220,y=270)
green_red5.config(bg="Gray")

green_red6=Label(fr1,image=green)
green_red6.place(x=220,y=320)
green_red6.config(bg="Gray")

red_met=Label(fr3,image=red_meter)
red_met.place(x=60,y=100)
red_met.config(bg="Gray")

water_met=Label(fr4,image=water_meter)
water_met.place(x=65,y=60)
water_met.config(bg="Gray")

temp1=Label(fr2,text="Temperatura 1")
temp1.place(x=60,y=100)
temp1.config(bg="Gray",fg="White",font=("Calibri",15))

temp2=Label(fr2,text="Temperatura 2")
temp2.place(x=280,y=100)
temp2.config(bg="Gray",fg="White",font=("Calibri",15))

temp11=Label(fr2,image=green_meter)
temp11.place(x=20,y=170)
temp11.config(bg="Gray")

temp22=Label(fr2,image=yellow_meter)
temp22.place(x=245,y=170)
temp22.config(bg="Gray")

temp111=Label(fr2,text="Temp. Agua:")
temp111.place(x=150,y=320)
temp111.config(bg="Gray",fg="White",font=("Calibri",15))

temp222=Label(fr2,text="Temp. Ambiente:")
temp222.place(x=110,y=350)
temp222.config(bg="Gray",fg="White",font=("Calibri",15))

temp1111=Label(fr2,text="58°C")
temp1111.place(x=270,y=320)
temp1111.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))

temp2222=Label(fr2,text="32°C")
temp2222.place(x=270,y=350)
temp2222.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))

gph=Label(fr5,image=graph)
gph.place(x=10,y=60)
gph.config(bg="Gray")

gphLb1=Label(fr5,text="Piezas Producidas:")
gphLb1.place(x=230,y=440)
gphLb1.config(bg="Gray",fg="White",font=("Calibri",15))

gphLb2=Label(fr5,text="Piezas Defectuoas:")
gphLb2.place(x=230,y=480)
gphLb2.config(bg="Gray",fg="White",font=("Calibri",15))

gphLb11=Label(fr5,text="50")
gphLb11.place(x=390,y=440)
gphLb11.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))

gphLb22=Label(fr5,text="12")
gphLb22.place(x=390,y=480)
gphLb22.config(bg="Gray",fg="White",font=("Calibri",15,"bold"))


#Settings Label
lblSett=Label(root,text="SPAI 4.0")
lblSett.place(x=100,y=20)
lblSett.config(font=("Calibri",30),fg="White",bg="Green")


#Buttons

#Settings Button
btnSett=Button(root,image=settings)
btnSett.place(x=20,y=20)
btnSett.config(bg="Green")

root.mainloop()