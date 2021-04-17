import fdb

database = "localhost:/Users/Medow/PycharmProjects/tcc/base/TCC.fdb"


def conectafdb(database):
    fdb.connect(
        dsn=database,
        user='SYSDBA',
        password='masterkey'
    )
    return print("oi")
conectafdb(database)
# Create a Cursor object that operates in the context of Connection con:
cur = conectafdb(database).cursor()

# Execute the SELECT statement:
cur.execute("select * from languages order by year_released")

# Retrieve all rows as a sequence and print that sequence:
print cur.fetchall()