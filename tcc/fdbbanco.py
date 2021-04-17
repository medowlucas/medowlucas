import fdb

con = fdb.connect(dsn='tcc', user='sysdba', password='masterkey')
cur = con.cursor()
cur.execute("select * from teste order by nome")
print(cur.fetchall())
