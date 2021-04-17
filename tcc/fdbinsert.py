import fdb

nome_idade = ["lucaslopes", 33]


con = fdb.connect(dsn='localhost:/Users/Medow/PycharmProjects/tcc/base/TCC.fdb', user='sysdba', password='masterkey')
cur = con.cursor()
cur.execute("insert into teste (nome,idade) values (?,?)", nome_idade)
con.commit()

cur.execute("select * from teste order by nome")
print(cur.fetchall())
