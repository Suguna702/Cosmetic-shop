from tkinter import
import math.random
from tkinter import messagebox
import os
import smtplib
from tkinter import Tk, Label, Frame, Entry, Button
from subprocess import Popen

class Bill_App:
def_init__(self, master):
self.master-master
self.master.geometry("1920x1080+-10+0")
self.master.title("shop management system")

title Label(self.master,text="SHOP
MANAGEMENT",bd=12, relief GROOVE.bg="sky blue", font=("times
new roman",30,"bold").pady=2).pack(fill=X)

#variable
#cosmatic variable

self.soap-IntVar()
self.facecream-IntVar()
self.facewash-IntVar()
self.hair_spry-IntVar()
self.hair_gel-IntVar()
self.body_lotion IntVar()

#grocery varible
self.maggie-IntVar()
self.rice IntVar()
self.wheat IntVar()
self.food_oil-IntVar()
self.daal-IntVar()
self.sugar-IntVar()

#cold drink
self.maza-IntVar()
self.coca_cola-IntVar()
self.thumbs_up-IntVar()
self.slice IntVar()
self.frooti IntVar()
self.pepsi-IntVar()

#biscuit varible
self.parle IntVar()
self.britania IntVar()
self.goodday IntVar()
self.oreo-IntVar()
self.sunfist-IntVar()
self.monaco-IntVar()

#product price varible
self.cosmetic_price=StringVar()
self.grocery_price=StringVar()
self.cold_drink_price=StringVar()
self.biscuit_price=StringVar()

#tax varible
self.cosmetic_tax-StringVar()
self.grocery_tax-StringVar()
self.cold_drink_tax=StringVar()
self.biscuit_tax-StringVar()

#customer details
self.c_name=StringVar()
self.c_phon-StringVar()
self.c_mail-StringVar()
self.bill_no-StringVar()
self.search_bill-StringVar()
x=random.randint(1000,9999)
self.bill_no.set(str(x))

#admin
self.admin_id=StringVar()
self.admin_pass-StringVar()

#>>> CUSTOMER DETAILS <<<<<<
F0=LabelFrame(self.master.bd=10.relief-GROOVE.text="Customer Details", font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
F0.place(x=0,y=70,width=950)

cname_label=Label(F0.text="Customer Name",bg="sky blue" font=("times new
romen",18,"bold")).grid(row=0,column=0,padx=20.pady=5)
cname_txt=Entry(F0,width-20,textvariable=self.c_name.font="arial15",bd=7,relief=SUNKEN).grid(row=0,column=1,pady= 5,padx=10)

cphu_label-Label(F0,text="PhoneNo.",bg="skyblue",font-("timesnew romen",18,"bold")).grid(row=0.column=2,padx=20,pady=5)
cphn_txt=Entry(F0,width=20,textvariable=self.c_phon,font="arial15",hd=7,relief=SUNKEN).grid(row=0,column=3,pady=5,padx=10)

# send email button
F1-LabelFrame(self.master.bd-10.relief GROOVE,text="send bill via Email ",font=("times new roman",15,"bold").fg="gold",bg="sky blue")
F1.place(x=950,y=70,width=587)

cmail_label-Label(F1,text="Email",bg="skyblue",font=("timesnew",18,"bold")).grid(row=0,column=4,padx=20,pady=5)
cmail_txt=Entry(F1,width=20,textvariable=self.c_mail,font="arial15",bd=7,relief=SUNKEN).grid(row=0.column=5,pady=5,padx=10)

#bn_txt=Entry(F9,width=18,textvariable=self.search_bill,font="arial10 bold",bd=7,relief=SUNKEN).grid(row=0.column=1,padx=30,pady=1)

send_btn-Button(F1,text="Send",bg="cyan",bd=5.fg="black",width=8,font="arial12 bold").grid(row=0,column=7) #enter this line :- command=self.check_mail

#>>>>> Cosmetic frame <<<

F2-LabelFrame(self.master,bd=10,relief=GROOVE,text="Cosmetic",font=("timesnew roman",15,"bold"),fg="gold",bg="sky blue")
F2.place(x=5,y-152,width=277,height=393)

bath_txt=Entry(F2,width=2,textvariable=self.soap.font=("timesnew roman",16,"bold"),bd=5,relief-SUNKEN).grid(row=0,column=1,padx=10, pady 10,sticky-W)

bath_label-Label(F2, text="Bath Soap",font=("times new roman",16,"bold"),fg="black",bg="sky
blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")

#face cream
facecream_label-Label(F2,text="FaceCream",font=("timesnew roman",16,"bold"),fg="black",bg="sky
blue").grid(row=1,column=0,padx=10,pady=10,sticky="w")

facecream_txt=Entry(F2,width=2,textvariable=self.facecream,font=("times new
roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10, pady=10,sticky=W)

#Facewash
facewash_label-Label(F2,text="Facewash",font=("times new an",16,"bold"),fg="black",bg="sky
blue").grid(row=2.column=0.padx=10,pady=10,sticky="w")

facewash_txt=Entry(F2,width=2,textvariable=self.facewash,font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10, pady=10,sticky=W)

#hair spray
hair_Spry_label-Label(F2,text="Hair Spray",font=("times new
roman", 16, "bold"),fg="black",bg="sky
blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")

hair_spry_txt=Entry(F2,width=2,textvariable=self.hair_spry.font=("times
newroman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10, pady=10,sticky=W)

#Hair gel
hair_gel_label=Label(F2,text="HairGel",font=("timesnew roman",16,"bold"),fg="black".bg="skyblue").grid(row=4.column=0,padx=10,pady=10,sticky="w")
hair_gel_txt=Entry(F2,width=2.textvariable=self.hair_gel.font=("times
newroman",16","bold"),bd=5,relief=SUNKEN).grid(row=4,column=1.padx=10, pady=10,sticky-W)

#bodylotion
body_It_label-Label(F2,text="Body Lotion", font=("times new ",16,"bold"),fg="black",bg="sky
blue").grid(row=5.column=0,padx=10.pady=10,sticky="w")

body_lt_txt=Entry(F2,width=2,textvariable=self.body_lotion.font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1.padx=10, pady-10,sticky-W)

#you can use scroll bar here for frame

#bath_shampoo_label=Label(F2,text="Bath Shampoo",font=("times new
roman",16,"bold"),fg="black",bg="tomato").grid(row=6,column=0,padx= 10,pady=10,sticky="w")
#bath_shampoo_txt=Entry(F2,width=10.font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=6,column=1,padx=10, pady=10)

#bath_shampoo_label-Label(F2,text="hair oil", font=("times new
roman",16,"bold"),fg="black",bg="tomato").grid(row=7,column=0,padx= 10,pady=10,sticky="w")
#bath_shampoo_txt=Entry(F2,width=10.font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=7,column=1.padx=10, pady=10)

#>>>>> Groccery frame <<<

F3-LabelFrame(self.master,bd=10,relief=GROOVE,text="Grocery",font=("timesnew roman",15,"bold"),fg="gold",bg="sky blue")
F3.place(x=276,y=152,width=220,height=393)

gl_label=Label(F3,text="Meggie", font=("times new roman",16,"bold"),fg="black",bg="sky blue").grid(row=0.column=0,padx=10,pady=10,sticky="w")
gl_txt=Entry(F3,width=4,textvariable=self.maggie.font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1.padx=10, pady=10,sticky=W)

g2_label-Label(F3.text="Rice" font=("times new roman", 16, "bold"),fg="black",bg="sky blue").grid(row-1.column=0,padx=10,pady=10,sticky="w")
g2_txt=Entry(F3,width=4,textvariable=self.rice,font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10, pady=10,sticky-W)

g3_label-Label(F3,text="Wheat",font=("times new roman",16,"bold"),fg="black".bg="sky
blue").grid(row=2.column=0,padx=10,pady=10,sticky="w")
g3_txt=Entry(F3,width=4,textvariable=self.wheat,font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2.column=1,padx=10, pady=10,sticky-W)

g4_label-Label(F3,text="Food oil", font=("times new
roman",16, "bold"),fg="black",bg="skyblue").grid(row=3.column=0,padx=10.pady=10,sticky="w")
g4_txt=Entry(F3,width=4,textvariable=self.food_oil,font=("times new roman",16,"bold"),bd-5,relief-SUNKEN).grid(row=3,column=1,padx=10, pady 10,sticky-W)

g5_label-Label(F3,text="Daal", font=("times new
roman",16,"bold"),fg="black",bg="sky
blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
g5_txt=Entry(F3,width=4,textvariable=self.daal,font=("timesnewromon” ,16,”bold”),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10, pady=10,sticky=W)

g6_label=Label(F3,text="Sugar", font=("times new
roman",16,"bold"),fg="black",bg="sky
blue").grid(row=5,column=0,padx=10,pady=10,sticky="w")
g6_txt=Entry(F3,width=4,textvariable=self.sugar.font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10, pady-10,sticky-W)

# >>>>> cold-drink frame <<<-

F4-LabelFrame(self.master,bd=10,relief GROOVE,text="Cold Drink", font=("times new roman", 15,"bold"),fg="gold",bg="sky blue")
F4.place(x=490,y=152,width=220,height=393)

cl_label-Label(F4,text="Maza", font=("times new
roman",16,"bold"),fg="black",bg="sky
blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
cl_txt=Entry(F4,width=4,textvariable=self.maza.font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1,padx=10, pady=10,sticky=W)

c2_label-Label(F4.text- xt="Coca cola", font=("times new roman", 16, "bol "bold").fg="1 ="black",bg="sky
blue").grid(row=1.colum column=0,padx=10,pady=10,sticky="w")
c2_txt=Entry(F4,width=4,textvariable=self.coca_cola,font=("times
new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1.column=1,padx=10, pady=10,sticky-W)

c3_label-Label(F4,text="Thumbs-up",font=("times new roman",16,"bold"),fg="black".bg="sky blue").grid(row=2,column=0.padx=10,pady=10.sticky="w")
c3_txt=Entry(F4,width=4,textvariable=self.thumbs_up,font=("times
new roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10, pady=10,sticky-W)

c4_label-Label(F4,text="Slice", font=("times new
roman",16,"bold").fg="black".bg="sky
blue").grid(row=3.column=0,padx=10,pady=10,sticky="w")
c4_txt=Entry(F4,width=4,textvariable=self.slice,font=("times new roman",16,"bold"), bd=5, relief=SUNKEN).grid(row=3,column=1,padx=10, pady-10,sticky-W)

c5_label-Label(F4,text="Frooti",font=("times new
roman",16,"bold"),fg="black",bg="sky
blue").grid(row=4,column=0,padx=10.pady=10,sticky="w")
c5_txt=Entry(F4,width=4,textvariable=self.frooti.font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10.pady=10,sticky=w)

c6_label=Label(F4,text="Pepsi",font=("times new
roman",16,"bold"),fg="black",bg="sky
blue").grid(row=5.column=0,padx=10,pady=10,sticky="w")
c6_txt=Entry(F4,width=4,textvariable=self.pepsi,font=("timesnewroman",16, "bold").bd=5,relief=SUNKEN).grid(row=5.column=1.padx=10, pady=10,sticky-W)

#>>>>> Biscuit frame <<<

F4-LabelFrame(self.master,bd=10,relief=GROOVE,text="Biscuits",font=("timesnew roman",15,"bold"),fg="gold",bg="sky blue")
F4.place(x=705,y=152,width=230,height=393)

c1_label-Label(F4,text="Parle-G",font=("times new roman",16,"bold"),fg="black",bg="sky
blue").grid(row=0,column=0,padx=10,pady=10,sticky="w")
cl_txt=Entry(F4,width=4,textvariable=self.parle,font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=0,column=1.padx=10, pady=10,sticky=W)

c2_label-Label(F4,text="Britania",font=("times new roman",16,"bold"),fg="black",bg="sky
blue").grid(row=1.column=0,padx=10,pady=10,sticky="w")
c2_txt=Entry(F4,width=4,textvariable=self.britania,font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=1,column=1,padx=10, pady=10,sticky-W)

c3_label-Label(F4,text="Oreo", font=("times new
roman",16,"bold"),fg="black",bg="sky blue").grid(row=2,column=0,padx=10,pady=10,sticky="w")
c3_txt=Entry(F4,width=4,textvariable=self.oreo,font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=2,column=1,padx=10, pady=10,sticky-W)

c4_label-Label(F4,text="Good Day", font=("times new roman",16,"bold"),fg="black",bg="sky
blue").grid(row=3,column=0,padx=10,pady=10,sticky="w")
c4_txt=Entry(F4,width=4,textvariable=self.goodday,font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=3,column=1,padx=10, pady=10,sticky=W)

c5_label-Label(F4,text="Sunfist", font=("times new
roman",16,"bold"),fg="black",bg="sky blue").grid(row=4,column=0,padx=10,pady=10,sticky="w")
c5_txt=Entry(F4,width=4,textvariable=self.sunfist.font=("timesnewroman",16, "bold"),bd=5,relief=SUNKEN).grid(row=4,column=1,padx=10, pady=10,sticky-W)

c6_label=Label(F4,text="Monaco", font=("times new
roman",16,"bold"),fg="black",bg="sky
blue").grid(row=5.column=0,padx=10,pady=10,sticky="w")
c6_txt=Entry(F4,width=4,textvariable=self.monaco,font=("timesnew roman",16,"bold"),bd=5,relief=SUNKEN).grid(row=5,column=1,padx=10, pady=10,sticky=W)

>>>>> image frame <<<--

self.image_section()

#bill Area............

F6-LabelFrame(self.master,bd=10,relief=GROOVE)
F6.place(x=1160,y=152,width=380,height=393)
bill_title=Label(F6,text="Bill Area" font="arial 15
bold".bd=7,relief GROOVE).pack(fill=X)

scrol_y=Scrollbar(F6,orient=VERTICAL)
self.txtarea=Text(F6,yscrollcommand=scrol_y.set)
scrol_y.pack(side=RIGHT,fill=Y)
serol_y.config(command=self.txtarea.yview)
self.txtarea.pack(fill=BOTH.expand=1)

#bottom button frame-

F7-LabelFrame(self.master,bd=10,relief GROOVE,text="Bill
Menu",font=("times new roman",15,"bold"),fg="gold",bg="sky blue")
F7.place(x=0,y=540,relwidth=1,height=180)

ml-Label(F7,text="Total Cosmetic Price",bg="sky
blue",fg="black", font=("times new
roman",14,"bold")).grid(row=0,column=0,padx=20,pady=1,sticky-W)

ml_txt=Entry(F7,width=18,textvariable=self.cosmetic_price,font="arial 10
bold",bd=7,relief-SUNKEN).grid(row=0.column=1.padx=10,pady=1)

m2=Label(F7,text="Total Grocery Price",bg="sky
blue",fg="black",font=("times new
roman",14,"bad")}\grid(row=Lcolumn=0,padx=20,pady-sticky-W)

m2_txt=Entry(F7,width=18,textvariable=self.grocery_price.font="arial10 bold",bd=7,relief=SUNKEN).grid(row=1,column=1.padx=10,pady=1)

m3=Label(F7,text="Total Cold-drink Price",bg="sky
blue".fg="black", font=("times new
roman",14,"bold")).grid(row=2.column=0,padx=20,pady=1,sticky=W)

m3_txt=Entry(F7,width=18,textvariable=self.cold_drink_price.font="arial10 bold",bd=7,relief=SUNKEN).grid(row=2,column=1,padx=10,pady=1)

m4-Label(F7,text="Total Biscuit Price",bg="sky
blue",fg="black",font=("times new
roman",14,"bold")).grid(row=3,column=0,padx=20,pady=1,sticky=W)
m4_txt=Entry(F7,width=18,textvariable=self.biscuit_price,font="arial 10 bold",bd=7,relief-SUNKEN).grid(row=3,column=1,padx=10,pady=1)

#for tax

tax1=Label(F7,text="Cosmetic Tax (28%)",bg="sky
blue",fg="black",font=("timesnew roman",14,"bold")).grid(row=0,column=2,padx=20,pady=1,sticky=W)
taxl_txt=Entry(F7,width=18,textvariable=self.cosmetic_tax,font="arial 10
bold", bd=7,relief=SUNKEN).grid(row=0,column=3,padx=10.pady=1)

tax2=Label(F7,text="Grocery Tax (5%)",bg="sky
blue",fg="black",font=("times new
roman",14,"bold").grid(row=1,column=2,padx=20,pady=1,sticky=W)
tax2_txt=Entry(F7,width=18,textvariable=self.grocery_tax,font="arial
10 bold",bd=7,relief=SUNKEN).grid(row=1.column=3,padx=10,pady=1)

tax3=Label(F7,text="Cold-drink Tax (40%)",bg="sky
blue",fg="black", font=("times new
roman",14,"bold")).grid(row=2.column=2,padx=20,pady=1,sticky=W)

tax3_txt=Entry(F7,width=18,textvariable=self.cold_drink_tax,font="arial 10 bold", bd=7,relief-SUNKEN).grid(row=2,column=3,padx=10,pady=1)

tax4-Label(F7,text="Biscuit Tax (5%)",bg="sky
blue",fg="black",font=("timesnew roman",14,"bold").grid(row=3,column=2,padx=20,pady=1,sticky=W)
tax4_txt=Entry(F7,width=18,textvariable=self.biscuit_tax.font="arial 10 bold", bd=7,relief SUNKEN).grid(row=3.column=3,padx=10,pady=1)

btn_frame=Frame(F7,bd=7,relief GROOVE)
btn_frame.place(x=810,y=10,width=700,height=115)

total_btn=Button(btn_frame.command=self.total.text="Total".bg="
bd-5,fg="black",pady=15,width=14,font="arial 12
bold").grid(row=0,column=0.padx=15,pady=15)

genbill_btn=Button(btn_frame,text="Generate
Bill",command=self.bill_area,bg="cyan",bd=5,fg="black",pady=15,width=14,f)
