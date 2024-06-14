import sqlite3

conn = sqlite3.connect('maintenance.sqlite3') #Create db connection
c = conn.cursor() # Create Cursor

# Create db if not extists
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








""" 

insert_mtworkorder('tsid001','ลุงโอJ','แผนกรปภ.','ปืนใหญ่','ยิงไม่ออก','6795','0904342311')
insert_mtworkorder('tsid002','ลุงโอJ','แผนกรปภ.','ปืนใหญ่','ยิงไม่ออก','6795','0904342312')
update_mtworkorder('tsid002','tel','0903539922')
delete_mtworkorder('tsid002')

result = view_mtworkorder()
print(result[1][7]) """