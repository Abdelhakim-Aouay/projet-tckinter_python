from tkinter import *
from tkinter import ttk
import mysql.connector
import mysql
from tkinter import messagebox

frm=Tk()
frm.geometry('1500x800+1+1')
frm.title('first application')
frm.resizable(False,False)
frm.config(background='silver')
title=Label(frm,
text='détails des développeurs',
bg='#1AAECB',
font=('monospace',14),
fg='white'

)
title.pack(fill=X)

#------------------------------variables-----------------------------

id_var=StringVar()
name_var=StringVar()
email_var=StringVar()
address_var=StringVar()
phone_var=StringVar()
competence_var=StringVar()
experience_var=StringVar()
gendre_var=StringVar()
choisir_var=StringVar()
search_var=StringVar()

#----------------------------------------------------------------------------------functions






#------------------------------frame des etudients--------------------
details=Frame(frm, bg='white')
details.place(y=30, width=210, height=600)

lbl1=Label(details, text='id',bg='white')
lbl1.pack()
entry1=Entry(details, justify='center', bd=2, bg='white', textvariable=id_var)
entry1.pack()

lbl2=Label(details, text='name', bg='white')
lbl2.pack()
entry2=Entry(details, justify='center', bd=2, bg='white', textvariable=name_var )
entry2.pack()


lbl3=Label(details, text='email', bg='white')
lbl3.pack()
entry3=Entry(details, justify='center', bd=2, bg='white', textvariable=email_var)
entry3.pack()

lbl4=Label(details, text='address', bg='white')
lbl4.pack()
entry4=Entry(details, justify='center', bd=2, bg='white', textvariable=address_var)
entry4.pack()

phone=Label(details, text='phone', bg='white')
phone.pack()
entry5=Entry(details, justify='center', bd=2, bg='white', textvariable=phone_var)
entry5.pack()

lbl_competence=Label(details, text='compétences', bg='white')
lbl_competence.pack()
combo_gender= ttk.Combobox(details, textvariable=competence_var)
combo_gender['value']=('python', 'java', 'c++', 'c', 'Ruby', 'PHP')
combo_gender.pack()

lbl_experience=Label(details, text='expérience', bg='white')
lbl_experience.pack()
combo_gender= ttk.Combobox(details, textvariable=experience_var)
combo_gender['value']=('0', '1-3 ans', '3-5 ans', '5 ans +')
combo_gender.pack()

lbl_gendre=Label(details, text='gendre', bg='white')
lbl_gendre.pack()
combo_gender= ttk.Combobox(details, textvariable=gendre_var)
combo_gender['value']=('masculin', 'femnin')
combo_gender.pack()


#------------------frame horizontale------------------
chercher_frame=Frame(frm, bg='white')
chercher_frame.place(x=210, y=30, width=1435,height=50)

lbl_chercher=Label(chercher_frame, text='choisir',)
lbl_chercher.place(x=2, y=15)

dev= ttk.Combobox(chercher_frame, textvariable=search_var)
dev['value']=('id', 'name', 'email', 'phone')
dev.place(x=80, y=15)

ent=Entry(chercher_frame, justify='center', bd=2, bg='white', textvariable=choisir_var)
ent.place(x=250, y=15)

btn_search=Button(chercher_frame, text='chercher',  bg='#0D6FB8', bd=2, fg='white')
btn_search.place(x=400,y=12, width=130, height=25)



#-------------------------------resultas des developpeurs-------------------------------------------

details_frame=Frame(frm,bg='silver')
details_frame.place(x=210, y=80, width=1295,height=710)

scroll_x=Scrollbar(details_frame, orient= HORIZONTAL)
scroll_y=Scrollbar(details_frame, orient=VERTICAL)

developpeur_table=ttk.Treeview(details_frame,
columns=('id','name','email','address','phone','competence','expérience','gendre'),
xscrollcommand=scroll_x.set,
yscrollcommand=scroll_y.set)
developpeur_table.place(x=5,y=1,width=1335,height=690)
scroll_x.pack(side=BOTTOM, fill=X)
scroll_y.pack(side= LEFT, fill= Y)

#scroll_y.config(command=developpeur_table.xview)

developpeur_table['show']='headings'
developpeur_table.heading('id', text="id du développeur")
developpeur_table.heading('name', text="nom du développeur")
developpeur_table.heading('email', text="email du développeur")
developpeur_table.heading('address', text="adresse du développeur")
developpeur_table.heading('phone', text="phone du développeur")
developpeur_table.heading('competence', text="competence du développeur")
developpeur_table.heading('expérience', text="experience du développeur")
developpeur_table.heading('gendre', text="gendre")


developpeur_table.column('id', width=30)
developpeur_table.column('name',width=60)
developpeur_table.column('email', width=60)
developpeur_table.column('address', width=60)
developpeur_table.column('phone', width=60)
developpeur_table.column('competence', width=70)
developpeur_table.column('expérience', width=70)
developpeur_table.column('gendre', width=80)



#-----------------------------------------base de données---------------------------------------------


    #mycur.execute("CREATE DATABASE Projet_Developpeurs")
#mycur.execute("CREATE TABLE developpeurs (id int primary key, name VARCHAR(255), email VARCHAR(100), address VARCHAR(255), phone VARCHAR(20), competence VARCHAR(50), experience VARCHAR(50), gendre VARCHAR(30))")
def connection():
    
    try:
        conn = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = 'Projet_developpeurs',
        )
        return conn
    except:
        print('erreur')


conn=connection()
mycur=conn.cursor()
mycur.execute("select * from developpeurs")
rows=mycur.fetchall()
if len(rows) !=0:
    developpeur_table.delete(*developpeur_table.get_children())
    for row in rows:
        developpeur_table.insert("", END, values = row)
        
    conn.commit()

conn.close()

def ajout_developpeurs():
    conn=connection()
    mycur = conn.cursor()
    mycur.execute("INSERT INTO developpeurs values(%s, %s, %s, %s, %s, %s, %s, %s)", (
                                                                            id_var.get(), 
                                                                            name_var.get(), 
                                                                            email_var.get(), 
                                                                            address_var.get(), 
                                                                            phone_var.get(), 
                                                                            competence_var.get(), 
                                                                            experience_var.get(), 
                                                                            gendre_var.get()
                                                                            ))
    
    
    mycur.execute("select * from developpeurs")
    rows=mycur.fetchall()
    if len(rows) !=0:
        developpeur_table.delete(*developpeur_table.get_children())
        for row in rows:
            developpeur_table.insert("", END, values = row)
        conn.commit()
    
    clear()
    conn.close()


   

'''conn=connection()
mycur = conn.cursor()
mycur.execute("select * from developpeurs")
    #rows = mycur.fetchall()
   
for row in mycur:
    developpeur_table.insert("", END, values = row)'''
        

def delete():
    idSelector= developpeur_table.item(developpeur_table.selection())['values'][0]
    conn=connection()
    mycur = conn.cursor()
    mycur.execute("DELETE FROM developpeurs WHERE id ={}".format(idSelector))
    mycur.execute("select * from developpeurs")
    rows=mycur.fetchall()
    if len(rows) !=0:
        developpeur_table.delete(*developpeur_table.get_children())
        for row in rows:
            developpeur_table.insert("", END, values = row)
        conn.commit()
    developpeur_table.delete(developpeur_table.selection())
    clear()
    conn.close()

def clear():
    id_var.set('')
    name_var.set('')
    email_var.set('')
    address_var.set('')
    phone_var.set('')
    competence_var.set('')
    experience_var.set('')
    gendre_var.set('')
    #choisir_var.set('')
    


def get_cursor(ev):
    cursor_row=developpeur_table.focus()
    contents=developpeur_table.item(cursor_row)
    row=contents['values']
    id_var.set(row[0])
    name_var.set(row[1])
    email_var.set(row[2])
    address_var.set(row[3])
    phone_var.set(row[4])
    competence_var.set(row[5])
    experience_var.set(row[6])
    gendre_var.set(row[7])

developpeur_table.bind("<ButtonRelease-1>", get_cursor)   

def update():
    conn=connection()
    mycur=conn.cursor()
    sql="UPDATE developpeurs set name = %s, email = %s,  address = %s, compétences = %s, expérience=%s, where id= %s  "
    val = (name_var.get(), address_var.get(), phone_var.get(), competence_var.get(), experience_var.get(), gendre_var.get(), id_var.get())
    mycur.execute(sql,val)
    
    rows=mycur.fetchall()
    #if len(rows) !=0:
     #   developpeur_table.delete(*developpeur_table.get_children())
    for row in rows :
        developpeur_table.insert("", END, values = row)
        conn.commit()
    
    conn.close()
    
                                                                                                                                
   


def sortbyname():
    for x in developpeur_table.get_children():
        developpeur_table.delete(x)
    conn=connection()
    mycur = conn.cursor()
    mycur.execute("select*from developpeurs order by name asc")
    rows = mycur.fetchall()
    conn.commit()
    for row in rows:
        developpeur_table.insert("", END, values = row)
    conn.close()


def chercher():
    conn=connection()
    mycur = conn.cursor()
    

    mycur.execute("select * from developpeurs")
    rows=mycur.fetchall()
    

    for row in rows:
        print(row)
    conn.commit()
    conn.close()
#ent.bind("<Return>", chercher)'''



#------------------frame des boutons-------------
btn_frame=Frame(frm, bg='white')
btn_frame.place(y=500,width=210,height=353)
title=Label(btn_frame, text="Panneau de controle", font=('Deco',13),fg='white',bg='#1AAECB')
title.pack(fill=X)



add_btn=Button(btn_frame, text='ajouter développeur',  bg='silver', bd=2, command=ajout_developpeurs)
add_btn.place(x=33,y=75, width=150, height=30)

sup_btn=Button(btn_frame, text='suuprimer développeur',  bg='silver', bd=2, command=delete)
sup_btn.place(x=33,y=105, width=150, height=30)

sortir_btn=Button(btn_frame, text='supprimer tous',  bg='silver', bd=2)
sortir_btn.place(x=33,y=135, width=150, height=30)
    
vider_btn=Button(btn_frame, text='vider',  bg='silver', bd=2, command=clear)
vider_btn.place(x=33,y=165, width=150, height=30)

mise_ajour_btn=Button(btn_frame, text='mise a jour',  bg='silver', bd=2, command=update)
mise_ajour_btn.place(x=33,y=195, width=150, height=30)

sortByName_btn=Button(btn_frame, text='sortByName',  bg='silver', bd=2, command=sortbyname)
sortByName_btn.place(x=33,y=225, width=150, height=30)

quitter_btn=Button(btn_frame, text='quitter',  bg='silver', bd=2, command=frm.quit)
quitter_btn.place(x=33,y=255, width=150, height=30)



btn_search=Button(chercher_frame, text='chercher',  bg='#0D6FB8', bd=2, fg='white', command=chercher)
btn_search.place(x=400,y=12, width=130, height=25)
frm.mainloop()
