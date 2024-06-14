from tkinter import *
from tkinter import messagebox
from datetime import datetime
from db_Maintenance import *
from tkinter import ttk





###GUI SET UP #########################################################
GUI = Tk()

GUI.title('โปรแกรมซ่อมบำรุง by OHM')
GUI.geometry('1000x600+50+50')
####FONT#####
FONT1 = ('THSarabunNew Bold',22,'bold')
FONT2 = ('THSarabunNew',18)
########TAB Set Up########
Tab = ttk.Notebook(GUI)
T1 = Frame(Tab)
T2 = Frame(Tab)
T3 = Frame(Tab)
Tab.add(T1,text='ใบแจ้งซ่อม')
Tab.add(T2,text='ดูใบแจ้งซ่อม')
Tab.add(T3,text='สรุป')
Tab.pack(fill=BOTH,expand=1)


####TAB1##########################################################################
L = Label(T1,text='ใบแจ้งซ่อม',font=FONT1)
L.place(x=100,y=10)

#-------------
L = Label(T1,text='ชื่อผู้แจ้ง',font=FONT2)
L.place(x=30,y=50)
v_name = StringVar() #ตัวแปรพิเศษใช้กับ GUI
E1 = ttk.Entry(T1,textvariable=v_name, font=FONT2)
E1.place(x=150,y=50)

#-------------
L = Label(T1,text='แผนก',font=FONT2)
L.place(x=30,y=100)
v_department =StringVar()
E2 = ttk.Entry(T1,textvariable=v_department,font=FONT2)
E2.place(x=150,y=100)
#-------------
L = Label(T1,text='อุปกรณ์/เครื่อง',font=FONT2)
L.place(x=30,y=150)
v_machine =StringVar()
E3 = ttk.Entry(T1,textvariable=v_machine,font=FONT2)
E3.place(x=150,y=150)
#-------------
L = Label(T1,text='อาการเสีย',font=FONT2)
L.place(x=30,y=200)
v_problem =StringVar()
E4 = ttk.Entry(T1,textvariable=v_problem ,font=FONT2)
E4.place(x=150,y=200)
#-------------
L = Label(T1,text='หมายเลข',font=FONT2)
L.place(x=30,y=250)
v_number =StringVar()
E5 = ttk.Entry(T1,textvariable=v_number,font=FONT2)
E5.place(x=150,y=250)
#-------------
L = Label(T1,text='เบอร์โทร',font=FONT2)
L.place(x=30,y=300)
v_tel =StringVar()
E6 = ttk.Entry(T1,textvariable=v_tel,font=FONT2)
E6.place(x=150,y=300)


####TAB2##########################################################################

header = ['TSID','ชื่อ','แผนก','อุปกรณ์','อาการเสีย','หมายเลข','เบอร์โทรผู้แจ้ง']    #ชื่อหัวตาราง
headerw = [100,150,100,100,250,100,100]

mtworkorderlist = ttk.Treeview(T2,columns=header,show='headings',height=20) #ให้อยู่ในแทป2
mtworkorderlist.pack()

style = ttk.Style()
style.configure('Treeview.Heading',font=('THSarabunNew',20))
style.configure('Treeview',rowheight=25,font=('THSarabunNew',15))

for h,w in zip(header,headerw):
    mtworkorderlist.heading(h,text=h)
    mtworkorderlist.column(h,width=w,anchor='center')
#mtworkorderlist.insert('','end',values=headerw)

mtworkorderlist.column('TSID',anchor='w')

def update_table():

    #เคลียร์ข้อมูลเก่าในตารางออกก่อน
    mtworkorderlist.delete(*mtworkorderlist.get_children())
    data = view_mtworkorder()
    #print(data)
    for d in data :
        d = list(d) #แปลง tuple เป็น list
        del d[0]    #ลบคอลัมภ์แรก ที่เป็นตัวเลขรันไปเรื่อย
        mtworkorderlist.insert('','end',values=d)

####TAB3##########################################################################





####FUNCTION
def genTsid():
    dt = str(int(datetime.now().strftime('%y%m%d%H%M%S'))+240332210200)
    print(dt)
    return(dt)

def save():
    name = v_name.get() # .get คือการดึงออกมาจาก StringVar
    department = v_department.get()
    machine = v_machine.get()
    problem = v_problem.get()
    number = v_number.get()
    tel = v_tel.get()

    text = 'ชื่อผู้แจ้ง: ' + name + '\n' # \n คือขึ้นบรรทัดใหม่
    text = text + 'แผนก: ' + department + '\n'
    text = text + 'อุปกรณ์/เครื่อง: ' + machine + '\n'
    text = text + 'อาการเสีย: ' + problem + '\n'
    text = text + 'หมายเลข: ' + number + '\n'
    text = text + 'โทร: ' + tel + '\n'

    tsid = genTsid()
    insert_mtworkorder(tsid,name,department,machine,problem,number,tel)
    update_table()





    #dt = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #record = [tsid,name,department,machine,problem,number,tel]
    messagebox.showinfo('กำลังบันทึกข้อมูล...',text)


















####BUTTON

B = Button(T1, text='บันทึกใบแจ้งซ่อม',command=save)
B.place(x=200,y=350)




##########Init First when start up ###########

update_table()
GUI.mainloop()