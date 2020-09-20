from requests import Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import pymysql
import json
import requests
import os

apikey = 'H4jPeoooR6osSlGm0pDs9m4gQ5H0M69jPrm1LQqHLBzrj9QusHOh1n1o5N6p9DzZ'

secret_key = 'H4jPeoooR6osSlGm0pDs9m4gQ5H0M69jPrm1LQqHLBzrj9QusHOh1n1o5N6p9DzZ'

url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'

parameters = {

    'start': '1',

    'limit': '5000',

    'convert': 'USD'

}

headers = {

    'Accepts': 'application/json',

    'X-CMC_PRO_API_KEY': 'b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c',

}

session = Session()

session.headers.update(headers)


class DataBase:

    def __init__(self):

        self.connection = pymysql.connect(
            
            host='localhost',
            
            user='root',
            
            password='123',
            
            db='python'

        )
        
        self.cursor = self.connection.cursor()

        print("conexion establecida correctamente")

    def SelectFecha(self, id):

        sql = 'SELECT id, fecha from historico where id = {}'.format(id)

        try:

            self.cursor.execute(sql)

            fecha = self.cursor.fetchone()

            print("Número: ", fecha[0])
            print("Fecha y hora: ", [1])
            print("_____\n")

        except Exception as identifier:

            raise

    def SelectBilletera(self):

        sql = "SELECT * FROM billetera"

        try:

            self.cursor.execute(sql)

            bille = self.cursor.fetchall()

            for user in bille:

                print("Billetera: ", bille[0])
                print("Bitcoins: ", bille[1])
                print("Bitcoin Cash: ", bille[2])
                print("Litecoin: ", bille[3])
                print("Ethernums: ", bille[4])
                print("Ethercoin: ", bille[5])
                print("Ledgers: ", bille[6])
                print("______\n")

        except Exception as e:
            raise

    def select_all_Fechas(self):

        sql = 'SELECT id, fecha from historico'

        try:

            self.cursor.execute(sql)

            fechas = self.cursor.fetchall()

            for user in fechas:

                print("Numero:", user[0])
                print("Fecha y hora:", user[1])
                print("____\n")

        except Exception as identifier:

            raise

    def update_fecha(self, id, fecha):

        sql = "UPDATE historico SET fecha='{}' WHERE id={}".format(fecha, id)

        try:
            self.cursor.execute(sql)
            self.connection.commit()

        except Exception as e:
            raise

    def insert_fecha(self):

        sql = "INSERT INTO historico values(NULL, NOW())"

        try:
            self.cursor.execute(sql)
            self.connection.commit()
        except Exception as e:
            raise

    def close(self):
        self.connection.close()


database = DataBase()
database.SelectBilletera()

try:

    response = session.get(url, params=parameters)

    data = json.loads(response.text)

    print(data)

except (ConnectionError, Timeout, TooManyRedirects) as e:

    print(e)


def menu():
    os.system("cls")
    print("Selecciona una opción:")
    print("")
    print("Opcion 1: Recibir un monto de alguna criptomonoda.")
    print("")
    print("Opcion 2: Enviar un monto de alguna criptomoneda.")
    print("")
    print("Opcion 3: Revisar el balance de alguna criptomoneda.")
    print("")
    print("Opcion 4: Revisar el balance general.")
    print("")
    print("Opcion 5: Mostrar el historial de transacciones.")
    print("")
    print("Opcion 6: Salir.")
    print("")

while True:

    menu()

    opcionMenu = input("Porfavor ingrese un valor >> ")

    if opcionMenu == "1":

        print("Has elegido recibir un monto de alguna criptomoneda.")

        import json

        nombre = input(

            "Inserte el nombre de su criptomoneda (Utilice la sigla correspondiente): " + "\n" + "BTC: bitcoin" + "\n" +
            "BCC: bitcoincash" + "\n" + "LTC: Litecoin" + "\n" + "ETH: Ether"
            + "\n" + "ETC: Ethercoin" + "\n" + "XRP: Ledger" + "\n")

        if nombre == "BTC" or nombre == "BCC" or nombre == "LTC" \
                or nombre == "ETH" or nombre == "ETC" or nombre == "XRP":

            nombremodificado = str(nombre + "USDT")

            res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=" + nombremodificado)

            json = res.json()

            print("Grandioso " + nombre + " se cotiza hoy en " + str(json["price"]) + " USD.")

        else:

            print("Usted digitó mal la sigla")

            break

        criptorecibe = input("Porfavor ingresa la cantidad de " + nombre + " que recibira ")

        if criptorecibe != "":

            coderecibe = input("Porfavor ahora indique el codigo númerico del remitente ")

            if coderecibe != "":

                print("Codigo verificado")

                if criptorecibe == "1":

                    print("Se acreditó un/a " + nombre)

                    database.insert_fecha()

                    break

                else:

                    print("Se acreditarón " + criptorecibe + ' ' + nombre)

                    database.insert_fecha()

                    break

            else:

                print("El codigo ingresado es invalido")

                break
        else:

            print("Porfavor ingrese un valor.")

            break

    elif opcionMenu == "2":

        print("Has elegido enviar un monto de alguna criptomoneda.")

        nombre = input(

            "Inserte el nombre de la criptomoneda que enviara (Utilice la sigla correspondiente): " + "\n"
            + "BTC: bitcoin" + "\n" + "BCC: bitcoincash" + "\n" + "LTC: Litecoin" + "\n" + "ETH: Ether" + "\n" +
            "ETC: Ethercoin" + "\n" + "XRP: Ledger" + "\n")

        if nombre == "BTC" or nombre == "BCC" or nombre == "LTC" \
                or nombre == "ETH" or nombre == "ETC" or nombre == "XRP":

            nombremodificado = str(nombre + "USDT")

            res = requests.get("https://api.binance.com/api/v3/ticker/price?symbol=" + nombremodificado)

            json = res.json()

            print("Grandioso " + nombre + " se cotiza hoy en " + str(json["price"]) + " USD.")

        else:

            print("Usted digitó mal la sigla")

            break
        criptoenvio = input("Porfavor ingresa la cantidad de " + nombre + " que enviara ")

        if criptoenvio >= "1":

            codigoReceptor = input("Porfavor ahora indique el codigo númerico del receptor ")

            if codigoReceptor >= "1":
                print("Codigo verificado")

                codigoEnvio = int(input("Ahora por favor digite su codigo para confirmar la transacción"))

                if criptoenvio >= "1":

                    print("Codigo validado")

                    if criptoenvio == "1":

                        print("Se envió un/ una " + nombre)

                        database.insert_fecha()

                        break

                    else:

                        print("Se enviaron " + criptoenvio + " " + nombre)

                        database.insert_fecha()

                        break

                else:

                    print("Codigo invalido")

                    break

            else:

                break

        else:

            break

    elif opcionMenu == "3":

        print("Has elegido revisar el balance de alguna criptomoneda.")

        print("")

        break

    elif opcionMenu == "4":

        print("")

        input("Has elegido revisar el balance general.")

        break

    elif opcionMenu == "5":

        print("Has elegido revisar tu historial de transacciones")

        print("Tus transacciones fueron:")

        database.select_all_Fechas()

        break

    elif opcionMenu == "6":

        print("")

        database.close()

        break

    else:

        print("Por favor elija una opción valida")
