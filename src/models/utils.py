from src.connection.con_db import mysql

class DeliveryModel():
    def listDelivery(self):
        cursor = mysql.get_db().cursor()
        cursor.execute("""SELECT id, names, last_names
                        FROM delivery""")
        data = cursor.fetchall()
        print('Deliverys: ',data)
        cursor.close()
        return data