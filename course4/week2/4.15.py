import sqlite3

conn=sqlite3.connect('emaildb.sqlite')
cur=conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('CREATE TABLE Counts(org TEXT, count INTEGER)')

fname=input("enter file name")
try:
    fh=open(fname)
except:
    print("file doesnot exists")
    exit()

for line in fh:
    if not line.startswith("From:"):
        continue
    words=line.split()
    email=words[1]
    (emailname, org) = email.split("@")
    cur.execute('SELECT count FROM Counts WHERE org= ?',(org,))
    row=cur.fetchone()
    if row is None:
        cur.execute('INSERT INTO Counts(org,count) VALUES (?,1)',(org,))
    else:
        cur.execute('UPDATE Counts SET count=count+1 WHERE org=?',(org,))
    conn.commit()

sql='SELECT org,count FROM Counts ORDER BY count DESC'
for row in cur.execute(sql):
    print(row[0],row[1])

cur.close()
