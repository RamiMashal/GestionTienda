import time
import uuid
import pandas as pd
from gestion_tienda import Tienda

mi_tienda = Tienda();

try:
    mi_tienda.cargar_json_productos();
    mi_tienda.cargar_json_clientes();
    mi_tienda.cargar_json_pedidos();
except:
    mi_tienda.log_app("""
    No se han cargado los json. Puede que sea hayan borrado los propios archivos o los diccionarios que contienen.
    Deberían crearse automáticamente al crear nuevos productos, clientes y pedidos.
    """);


while True:

    print("""
    \tGestión de Tienda

    [0] Crear nuevo producto * [5] Crear nuevo cliente * [a] Crear nuevo pedido           * [f] Nº de pedidos por cliente
    [1] Modificar producto   * [6] Modificar cliente   * [b] Modificar cantidad de pedido * [g] Mostrar pedidos ordenados por fecha
    [2] Consultar producto   * [7] Consultar cliente   * [c] Consultar pedido             * [h] Mostrar pedidos ordenados por ID_Cliente
    [3] Eliminar producto    * [8] Eliminar cliente    * [d] Eliminar pedido              * [i] Mostrar pedidos ordenados por cantidad
    [4] Mostrar productos    * [9] Mostrar clientes    * [e] Mostrar pedidos              * [j] Mostrar pedidos ordenados por precio total
    ------------------------------------------------------------------------------------- * [k] Ventas por mes

    [x] Cerrar app
    """);

    operacion = input("Elige operación: ");

    if operacion == "0": # CREAR NUEVO PRODUCTO

        tipo_producto = input("""\tElija el Tipo de Producto:
            [0] Bebida
            [1] Comida
            --> """);

        while mi_tienda.validar_tipo_producto(tipo_producto) == False:

            print("Solo puede elegir entre los tipos Bebida y Comida");
            tipo_producto = input("\tElija el Tipo de Producto:\n[0] Bebida\n[1] Comida\n--> ");
        
        tipo_producto = mi_tienda.formato_tipo_producto(tipo_producto);

        nombre_producto = input("Introduzca Nombre del Producto: ");
        marca_producto = input("Introduzca Marca del Producto: ");
        precio_producto = input("Introduzca Precio del Producto: ");

        while mi_tienda.validar_precio_producto(precio_producto) == True:
            print("""Entrada errónea. Introduzca un precio sin separador de miles.
            Si necesita decimales, use la coma.
            Ej: 9,5 / 9,99 / 1000 / 10000""");
            precio_producto = input("Introduzca Precio del Producto: ");

        precio_producto = mi_tienda.formato_precio_producto(precio_producto);

        stock_producto = input("Introduzca Stock del Producto: ");

        while stock_producto.isdigit() is not True:
            print("No se admiten decimales, ni caracteres extraños o espacios");
            stock_producto = input("Introduzca Stock del Producto: ");
        
        stock_producto = int(stock_producto);

        try:
            print(mi_tienda.crear_producto(
                tipo_producto, nombre_producto, marca_producto, precio_producto, stock_producto));

        except:
            print("Error inesperado al crear el producto");
            mi_tienda.log_app("Error inesperado al crear el producto");
        
        try:
            mi_tienda.log_app("Guardando lista productos en json");
            mi_tienda.guardar_json_productos();
        except:
            mi_tienda.log_app("Error inesperado al guardar lista productos en json");

    elif operacion == "1": # MODIFICAR PRODUCTO
        
        campo_modificar = input("\tQué elemento quieres modificar?\n[0] Tipo\n[1] Nombre\n[2] Marca\n[3] Precio\n[4] Stock\n");

        while mi_tienda.validar_campo_modificar(campo_modificar) == False:
            print("Ese campo no existe");
            campo_modificar = input("\tQué elemento quieres modificar?\n[0] Tipo\n[1] Nombre\n[2] Marca\n[3] Precio\n[4] Stock\n");
            
        if campo_modificar == "0": # MODIFICAR TIPO DE PRODUCTO

            nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            while mi_tienda.validar_buscar_producto(nombre_producto) == False:
                print("No encuentro ese producto");
                nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            nuevo_tipo = input("\tElija nuevo tipo de producto\n[0] Bebida\n[1] Comida\n");

            while mi_tienda.validar_tipo_producto(nuevo_tipo) == False:
                print("Solo puede elegir entre los tipos Bebida y Comida");
                nuevo_tipo = input("\tElija nuevo tipo de producto\n[0] Bebida\n[1] Comida\n");
            
            nuevo_tipo = mi_tienda.formato_tipo_producto(nuevo_tipo);

            try:
                print(mi_tienda.modificar_tipo_producto(nombre_producto, nuevo_tipo));
            except:
                print("Error inesperado al modificar Tipo de Producto");
                mi_tienda.log_app("Error inesperado modificar Tipo de Producto");
            
            try:
                mi_tienda.log_app("Guardando lista productos en json");
                mi_tienda.guardar_json_productos();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista productos en json");

        elif campo_modificar == "1": # MODIFICAR NOMBRE DE PRODUCTO

            nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            while mi_tienda.validar_buscar_producto(nombre_producto) == False:
                print("No encuentro ese producto");
                nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            nuevo_nombre = input("Introduzca nuevo nombre: ");

            try:
                print(mi_tienda.modificar_nombre_producto(nombre_producto, nuevo_nombre));
            except:
                print("Error inesperado al modificar Nombre de Producto");
                mi_tienda.log_app("Error inesperado modificar Nombre de Producto");
            
            try:
                mi_tienda.log_app("Guardando lista productos en json");
                mi_tienda.guardar_json_productos();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista productos en json");

        elif campo_modificar == "2": # MODIFICAR MARCA DE PRODUCTO

            nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            while mi_tienda.validar_buscar_producto(nombre_producto) == False:
                print("No encuentro ese producto");
                nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            nueva_marca = input("Introduzca nueva marca: ");

            try:
                print(mi_tienda.modificar_marca_producto(nombre_producto, nueva_marca));
            except:
                print("Error inesperado al modificar Marca de Producto");
                mi_tienda.log_app("Error inesperado modificar Marca de Producto");
            
            try:
                mi_tienda.log_app("Guardando lista productos en json");
                mi_tienda.guardar_json_productos();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista productos en json");

        elif campo_modificar == "3": # MODIFICAR PRECIO DE PRODUCTO

            nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            while mi_tienda.validar_buscar_producto(nombre_producto) == False:
                print("No encuentro ese producto");
                nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            nuevo_precio = input("Introduzca nuevo precio: ");

            while mi_tienda.validar_precio_producto(nuevo_precio) == True:
                print("""Entrada errónea. Introduzca un precio sin separador de miles.
                Si necesita decimales, use la coma.
                Ej: 9,5 / 9,99 / 1000 / 10000""");
                nuevo_precio = input("Introduzca nuevo precio: ");

            nuevo_precio = mi_tienda.formato_precio_producto(nuevo_precio);

            try:
                print(mi_tienda.modificar_precio_producto(nombre_producto, nuevo_precio));
            except:
                print("Error inesperado al modificar Precio de Producto");
                mi_tienda.log_app("Error inesperado Precio de Producto");
            
            try:
                mi_tienda.log_app("Guardando lista productos en json");
                mi_tienda.guardar_json_productos();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista productos en json");

        else: # MODIFICAR STOCK DE PRODUCTO

            nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            while mi_tienda.validar_buscar_producto(nombre_producto) == False:
                print("No encuentro ese producto");
                nombre_producto = input("Introduzca el nombre del producto que desea modificar: ");

            nuevo_stock = input("Introduzca nuevo stock: ");

            while nuevo_stock.isdigit() is not True:
                print("No se admiten decimales, ni caracteres extraños o espacios");
                nuevo_stock = input("Introduzca Stock del Producto: ");
            
            nuevo_stock = int(nuevo_stock);

            try:
                print(mi_tienda.modificar_stock_producto(nombre_producto, nuevo_stock));
            except:
                print("Error inesperado al modificar Stock de Producto");
                mi_tienda.log_app("Error inesperado Stock de Producto");
            
            try:
                mi_tienda.log_app("Guardando lista productos en json");
                mi_tienda.guardar_json_productos();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista productos en json");

    elif operacion == "2": # CONSULTAR PRODUCTO

        nombre_producto = input("Introduzca el nombre del producto que desea consultar: ");

        while mi_tienda.validar_buscar_producto(nombre_producto) == False:
            print("No encuentro ese producto");
            nombre_producto = input("Introduzca el nombre del producto que desea consultar: ");

        try:
            print(mi_tienda.consultar_producto(nombre_producto));
        except:
            print("Error inesperado al mostrar el producto");
            mi_tienda.log_app("Error inesperado al mostrar el producto");

    elif operacion == "3": # ELIMINAR PRODUCTO

        nombre_producto = input("Introduzca el nombre del producto que desea eliminar: ");

        while mi_tienda.validar_buscar_producto(nombre_producto) == False:
            print("No encuentro ese producto");
            nombre_producto = input("Introduzca el nombre del producto que desea eliminar: ");

        try:
            print(mi_tienda.eliminar_producto(nombre_producto));
        except:
            print("Error inesperado al eliminar el producto");
            mi_tienda.log_app("Error inesperado al eliminar el producto");
        
        try:
            mi_tienda.log_app("Guardando lista productos en json");
            mi_tienda.guardar_json_productos();
        except:
            mi_tienda.log_app("Error inesperado al guardar lista productos en json");

    elif operacion == "4": # MOSTRAR LISTA DE PRODUCTOS ORDENADOS POR ORDEN ALFABÉTICO
        mi_tienda.log_app("Mostrando Lista de Productos por orden alfabético");
        print("\nLista de Productos por orden alfabético\n");

        try:
            mi_tienda.crear_csv_productos();
            df_productos = pd.read_csv("csv_productos.csv", header=0);
            df_productos_nombre = df_productos.sort_values(by="Nombre", ascending=True);
            print(df_productos_nombre);

            mi_tienda.log_app("Lista de Productos por orden alfabético mostrada");
        except:
            mi_tienda.log_app("Error al mostrar Lista de Productos por orden alfabético");

    elif operacion == "5": # CREAR NUEVO CLIENTE
        
        id_cliente = str(uuid.uuid4());

        nombre_cliente = input("Introduzca el nombre del cliente que desea crear: ");
        apellidos_cliente = input("Introduzca los apellidos: ");
        correo_cliente = input("Introduzca el correo electrónico: ");

        while mi_tienda.validar_correo(correo_cliente) == False:
            print("Introduzca un correo válido");
            correo_cliente = input("Introduzca el correo electrónico: ");
        
        telefono_cliente = input("Introduzca el teléfono del cliente: ");

        while telefono_cliente.isdigit() is not True:
            print("Introduzca un teléfono válido");
            telefono_cliente = input("Introduzca el nombre del cliente que desea crear: ");

        print("Para la dirección del cliente...");
        calle = input("Introduzca calle, avenida, vía, etc: ");
        portal = input("Introduzca número/letra de portal: ");
        piso = input("Introduzca el piso: ");

        while piso.isdigit() is not True:
            print("Solo se admiten datos numéricos, sin decimales ni caracteres extraños o espacios");
            piso = input("Introduzca el piso: ");
        
        letra = input("Introduzca la letra: ");

        while letra.isalpha() is not True:
            print("Solo se admiten letras, sin caracteres extraños, espacios o números");
            letra = input("Introduzca la letra: ");

        codigo_postal = input("Introduzca el código postal: ");

        while codigo_postal.isdigit() is not True or len(codigo_postal) != 5:
            print("El CP son 5 números sin decimales ni caracteres extraños o espacios");
            codigo_postal = input("Introduzca el código postal: ");

        direccion = mi_tienda.direccion_cliente(calle, portal, piso, letra, codigo_postal);

        try:
            print(mi_tienda.crear_cliente(
                id_cliente, nombre_cliente, apellidos_cliente, correo_cliente, telefono_cliente, direccion
            ));
        except:
            print("Error inesperado al crear nuevo cliente");
            mi_tienda.log_app("Error inesperado al crear nuevo cliente");
        
        try:
            mi_tienda.log_app("Guardando lista clientes en json");
            mi_tienda.guardar_json_clientes();
        except:
            mi_tienda.log_app("Error inesperado al guardar lista clientes en json");

    elif operacion == "6": # MODIFICAR CLIENTE

        campo_modificar = input(
            "\tQué elemento quieres modificar?\n[0] Nombre\n[1] Apellidos\n[2] Correo\n[3] Teléfono\n[4] Dirección\n"
        );

        while mi_tienda.validar_campo_modificar(campo_modificar) == False:
            print("Ese campo no existe");
            campo_modificar = input(
            "\tQué elemento quieres modificar?\n[0] Nombre\n[1] Apellidos\n[2] Correo\n[3] Teléfono\n[4] Dirección\n"
        );

        if campo_modificar == "0": # MODIFICAR NOMBRE DE CLIENTE

            id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            while mi_tienda.validar_buscar_IDcliente(id_buscar) == False:
                print(f"No encuentro ID: {id_buscar}");
                id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            nuevo_nombre = input("Introduzca nuevo nombre: ");

            try:
                print(mi_tienda.modificar_nombre_cliente(id_buscar, nuevo_nombre));
            except:
                print("Error inesperado al modificar Nombre de Cliente");
                mi_tienda.log_app("Error inesperado modificar Nombre de Cliente");
            
            try:
                mi_tienda.log_app("Guardando lista clientes en json");
                mi_tienda.guardar_json_clientes();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista clientes en json");

        elif campo_modificar == "1": # MODIFICAR APELLIDOS DE CLIENTE

            id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            while mi_tienda.validar_buscar_IDcliente(id_buscar) == False:
                print(f"No encuentro ID: {id_buscar}");
                id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            nuevo_apellidos = input("Introduzca nuevos apellidos: ");

            try:
                print(mi_tienda.modificar_apellidos_cliente(id_buscar, nuevo_apellidos));
            except:
                print("Error inesperado al modificar Apellidos de Cliente");
                mi_tienda.log_app("Error inesperado modificar Apellidos de Cliente");
            
            try:
                mi_tienda.log_app("Guardando lista clientes en json");
                mi_tienda.guardar_json_clientes();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista clientes en json");
                

        elif campo_modificar == "2": # MODIFICAR CORREO DE CLIENTE

            id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            while mi_tienda.validar_buscar_IDcliente(id_buscar) == False:
                print(f"No encuentro ID: {id_buscar}");
                id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            nuevo_correo = input("Introduzca nuevo correo: ");

            while mi_tienda.validar_correo(nuevo_correo) == False:
                print("Introduzca un correo válido");
                nuevo_correo = input("Introduzca nuevo correo: ");
            
            try:
                print(mi_tienda.modificar_correo_cliente(id_buscar, nuevo_correo));
            except:
                print("Error inesperado al modificar Correo de Cliente");
                mi_tienda.log_app("Error inesperado modificar Correo de Cliente");
            
            try:
                mi_tienda.log_app("Guardando lista clientes en json");
                mi_tienda.guardar_json_clientes();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista clientes en json");

        elif campo_modificar == "3": # MODIFICAR TELÉFONO DE CLIENTE
            
            id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            while mi_tienda.validar_buscar_IDcliente(id_buscar) == False:
                print(f"No encuentro ID: {id_buscar}");
                id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            nuevo_telefono = input("Introduzca nuevo teléfono: ");

            while nuevo_telefono.isdigit() is not True:
                print("Introduzca un teléfono válido");
                nuevo_telefono = input("Introduzca nuevo teléfono: ");
            
            try:
                print(mi_tienda.modificar_telefono_cliente(id_buscar, nuevo_telefono));
            except:
                print("Error inesperado al modificar Teléfono de Cliente");
                mi_tienda.log_app("Error inesperado modificar Teléfono de Cliente");
            
            try:
                mi_tienda.log_app("Guardando lista clientes en json");
                mi_tienda.guardar_json_clientes();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista clientes en json");

        else: # MODIFICAR DIRECCIÓN DE CLIENTE

            id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            while mi_tienda.validar_buscar_IDcliente(id_buscar) == False:
                print(f"No encuentro ID: {id_buscar}");
                id_buscar = input("Introduzca ID de Cliente que desea modificar: ");

            print("Para la nueva dirección del cliente...");
            nueva_calle = input("Introduzca nueva calle, avenida, vía, etc: ");
            nuevo_portal = input("Introduzca nuevo número/letra de portal: ");
            nuevo_piso = input("Introduzca nuevo piso: ");

            while nuevo_piso.isdigit() is not True:
                print("Solo se admiten datos numéricos, sin decimales ni caracteres extraños o espacios");
                nuevo_piso = input("Introduzca nuevo piso: ");
            
            nueva_letra = input("Introduzca nueva letra: ");

            while nueva_letra.isalpha() is not True:
                print("Solo se admiten letras, sin caracteres extraños, espacios o números");
                nueva_letra = input("Introduzca nueva letra: ");

            nuevo_codigo_postal = input("Introduzca nuevo código postal: ");

            while nuevo_codigo_postal.isdigit() is not True or len(nuevo_codigo_postal) != 5:
                print("El CP son 5 números sin decimales ni caracteres extraños o espacios");
                nuevo_codigo_postal = input("Introduzca nuevo código postal: ");
            
            nueva_direccion = {
                nueva_calle, nuevo_portal, nuevo_piso, nueva_letra, nuevo_codigo_postal
            };

            try:
                print(mi_tienda.modificar_direccion_cliente(
                    id_buscar, nueva_calle, nuevo_portal, nuevo_piso, nueva_letra, nuevo_codigo_postal, nueva_direccion
                ));
            except:
                print("Error inesperado al modificar nueva dirección de cliente");
                mi_tienda.log_app("Error inesperado al modificar nueva dirección de cliente");
            
            try:
                mi_tienda.log_app("Guardando lista clientes en json");
                mi_tienda.guardar_json_clientes();
            except:
                mi_tienda.log_app("Error inesperado al guardar lista clientes en json");

    elif operacion == "7": # CONSULTAR CLIENTE

        id_buscar = input("Introduzca ID de Cliente que desea consultar: ");

        while mi_tienda.validar_buscar_IDcliente(id_buscar) == False:
            print(f"No encuentro ID: {id_buscar}");
            id_buscar = input("Introduzca ID de Cliente que desea consultar: ");
        
        try:
            print(mi_tienda.consultar_cliente(id_buscar));
        except:
            print("Error inesperado al consultar cliente");
            mi_tienda.log_app("Error inesperado al consultar cliente");

    elif operacion == "8": # ELIMINAR CLIENTE

        id_buscar = input("Introduzca ID de Cliente que desea eliminar: ");

        while mi_tienda.validar_buscar_IDcliente(id_buscar) == False:
            print(f"No encuentro ID: {id_buscar}");
            id_buscar = input("Introduzca ID de Cliente que desea eliminar: ");
        
        try:
            print(mi_tienda.eliminar_cliente(id_buscar));
        except:
            print("Error inesperado al eliminar cliente");
            mi_tienda.log_app("Error inesperado al eliminar cliente");
        
        try:
            mi_tienda.log_app("Guardando lista clientes en json");
            mi_tienda.guardar_json_clientes();
        except:
            mi_tienda.log_app("Error inesperado al guardar lista clientes en json");

    elif operacion == "9": # MOSTRAR LISTA DE CLIENTES POR ORDEN ALFABÉTICO
        mi_tienda.log_app("Mostrando Lista de Clientes por orden alfabético");
        print("\nLista de Clientes por orden alfabético\n");

        try:
            mi_tienda.crear_csv_clientes(); 
            df_clientes = pd.read_csv("csv_clientes.csv", header=0);
            df_clientes_nombre = df_clientes.sort_values(by="Nombre", ascending=True);
            print(df_clientes_nombre);

            mi_tienda.log_app("Lista de Clientes por orden alfabético mostrada");
        except:
            mi_tienda.log_app("Error al mostrar Lista de Clientes por orden alfabético");

    elif operacion.lower() == "a": # CREAR NUEVO PEDIDO

        id_pedido = str(uuid.uuid4());

        id_cliente_pedidos = input("Introduzca ID del cliente que realiza el pedido: ");

        while mi_tienda.validar_buscar_IDcliente(id_cliente_pedidos) == False:
            print(f"No encuentro ID: {id_cliente_pedidos}");
            id_cliente_pedidos = input("Introduzca ID del cliente que realiza el pedido: ");
        
        producto_pedido = input("Introduzca el nombre del producto para el pedido: ");

        while mi_tienda.validar_buscar_producto(producto_pedido) == False:
            print("No encuentro ese producto");
            producto_pedido = input("Introduzca el nombre del producto para el pedido: ");
        
        cantidad_producto = input("Introduzca la cantidad de producto para el pedido: ");

        while cantidad_producto.isdigit() is not True:
            print("Solo se admiten datos numéricos, sin decimales ni caracteres extraños o espacios");
            cantidad_producto = input("Introduzca la cantidad de producto para el pedido: ");
        
        cantidad_producto = float(cantidad_producto);

        precio_total = mi_tienda.calc_precio_total(producto_pedido, cantidad_producto);
        fecha_pedido = time.strftime('%d/%m/%Y %H:%M:%S');

        try:
            print(mi_tienda.crear_pedido(
                id_pedido, id_cliente_pedidos, producto_pedido, cantidad_producto, precio_total, fecha_pedido
            ));
        except:
            print("Error inesperado al crear pedido");
            mi_tienda.log_app("Error inesperado al crear pedido");
        
        try:
            mi_tienda.log_app("Guardando lista pedidos en json");
            mi_tienda.guardar_json_pedidos();
        except:
            mi_tienda.log_app("Error inesperado al guardar lista pedidos en json");

    elif operacion.lower() == "b": # MODIFICAR LA CANTIDAD DEL PEDIDO

        id_buscar = input("Introduzca ID de Pedido que desea modificar: ");

        while mi_tienda.validar_buscar_IDpedido(id_buscar) == False:
            print(f"No encuentro ID: {id_buscar}");
            id_buscar = input("Introduzca ID de Pedido que desea modificar: ");

        nueva_cantidad = input("Introduzca nueva cantidad de producto para este pedido: ");

        while nueva_cantidad.isdigit() is not True:
            print("Solo se admiten datos numéricos, sin decimales ni caracteres extraños o espacios");
            nueva_cantidad = input("Introduzca nueva cantidad de producto para este pedido: ");
        
        nueva_cantidad = float(nueva_cantidad);

        try:
            print(mi_tienda.modificar_pedido_cantidad(id_buscar, nueva_cantidad));
        except:
            print("Error inesperado al modificar la cantidad del pedido");
            mi_tienda.log_app("Error inesperado al modificar la cantidad del pedido");
        
        try:
            mi_tienda.log_app("Guardando lista pedidos en json");
            mi_tienda.guardar_json_pedidos();
        except:
            mi_tienda.log_app("Error inesperado al guardar lista pedidos en json");

    elif operacion.lower() == "c": # CONSULTAR PEDIDO

        id_buscar = input("Introduzca ID de Pedido que desea consultar: ");

        while mi_tienda.validar_buscar_IDpedido(id_buscar) == False:
            print(f"No encuentro ID: {id_buscar}");
            id_buscar = input("Introduzca ID de Pedido que desea consultar: ");
        
        try:
            print(mi_tienda.consultar_pedido(id_buscar));
        except:
            print("Error inesperado al consultar pedido");
            mi_tienda.log_app("Error inesperado al consultar pedido");

    elif operacion.lower() == "d": # ELIMINAR PEDIDO

        id_buscar = input("Introduzca ID de Pedido que desea eliminar: ");

        while mi_tienda.validar_buscar_IDpedido(id_buscar) == False:
            print(f"No encuentro ID: {id_buscar}");
            id_buscar = input("Introduzca ID de Pedido que desea eliminar: ");
        
        try:
            print(mi_tienda.eliminar_pedido(id_buscar));
        except:
            print("Error inesperado al eliminar pedido");
            mi_tienda.log_app("Error inesperado al eliminar pedido");
        
        try:
            mi_tienda.log_app("Guardando lista pedidos en json");
            mi_tienda.guardar_json_pedidos();
        except:
            mi_tienda.log_app("Error inesperado al guardar lista pedidos en json");
    
    elif operacion.lower() == "e": # MOSTRAR TODOS LOS PEDIDOS

        try:
            print(mi_tienda.mostrar_pedidos());
        except:
            print("Error inesperado al mostrar Lista de Pedidos");
            mi_tienda.log_app("Error inesperado al mostrar Lista de Pedidos");
        
    elif operacion.lower() == "f": # RANKING NÚMERO DE PEDIDOS POR CLIENTE
        mi_tienda.log_app("Mostrando Ranking Nº pedidos por cliente");

        try:
            mi_tienda.crear_csv_pedidos();
            df_pedidos = pd.read_csv("csv_pedidos.csv", header=0);
            ranking_pedidos = df_pedidos["ID_Cliente"].value_counts();
            print("\nID_Cliente ---------------------------- Nº Pedidos\n");
            print(ranking_pedidos);

            mi_tienda.log_app("Ranking Nº pedidos por cliente mostrado");
        except:
            mi_tienda.log_app("Error al mostrar Ranking Nº pedidos por cliente");
    
    elif operacion.lower() == "g": # RANKING PEDIDOS ORDENADOS POR FECHA (MÁS RECIENTE)
        mi_tienda.log_app("Mostrando Ranking pedidos por fecha");
        print("\nPedidos ordenados por fecha más reciente\n");

        try:
            mi_tienda.crear_csv_pedidos();
            df_pedidos = pd.read_csv("csv_pedidos.csv", header=0);
            df_fechas_pedidos = df_pedidos.sort_values(by="Fecha_pedido", ascending=False);
            print(df_fechas_pedidos);

            mi_tienda.log_app("Ranking pedidos por fecha mostrado");
        except:
            mi_tienda.log_app("Error al mostrar Ranking pedidos por fecha");
    
    elif operacion.lower() == "h": # PEDIDOS ORDENADOS POR ID_CLIENTE
        mi_tienda.log_app("Mostrando Ranking pedidos por cliente");
        print("\nPedidos ordenados por ID_Cliente\n");

        try:
            mi_tienda.crear_csv_pedidos();
            df_pedidos = pd.read_csv("csv_pedidos.csv", header=0);
            df_clientes_pedidos = df_pedidos.sort_values(by="ID_Cliente");
            print(df_clientes_pedidos);

            mi_tienda.log_app("Ranking pedidos por cliente mostrado");
        except:
            mi_tienda.log_app("Error al mostrar Ranking pedidos por cliente");
    
    elif operacion.lower() == "i": # PEDIDOS ORDENADOS POR CANTIDAD
        mi_tienda.log_app("Mostrando pedidos ordenados por cantidad");
        print("\nPedidos ordenados por cantidad\n");

        try:
            mi_tienda.crear_csv_pedidos();
            df_pedidos = pd.read_csv("csv_pedidos.csv", header=0);
            df_cantidad_pedidos = df_pedidos.sort_values(by="Cantidad", ascending=False);
            print(df_cantidad_pedidos);

            mi_tienda.log_app("Pedidos ordenados por cantidad mostrados");
        except:
            mi_tienda.log_app("Error al mostrar pedidos ordenados por cantidad");
    
    elif operacion.lower() == "j": # PEDIDOS ORDENADOS POR PRECIO TOTAL
        mi_tienda.log_app("Mostrando pedidos ordenados por Precio total");
        print("\nPedidos ordenados por Precio total\n")

        try:
            mi_tienda.crear_csv_pedidos();
            df_pedidos = pd.read_csv("csv_pedidos.csv", header=0);
            df_precio_pedidos = df_pedidos.sort_values(by="Precio_total", ascending=False);
            print(df_precio_pedidos);

            mi_tienda.log_app("Pedidos ordenados por Precio total mostrados");
        except:
            mi_tienda.log_app("Error al mostrar pedidos ordenados por Precio total");
        
    elif operacion.lower() == "k": # VENTAS POR MES
        mi_tienda.log_app("Mostrando Ranking Nº pedidos por mes");

        try:
            print("\nRanking Nº pedidos por mes:\n");
            print(mi_tienda.ventas_mes());

            mi_tienda.log_app("Ranking Nº pedidos por mes mostrado");
        except:
            mi_tienda.log_app("Error al mostrar Ranking Nº pedidos por mes");

    elif operacion.lower() == "x":
        exit(0);

    else:
        print("Esa operación no está disponible.");
        