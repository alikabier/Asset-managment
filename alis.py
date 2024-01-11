import tkinter as tk
from tkinter import ttk
import requests

win=tk.Tk()
win.geometry("1350x700+0+0")
win.title("Asset Managemnt System")
title_label=tk.Label(win,text="Asset Managment Systen",font=("Arial",30, "bold"), border=12, relief=tk.GROOVE,bg= "lightgrey").pack(side=tk.TOP,fill=tk.X)
detail_frame=tk.LabelFrame(win,text="Enter Details",font=("Arial",20),relief=tk.GROOVE,bg="lightgrey",bd=12).place(x=20,y=90,width=420,height=575)
data_frame=tk.Frame(win,bd=12,bg="lightgrey",relief=tk.GROOVE).place(x=475,y=90,width=810,height=575)

rollno_lbl=tk.Label(detail_frame,text="Serial no",font=('Arial',15),background="lightgrey")
rollno_lbl.place(x=40,y=125,width=85,height=75)
#rollno_lbl.grid(row=0,column=0,padx=2,pady=2)

rollno_ent=tk.Entry(detail_frame,bd=7,font=("arial",15)).place(x=151,y=135,width=240,height=45)
#rollno_ent.grid(row=0,column=1,padx=2,pady=2)

deprt_lbl=tk.Label(detail_frame,text="Department",font=('Arial',15),background="lightgrey")
deprt_lbl.place(x=40,y=185,width=105,height=75)
depart_ent=tk.Entry(detail_frame,bd=7,font=("arial",15)).place(x=151,y=195,width=240,height=45)

asset_lbl=tk.Label(detail_frame,text="Asset",font=('Arial',15),background="lightgrey").place(x=40,y=250,width=60,height=55)
asset_ent=tk.Entry(detail_frame,bd=7,font=("arial",15)).place(x=151,y=250,width=240,height=45)

quan_lbl=tk.Label(detail_frame,text="Quantity",font=('Arial',15),background="lightgrey").place(x=40,y=300,width=80,height=75)
quan_ent=tk.Entry(detail_frame,bd=7,font=("arial",15)).place(x=151,y=310,width=240,height=45)

cost_lbl=tk.Label(detail_frame,text="Cost",font=('Arial',15),background="lightgrey").place(x=40,y=370,width=55,height=55)
cost_ent=tk.Entry(detail_frame,bd=7,font=("arial",15)).place(x=151,y=370,width=240,height=45)

supplier_lbl=tk.Label(detail_frame,text=" Supplier",font=('Arial',15),background="lightgrey").place(x=40,y=430,width=75,height=55)
supplier_ent=tk.Entry(detail_frame,bd=7,font=("arial",15)).place(x=151,y=430,width=240,height=45)

campus_lbl=tk.Label(detail_frame,text="Campus",font=('Arial',15),background="lightgrey").place(x=40,y=490,width=75,height=55)
campus_ent=ttk.Combobox(detail_frame,font=("arial,18"),state="readonly")
campus_ent['values']=("Abbasia","Baghdad","Railway Road")
campus_ent.place(x=151,y=505,width=120,height=25)

date_lbl=tk.Label(detail_frame,text="Date",font=('Arial',15),background="lightgrey").place(x=40,y=540,width=75,height=55)
date_ent=tk.Entry(detail_frame,bd=7,font=("arial",15)).place(x=151,y=540,width=240,height=45)

btn_frame=tk.Frame(detail_frame,background="lightgrey" ,bd=10,relief=tk.GROOVE).place(x=40,y=588,width=385,height=55)

add_btn=tk.Button(btn_frame,bg="lightgrey",bd=7,text="add",font=("arial",13))
add_btn.place(x=61,y=595,width=65,height=35)

update_btn=tk.Button(btn_frame,bg="lightgrey",bd=7,text="Update",font=("arial",13))
update_btn.place(x=235,y=595,width=65,height=35)

delete_btn=tk.Button(btn_frame,bg="lightgrey",bd=7,text="Del",font=("arial",13))
delete_btn.place(x=150,y=595,width=65,height=35)

clear_btn=tk.Button(btn_frame,bg="lightgrey",bd=7,text="Clr",font=("arial",13))
clear_btn.place(x=325,y=595,width=65,height=35) 

search_frame=tk.Frame(data_frame,bg="lightgrey",bd=10,relief=tk.GROOVE,width=35)
search_frame.place(x=490,y=100,width=780,height=70 )

search_lbl=tk.Label(search_frame,text="Search",bg="lightgrey",font=("Arial",14))
search_lbl.grid(row=0,column=0,padx=12,pady=2)

search_in=ttk.Combobox(search_frame,font=("arial",14),state="readonly")
search_in['values']=("Serial","Department","Date","Asset","Quantity","Cost")
search_in.grid(row=0,column=1,padx=12,pady=2)

search_btn=tk.Button(search_frame,text="Search",font=("Arial",13),bd=9,width=14,bg="lightgrey")
search_btn.grid(row=0,column=2,padx=12,pady=2)

showall_btn=tk.Button(search_frame,text="Show All",font=("arial",13),bd=9,width=14,bg="lightgrey")
showall_btn.grid(row=0,column=3,padx=12,pady=2)

def add_asset():
    data = {
        "serial": rollno_ent.get(),
        "department": depart_ent.get(),
        "asset": asset_ent.get(),
        "quantity": quan_ent.get(),
        "cost": cost_ent.get(),
        "supplier": supplier_ent.get(),
        "campus": campus_ent.get(),
        "date": date_ent.get()
    }
    response = requests.post("http://127.0.0.1:5000/api/assets", json=data)
    print(response.json())

# Function to update an asset
def update_asset():
    serial = rollno_ent.get()
    data = {
        "department": depart_ent.get(),
        "asset": asset_ent.get(),
        "quantity": quan_ent.get(),
        "cost": cost_ent.get(),
        "supplier": supplier_ent.get(),
        "campus": campus_ent.get(),
        "date": date_ent.get()
    }
    response = requests.put(f"http://127.0.0.1:5000/api/assets/{serial}", json=data)
    print(response.json())

# Function to delete an asset
def delete_asset():
    serial = rollno_ent.get()
    response = requests.delete(f"http://127.0.0.1:5000/api/assets/{serial}")
    print(response.json())

# ... (Other functions, if needed)

# Assign the functions to the buttons
add_btn = tk.Button(btn_frame, bg="lightgrey", bd=7, text="Add", font=("arial", 13), command=add_asset)
add_btn.place(x=61, y=595, width=65, height=35)

update_btn = tk.Button(btn_frame, bg="lightgrey", bd=7, text="Update", font=("arial", 13), command=update_asset)
update_btn.place(x=235, y=595, width=65, height=35)

delete_btn = tk.Button(btn_frame, bg="lightgrey", bd=7, text="Del", font=("arial", 13), command=delete_asset)
delete_btn.place(x=150, y=595, width=65, height=35)



win.mainloop()