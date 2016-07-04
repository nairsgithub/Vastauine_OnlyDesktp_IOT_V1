#More IOT on (www.vastauine.com)
from Tkinter import *
vastauine=Tk()
#vastauine.minsize(width=666, height=666)
vastauine.title("VASTAUINE RPI2 GPIO GUI")
vastauine.configure(background='black')


  #................................................................#

def ONGPI(var,pin,display):
    var.configure(text=display,fg="white",font=700, bg="green",width=15, height=3,command= lambda : OFFGPI(var,pin,display))

    print("Turning Lights ON")
    #label = Label(myvar, text="Lights Have Switched ON",fg="black", bg="green")
    #label.pack()
    
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,True)
    
#.................................................................#    

def OFFGPI(var,pin,display):
    var.configure(text=display,fg="white",font=700, bg="red",width=15, height=3,command= lambda : ONGPI(var,pin,display))

    print("Turning Lights OFF")
    #label = Label(master, text="Lights have Switched OFF",fg="black", bg="red")
    #label.pack()
    import RPi.GPIO as GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin,GPIO.OUT)
    GPIO.output(pin,False)

#................................................................#  


def fun_buttons():
   
    but0_plus3v=Button(text='+3v3',font=700,fg="navy", bg="deepskyblue",width=15, height=3)
    #but0_plus3v.pack()
    but0_plus3v.grid(row=1,column=3)

    but1_GP2=Button(text='GPIO2/SDA1',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but1_GP2,2,'GPIO2/SDA1'))
    but1_GP2.grid(row=2,column=3)
    #but1_GP2.pack()

    but2_GP3=Button(text='GPIO3/SCL1',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but2_GP3,3,'GPIO3/SCL1'))
    #but2_GP3.pack()
    but2_GP3.grid(row=3,column=3)

    but3_GP4=Button(text='GPIO4',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but3_GP4,4,'GPIO4'))
    #but2_GP4.pack()
    but3_GP4.grid(row=4,column=3)

    but4_GND=Button(text='GND',font=700,fg="white", bg="black",width=15, height=3)
    #but3_GND.pack()
    but4_GND.grid(row=5,column=3)

    but5_GP17=Button(text='GPIO17',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but5_GP17,17,'GPIO17'))
    #but4_GP17.pack()
    but5_GP17.grid(row=6,column=3)

    but6_GP27=Button(text='GPIO27',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but6_GP27,27,'GPIO27'))
    #but5_GP27.pack()
    but6_GP27.grid(row=7,column=3)

    but7_GP22=Button(text='GPIO22',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but7_GP22,22,'GPIO22'))
    #but6_GP22.pack()
    but7_GP22.grid(row=8,column=3)

    but8_plus3v=Button(text='+3v3',font=700,fg="navy", bg="deepskyblue",width=15, height=3)
    #but7_plus3v.pack()
    but8_plus3v.grid(row=9,column=3)

    but9_GP10=Button(text='GPIO10/MOSI',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but9_GP10,10,'GPIO10/MOSI'))
    #but8_GP10.pack()
    but9_GP10.grid(row=10,column=3)

    but10_GP9=Button(text='GPIO9/MISO',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but10_GP9,9,'GPIO9/MISO'))
    #but9_GP9.pack()
    but10_GP9.grid(row=1,column=4)

    but11_GP11=Button(text='GPIO11/SCLK',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but11_GP11,11,'GPIO11/SCLK'))
    #but10_GP11.pack()
    but11_GP11.grid(row=2,column=4)

    but12_GND=Button(text='GND',font=700,fg="white", bg="black",width=15, height=3)
    #but12_GND.pack()
    but12_GND.grid(row=3,column=4)

    but13_GP0=Button(text='GPIO0/ID_SD',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but13_GP0,0,'GPIO0/ID_SD'))
    #but12_GP0.pack()
    but13_GP0.grid(row=4,column=4)

    but14_GP5=Button(text='GPIO5',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but14_GP5,5,'GPIO5'))
    #but13_GP5.pack()
    but14_GP5.grid(row=5,column=4)
    

    but15_GP6=Button(text='GPIO6',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but15_GP6,6,'GPIO6'))
    #but14_GP6.pack()
    but15_GP6.grid(row=6,column=4)

    but16_GP13=Button(text='GPIO13',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but16_GP13,13,'GPIO13'))
    #but15_GP2.pack()
    but16_GP13.grid(row=7,column=4)

    but17_GP19=Button(text='GPIO19/MISO',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but17_GP19,19,'GPIO19/MISO'))
    #but16_GP2.pack()
    but17_GP19.grid(row=8,column=4)

    but18_GP26=Button(text='GPIO26',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but18_GP26,26,'GPIO26'))
    #but17_GP2.pack()
    but18_GP26.grid(row=9,column=4)
    

    but19_GND=Button(text='GND',font=700,fg="white", bg="black",width=15, height=3)
    #but18_GP2.pack()
    but19_GND.grid(row=10,column=4)

    #..............................Second Side Button...........................................#
    
    but20_GP21=Button(text='GPIO21/SCLK',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but20_GP21,20,'GPIO21/SCLK'))
    but20_GP21.grid(row=1,column=7)

    but21_GP20=Button(text='GPIO20/MOSI',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but21_GP20,21,'GPIO20/MOSI'))
    but21_GP20.grid(row=2,column=7)

    but22_GP16=Button(text='GPIO16/CE2#',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but22_GP16,16,'GPIO16/CE2#'))
    but22_GP16.grid(row=3,column=7)

    but23_GND=Button(text='GND',font=700,fg="white", bg="black",width=15, height=3)
    but23_GND.grid(row=4,column=7)

    but24_GP12=Button(text='GPIO12',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but24_GP12,12,'GPIO12'))
    but24_GP12.grid(row=5,column=7)

    but25_GND=Button(text='GND',font=700,fg="white", bg="black",width=15, height=3)
    but25_GND.grid(row=6,column=7)

    but26_GP1=Button(text='GPIO1/ID_SC',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but26_GP1,1,'GPIO1/ID_SC'))
    but26_GP1.grid(row=7,column=7)

    but27_GP7=Button(text='GPIO7/CE1#',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but27_GP7,7,'GPIO7/CE1#'))
    but27_GP7.grid(row=8,column=7)

    but28_GP8=Button(text='GPIO8/CE0#',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but28_GP8,8,'GPIO8/CE0#'))
    but28_GP8.grid(row=9,column=7)

    but29_GP25=Button(text='GPIO25',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but29_GP25,25,'GPIO25'))
    but29_GP25.grid(row=10,column=7)

    but30_GND=Button(text='GND',font=700,fg="white", bg="black",width=15, height=3)
    but30_GND.grid(row=1,column=8)

    but31_GP24=Button(text='GPIO24',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but31_GP24,24,'GPIO24'))
    but31_GP24.grid(row=2,column=8)
    
    but32_GP23=Button(text='GPIO23',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but32_GP23,23,'GPIO23'))
    but32_GP23.grid(row=3,column=8)

    but33_GND=Button(text='GND',font=700,fg="white", bg="black",width=15, height=3)
    but33_GND.grid(row=4,column=8)
    
    but34_GP18=Button(text='GPIO18',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but34_GP18,18,'GPIO18'))
    but34_GP18.grid(row=5,column=8)

    but35_GP15=Button(text='RXD0/GPIO15',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but35_GP15,15,'RXD0/GPIO15'))
    but35_GP15.grid(row=6,column=8)
    
    but36_GP14=Button(text='GPIO14/TXD0',font=700,fg="white", bg="red",width=15, height=3,command= lambda: ONGPI(but36_GP14,14,'GPIO14/TXD0'))
    but36_GP14.grid(row=7,column=8)

    but37_GND=Button(text='GND',font=700,fg="white", bg="black",width=15, height=3)
    but37_GND.grid(row=8,column=8)
    
    but38_plus5v=Button(text='+5v',font=700,fg="navy", bg="deepskyblue",width=15, height=3)
    but38_plus5v.grid(row=9,column=8)

    but39_plus5v=Button(text='+5v',font=700,fg="navy", bg="deepskyblue",width=15, height=3)
    but39_plus5v.grid(row=10,column=8)

    #.......................................DECORFUX.......................................................#



print("Sucessfully Initialised ")
fun_buttons()
vastauine.mainloop()
   
