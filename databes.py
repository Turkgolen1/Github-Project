import mysql.connector
def insert_product(idproduct,name,price,image_url,description):

    connection=mysql.connector.connect(user="root",password="123456",host="localhost",database="node-app")
    cursor=connection.cursor()


    sql= "INSERT INTO PRODUCT(idproduct,name,price,image_url,description) VALUES(%s,%s,%s,%s,%s)"
    values = (idproduct,name,price,image_url,description)


    cursor.execute(sql,values)

    try:
        connection.commit()
    except mysql.connector.Error as err:
        print("hata:",err)
    finally:
        connection.close()
        print("Database bağlantısı kapandı")




name=input("id girin")
idproduct=input("id girin")
price=input("değer girin")
image_url=input("fotoğraf girin")
description=input("açıklama girin")
insert_product(idproduct,name,price,image_url,description)
