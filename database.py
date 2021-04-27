import psycopg2

con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "maul_motor2",
    user = "postgres",
    password = "Sidiqmaulana354")

cur = con.cursor()


print(" Program Demo Operasi CRUD PostgreSQL Database ")
print("       Sidiq Maulana Abdulloh (19/447128/SV/16847)            ")
print("================================================\n")
print("Menu Operasi Database")
print("1. Create database dan tabel")
print("2. Insert data")
print("3. Select/search data")
print("4. Update data")
print("5. Delete data")
menu=input("Silahkan pilih operasi ( 1/2/3/4/5 ) ? ")
print("Anda memilih : " + menu)

if menu=='1' :
    print("Create database dan tabel")
    # create a database named bengkel
    con = psycopg2.connect(
    host="localhost", 
    user = "postgres",
    database = "maul_motor2",
    port = 5432,
    password = "Sidiqmaulana354")
    cur = con.cursor()
    # create a table named user
    cur = con.cursor()
    cur.execute("CREATE TABLE insight (nama VARCHAR(60) NOT NULL, penilaian BOOLEAN NOT NULL)")
    con.commit()
elif menu=='2' :
    print("Insert data")
    #insert
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "maul_motor2",
    user = "postgres",
    password = "Sidiqmaulana354")
    cur = con.cursor()
    cur.execute('''INSERT INTO management_user (std_id, std_name, std_passwords, std_status) VALUES('8' 'David', 'david222', 'aktif');''')  
    con.commit()
elif menu=='3' :
    print("Select/search data")
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "maul_motor2",
    user = "postgres",
    password = "Sidiqmaulana354")
    cur = con.cursor()
    cur.execute("""SELECT * FROM sparepart""")
    query_res = cur.fetchall()
    print(query_res)

elif menu=='4' :
    print("Update data")
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "maul_motor2",
    user = "postgres",
    password = "Sidiqmaulana354")
    cur = con.cursor()
    sql1 = "UPDATE management_user SET passwords = 'etoo' WHERE std_id = 8"
    cur.execute(sql1)
    con.commit() 
    print(sql1)

elif menu=='5' :
    print("Delete data")
    con = psycopg2.connect(
    host="localhost", 
    port = 5432, 
    database = "maul_motor2",
    user = "postgres",
    password = "Sidiqmaulana354")
    cur = con.cursor()
    sql2 = "DELETE FROM usermanagement WHERE std_id = 4"
    cur.execute(sql2)
    con.commit()
    print(sql2)
cur.close()
con.close()