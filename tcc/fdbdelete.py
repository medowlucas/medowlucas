import fdb

nome = ['lucaslopes']

con = fdb.connect(dsn='localhost:/Users/Medow/PycharmProjects/tcc/base/TCC.fdb', user='sysdba', password='masterkey')
cur = con.cursor()
cur.execute("delete from teste where nome=?", nome)
con.commit()

cur.execute("select * from teste order by nome")
print(cur.fetchall())
