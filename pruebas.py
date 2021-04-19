import uuid

numero = "1000"

print(numero.isdigit())

id_numero = id(numero)

print(id_numero)

id_cliente = uuid.uuid4()

print(id_cliente)

print(id_cliente)

direccion_cliente = {
            "Calle": 1,
            "Portal": 2,
            "Piso": 3,
            "Letra": 4,
            "Codigo Postal": 5,
        };

direccion_cliente["Calle"] = 10

print(direccion_cliente)

import time

fecha = time.strftime('%d/%m/%Y %H:%M:%S')

print(fecha)
