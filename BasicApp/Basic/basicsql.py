import sqlite3

#Create db connection
conn = sqlite3.connect('maintenance.sqlite3')

# Create Cursor
c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS mt_workorder (          
                    ID INTEGER PRIMARY KEY AUTOINCREMENT,
                    tsid TEXT,
                    name TEXT,
                    department TEXT,
                    machine TEXT,
                    problem TEXT,
                    number TEXT,
                    tel TEXT ) """)



def insert_mtworkorder(tsid,name,department,machine,problem,number,tel):
    #creat
    with conn:
        command = 'INSERT INTO mt_workorder VALUES (?,?,?,?,?,?,?,?)'
        c.execute(command,(None,tsid,name,department,machine,problem,number,tel))
    conn.commit()

insert_mtworkorder('tsid002','ลุงโอJ','แผนกรปภ.','ปืนใหญ่','ยิงไม่ออก','6795','0904342313')

def view_mtworkorder():
    #Read
    with conn:
        command = 'SELECT * FROM mt_workorder'
        c.execute(command)
        result = c.fetchall()
    return result

def update_mtworkorder(tsid,field,newvalue):
    #Update
    with conn:
        command = 'UPDATE mt_workorder SET {} = (?) WHERE tsid=(?)'.format(field)
        c.execute(command,(newvalue,tsid))
    conn.commit()

def delete_mtworkorder(tsid):
    #Delete
    with conn:
        command = 'DELETE FROM mt_workorder WHERE tsid=(?)'
        c.execute(command,([tsid]))
    conn.commit()






result = view_mtworkorder()
print(type(result[0]))

""" 
update_mtworkorder('tsid002','tel','0903539921')
delete_mtworkorder('tsid002')
result = view_mtworkorder()
print(result[1][7]) """