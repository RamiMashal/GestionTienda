import time
import json
import pandas as pd

from producto import Producto
from cliente import Cliente
from pedido import Pedido

class Tienda():

    productos = [];
    clientes = [];
    pedidos = [];

    def log_app(self, mensaje):
        mensaje_control = f"{time.strftime('%d/%m/%Y %H:%M:%S')} - {mensaje}\n";

        fichero_log = open("fichero_log.txt", "a", encoding="utf-8");
        fichero_log.write(mensaje_control);
        fichero_log.close();

    # ----------------------------- FUNCIONES DE VALIDACIÓN / FORMATO -----------------------------

    def formato_texto(self, texto):

        texto = texto.lower();

        formato_tilde = {"á":"a", "é":"e", "í":"i", "ó":"o", "ú":"u"};
        for tilde, nuevo_caracter in formato_tilde.items():
            texto = texto.replace(tilde, nuevo_caracter);

        return texto;

    def validar_tipo_producto(self, tipo_producto):

        if tipo_producto == "0":
            return True;

        elif tipo_producto == "1":
            return True;
        
        else:
            return False;

    def formato_tipo_producto(self, tipo_producto):

        if tipo_producto == "0":
            tipo_producto = "Bebida";
        else:
            tipo_producto = "Comida";
        return tipo_producto;
    
    def validar_precio_producto(self, precio_producto):

        for caracter in "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ;%~$&¬ªº:/?¡¿!()[]}{¨ç´`^'·#*-+_. |<>=@":
            if caracter in precio_producto:
                return True;
            elif precio_producto == "":
                return True;
            elif precio_producto == ",":
                return True;
            else:
                return False;

    def formato_precio_producto(self, precio_producto):

        formato_decimal = {",":"."};
        for coma, punto in formato_decimal.items():
            precio_producto = precio_producto.replace(coma, punto);

        precio_producto = float(precio_producto);
        return precio_producto;

    def validar_buscar_producto(self, nombre):

        nombre = self.formato_texto(nombre);

        for producto in self.productos:

            if self.formato_texto(producto.nombre) == nombre:
                return True;
        
        return False;

    def validar_campo_modificar(self, campo):
        if campo == "0":
            return True;
        elif campo == "1":
            return True;
        elif campo == "2":
            return True;
        elif campo == "3":
            return True;
        elif campo == "4":
            return True;
        else:
            return False;
    
    def validar_correo(self, correo_cliente):

        if "@" not in correo_cliente or "." not in correo_cliente or correo_cliente[0] == "@" or correo_cliente[-1] == "@" or correo_cliente[0] == "." or correo_cliente[-1] == "." or correo_cliente.count("@") > 1 == True:
            return False;
        
        for caracter in ",;%~$&¬ªº:/?¡¿!()[]}{¨ç´`^'·#* |<>=áéíóúÁÉÍÓÚ":
            if caracter in correo_cliente:
                return False;
        else:
            return True;
    
    def validar_buscar_IDcliente(self, id_buscar):

        for cliente in self.clientes:
            if cliente.id_cliente == id_buscar:
                return True;
        return False;
    
    def validar_buscar_IDpedido(self, id_buscar):
        
        for pedido in self.pedidos:
            if pedido.id_pedido == id_buscar:
                return True;
        return False;

    # ----------------------------- FUNCIONES CREAR, MODIFICAR, CONSULTAR Y ELIMINAR -----------------------------

    def crear_producto(self, tipo, nombre, marca, precio, stock): # FUNCIONES PRODUCTO
        self.log_app(f"Creando producto: {nombre}...");

        nuevo_producto = Producto(tipo, nombre, marca, precio, stock);
        self.productos.append(nuevo_producto);

        self.log_app(f"Producto creado:\n{nuevo_producto}");
        return f"Producto creado:\n{nuevo_producto}";
    
    def modificar_tipo_producto(self, nombre_producto, nuevo_tipo): # MODIFICAR TIPO PRODUCTO
        self.log_app(f"Modificando Tipo de Producto de: {nombre_producto}...");

        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.tipo = nuevo_tipo;
            
                self.log_app(f"Tipo de Producto de - {nombre_producto} - modificado a {nuevo_tipo}");
                return f"Tipo de Producto de - {nombre_producto} - modificado a {nuevo_tipo}";

        self.log_app("Error inesperado modificar Tipo de Producto. Puede que no haya productos en la lista");
        return False;
    
    def modificar_nombre_producto(self, nombre_producto, nuevo_nombre): # MODIFICAR NOMBRE PRODUCTO
        self.log_app(f"Modificando Nombre de Producto de: {nombre_producto}...");

        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.nombre = nuevo_nombre;
            
                self.log_app(f"Nombre de Producto de - {nombre_producto} - modificado a {nuevo_nombre}");
                return f"Nombre de Producto de - {nombre_producto} - modificado a {nuevo_nombre}";

        self.log_app("Error inesperado modificar Nombre de Producto. Puede que no haya productos en la lista");
        return False;
    
    def modificar_marca_producto(self, nombre_producto, nueva_marca): # MODIFICAR MARCA PRODUCTO
        self.log_app(f"Modificando Marca de Producto de: {nombre_producto}...");

        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.marca = nueva_marca;
            
                self.log_app(f"Marca de Producto de - {nombre_producto} - modificada a {nueva_marca}");
                return f"Marca de Producto de - {nombre_producto} - modificada a {nueva_marca}";

        self.log_app("Error inesperado modificar Marca de Producto. Puede que no haya productos en la lista");
        return False;
    
    def modificar_precio_producto(self, nombre_producto, nuevo_precio): # MODIFICAR PRECIO PRODUCTO
        self.log_app(f"Modificando Precio de Producto de: {nombre_producto}...");

        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.precio = nuevo_precio;
            
                self.log_app(f"Precio de Producto de - {nombre_producto} - modificado a {nuevo_precio}");
                return f"Precio de Producto de - {nombre_producto} - modificado a {nuevo_precio}";

        self.log_app("Error inesperado modificar Precio de Producto. Puede que no haya productos en la lista");
        return False;

    def modificar_stock_producto(self, nombre_producto, nuevo_stock): # MODIFICAR STOCK PRODUCTO
        self.log_app(f"Modificando Stock de Producto de: {nombre_producto}...");

        for producto in self.productos:
            if producto.nombre == nombre_producto:
                producto.stock = nuevo_stock;
            
                self.log_app(f"Stock de Producto de - {nombre_producto} - modificado a {nuevo_stock}");
                return f"Stock de Producto de - {nombre_producto} - modificado a {nuevo_stock}";

        self.log_app("Error inesperado modificar Stock de Producto. Puede que no haya productos en la lista");
        return False;
    
    def consultar_producto(self, nombre_producto): # CONSULTAR PRODUCTO
        self.log_app(f"Consultar producto: {nombre_producto}...");

        consulta_producto = "Tipo\tNombre\tMarca\tPrecio\tStock\n\n";

        for producto in self.productos:
            if producto.nombre == nombre_producto:
                consulta_producto += str(producto) + "\n\n";

        self.log_app("Consulta de producto realizada");
        return consulta_producto;
    
    def eliminar_producto(self, nombre_producto): # ELIMINAR PRODUCTO
        self.log_app(f"Eliminando producto {nombre_producto}...");

        for producto in self.productos:
            if producto.nombre == nombre_producto:
                self.productos.remove(producto);
        
                self.log_app(f"Producto - {nombre_producto} - eliminado");
                return f"Producto - {nombre_producto} - eliminado";

    def mostrar_productos(self): # MOSTRAR LISTA DE PRODUCTOS
        self.log_app(f"Mostrando todos los productos...");

        contador = 0;
        lista_productos = "Tipo\tNombre\tMarca\tPrecio\tStock\n\n";

        for producto in self.productos:
            lista_productos += str(producto) + "\n\n";
            contador += 1;

        self.log_app("Lista de productos mostrada");
        return f"{lista_productos}\nHay {contador} productos";
    
    # FUNCIONES CLIENTE

    def direccion_cliente(self, calle, portal, piso, letra, codigo_postal):

        direccion_cliente = {
            "Calle": calle,
            "Portal": portal,
            "Piso": piso,
            "Letra": letra,
            "Codigo Postal": codigo_postal,
        };
        return direccion_cliente; 
    
    # CREAR CLIENTE
    def crear_cliente(self, id_cliente, nombre_cliente, apellidos_cliente, correo_cliente, telefono_cliente, direccion):

        self.log_app(f"Creando cliente: {nombre_cliente}...");

        nuevo_cliente = Cliente(
            id_cliente, nombre_cliente, apellidos_cliente, correo_cliente, telefono_cliente, direccion
        );

        self.clientes.append(nuevo_cliente);

        self.log_app(f"Cliente creado:\n{nuevo_cliente}");
        return f"Cliente creado:\n{nuevo_cliente}";

    def modificar_nombre_cliente(self, id_buscar, nuevo_nombre): # MODIFICAR NOMBRE CLIENTE
        self.log_app(f"Modificando Nombre de Cliente de: {id_buscar}...");

        for cliente in self.clientes:
            if cliente.id_cliente == id_buscar:
                cliente.nombre = nuevo_nombre;
            
                self.log_app(f"Nombre de Cliente de - {id_buscar} - modificado a {nuevo_nombre}");
                return f"Nombre de Cliente de - {id_buscar} - modificado a {nuevo_nombre}";

        self.log_app("Error inesperado modificar Nombre de Cliente. Puede que no haya clientes en la lista");
        return False;

    def modificar_apellidos_cliente(self, id_buscar, nuevo_apellidos): # MODIFICAR APELLIDOS CLIENTE
        self.log_app(f"Modificando Apellidos de Cliente de: {id_buscar}...");

        for cliente in self.clientes:
            if cliente.id_cliente == id_buscar:
                cliente.apellidos = nuevo_apellidos;
            
                self.log_app(f"Apellidos de Cliente de - {id_buscar} - modificados a {nuevo_apellidos}");
                return f"Apellidos de Cliente de - {id_buscar} - modificados a {nuevo_apellidos}";

        self.log_app("Error inesperado modificar Apellidos de Cliente. Puede que no haya clientes en la lista");
        return False;
    
    def modificar_correo_cliente(self, id_buscar, nuevo_correo): # MODIFICAR CORREO CLIENTE
        self.log_app(f"Modificando Correo de Cliente de: {id_buscar}...");

        for cliente in self.clientes:
            if cliente.id_cliente == id_buscar:
                cliente.correo = nuevo_correo;
            
                self.log_app(f"Correo de Cliente de - {id_buscar} - modificado a {nuevo_correo}");
                return f"Correo de Cliente de - {id_buscar} - modificado a {nuevo_correo}";

        self.log_app("Error inesperado modificar Apellidos de Cliente. Puede que no haya clientes en la lista");
        return False;
    
    def modificar_telefono_cliente(self, id_buscar, nuevo_telefono): # MODIFICAR TELÉFONO CLIENTE
        self.log_app(f"Modificando Teléfono de Cliente de: {id_buscar}...");

        for cliente in self.clientes:
            if cliente.id_cliente == id_buscar:
                cliente.telefono = nuevo_telefono;
            
                self.log_app(f"Teléfono de Cliente de - {id_buscar} - modificado a {nuevo_telefono}");
                return f"Teléfono de Cliente de - {id_buscar} - modificado a {nuevo_telefono}";

        self.log_app("Error inesperado modificar Apellidos de Cliente. Puede que no haya clientes en la lista");
        return False;
    
    # MODIFICAR DIRECCIÓN CLIENTE
    def modificar_direccion_cliente(self, id_buscar, nueva_calle, nuevo_portal, nuevo_piso, nueva_letra, nuevo_codigo_postal, nueva_direccion):
        self.log_app(f"Modificando Dirección de Cliente de: {id_buscar}...");

        for cliente in self.clientes:
            if cliente.id_cliente == id_buscar:
                cliente.direccion["Calle"] = nueva_calle;
                cliente.direccion["Portal"] = nuevo_portal;
                cliente.direccion["Piso"] = nuevo_piso;
                cliente.direccion["Letra"] = nueva_letra;
                cliente.direccion["Codigo Postal"] = nuevo_codigo_postal;
            
                self.log_app(f"Dirección de Cliente de - {id_buscar} - modificada a {nueva_direccion}");
                return f"Dirección de Cliente de - {id_buscar} - modificada a {nueva_direccion}";
        
        self.log_app("Error inesperado modificar Dirección de Cliente. Puede que no haya clientes en la lista");
        return False;
    
    def consultar_cliente(self, id_buscar): # CONSULTAR CLIENTE
        self.log_app(f"Consultando Cliente: {id_buscar}...");

        info_cliente = "ID\tNombre\tApellidos\tCorreo\tTelefono\tDirección\n\n";

        for cliente in self.clientes:
            if cliente.id_cliente == id_buscar:
                info_cliente += str(cliente) + "\n\n";

        self.log_app("Consulta de cliente realizada");
        return info_cliente;
    
    def eliminar_cliente(self, id_buscar): # ELIMINAR CLIENTE
        self.log_app(f"Eliminando cliente {id_buscar}...");

        for cliente in self.clientes:
            if cliente.id_cliente == id_buscar:
                self.clientes.remove(cliente);
        
                self.log_app(f"Cliente - {id_buscar} - eliminado");
                return f"Cliente - {id_buscar} - eliminado";
    
    def mostrar_clientes(self): # MOSTRAR LISTA DE CLIENTES
        self.log_app(f"Mostrando Lista de Clientes...");

        contador = 0;
        lista_clientes = "ID\tNombre\tApellidos\tCorreo\tTelefono\tDirección\n\n";

        for cliente in self.clientes:
            lista_clientes += str(cliente) + "\n\n";
            contador += 1;

        self.log_app("Lista de clientes mostrada");
        return f"{lista_clientes}\nHay {contador} clientes";
    
    def calc_precio_total(self, producto_pedido, cantidad_producto): # CALCULAR PRECIO TOTAL PEDIDO
        self.log_app(f"Calculando precio total pedido...");

        precio_unidad = 0.0;
        precio_total = 0.0;

        for producto in self.productos:
            if producto.nombre == producto_pedido:
                precio_unidad += producto.precio;
                precio_total += precio_unidad * cantidad_producto;

        self.log_app(f"Precio total obtenido");
        return precio_total;

    def crear_pedido(self, id_pedido, id_cliente_pedidos, producto, cantidad, precio_total, fecha_pedido): # CREAR PEDIDO
        self.log_app(f"Creando pedido de producto - {producto} - para cliente - {id_cliente_pedidos} -...");

        nuevo_pedido = Pedido(
            id_pedido, id_cliente_pedidos, producto, cantidad, precio_total, fecha_pedido
        );

        self.pedidos.append(nuevo_pedido);

        self.log_app(f"Pedido creado:\n{nuevo_pedido}");
        return f"Pedido creado:\n{nuevo_pedido}";

    def modificar_pedido_cantidad(self, id_buscar, nueva_cantidad): # MODIFICAR CANTIDAD DEL PEDIDO
        self.log_app(f"Modificando Cantidad del Pedido: {id_buscar}..."); 

        for pedido in self.pedidos:
            if pedido.id_pedido == id_buscar:
                pedido.cantidad = nueva_cantidad;
                producto_pedido = pedido.producto;
                nuevo_precio_total = self.calc_precio_total(producto_pedido, nueva_cantidad)
                pedido.precio_total = nuevo_precio_total;
            
                self.log_app(f"Cantidad de Pedido - {id_buscar} - {producto_pedido} - modificada a - {nueva_cantidad} - Precio total modificado a - {nuevo_precio_total} -");
                return f"Cantidad de Pedido - {id_buscar} - {producto_pedido} - modificada a - {nueva_cantidad} - Precio total modificado a - {nuevo_precio_total} -";

        self.log_app("Error inesperado modificar Cantidad de Pedido. Puede que no haya pedidos en la lista");
        return False;
    
    def consultar_pedido(self, id_buscar):  # CONSULTAR PEDIDO
        self.log_app(f"Consultando Pedido: {id_buscar}...");

        info_pedido = "ID_Pedido\tID_Cliente\tProducto\tCantidad\tPrecio Total\tFecha\n\n";

        for pedido in self.pedidos:
            if pedido.id_pedido == id_buscar:
                info_pedido += str(pedido) + "\n";
                for cliente in self.clientes:
                    if pedido.id_cliente_pedidos == cliente.id_cliente:
                        info_pedido += f"-- > Pedido para el cliente: - {cliente.id_cliente} - {cliente.nombre} {cliente.apellidos} -\n\n"

        self.log_app("Consulta de pedido realizada");
        return info_pedido;
    
    def eliminar_pedido(self, id_buscar): # ELIMINAR PEDIDO
        self.log_app(f"Eliminando pedido {id_buscar}...");

        for pedido in self.pedidos:
            if pedido.id_pedido == id_buscar:
                self.pedidos.remove(pedido);
        
                self.log_app(f"Pedido - {id_buscar} - eliminado");
                return f"Pedido - {id_buscar} - eliminado";
        
    def mostrar_pedidos(self): # MOSTRAR LISTA DE PEDIDOS
        self.log_app(f"Mostrando Lista de Pedidos...");

        contador = 0;
        lista_pedidos = "ID_Pedido\tID_Cliente\tProducto\tCantidad\tPrecio Total\tFecha\n\n";

        for pedido in self.pedidos:
            lista_pedidos += str(pedido) + "\n";
            for cliente in self.clientes:
                if pedido.id_cliente_pedidos == cliente.id_cliente:
                    lista_pedidos += f"-- > Pedido para el cliente: - {cliente.id_cliente} - {cliente.nombre} {cliente.apellidos} -\n\n"
            contador += 1;

        self.log_app("Lista de pedidos mostrada");
        return f"{lista_pedidos}\nHay {contador} pedidos";

    # ----------------------------- FUNCIONES JSON -----------------------------

    def guardar_json_productos(self):
        self.log_app("Guardando listas de productos en json");

        with open("lista_productos.json", "w") as lista_productos:

            datos_productos = {"productos": []};
            for producto in self.productos:
                datos_productos["productos"].append(producto.formato_json());
            
            json.dump(datos_productos, lista_productos);
        
        self.log_app("Lista de productos guardada en json");
    
    def guardar_json_clientes(self):
        self.log_app("Guardando listas de clientes en json");

        with open("lista_clientes.json", "w") as lista_clientes:
            
            datos_clientes = {"clientes": []};
            for cliente in self.clientes:
                datos_clientes["clientes"].append(cliente.formato_json());
            
            json.dump(datos_clientes, lista_clientes);
        
        self.log_app("Lista de clientes guardada en json");

    def guardar_json_pedidos(self):
        self.log_app("Guardando lista de pedidos en json");

        with open("lista_pedidos.json", "w") as lista_pedidos:
            
            datos_pedidos = {"pedidos": []};
            for pedido in self.pedidos:
                datos_pedidos["pedidos"].append(pedido.formato_json());
            
            json.dump(datos_pedidos, lista_pedidos);

        self.log_app("Lista de pedidos guardada en json");

    def cargar_json_productos(self):
        self.log_app("Cargando 'lista_productos.json' en lista de productos");

        with open("lista_productos.json", "r") as lista_productos:

            cargar_lista_productos = json.load(lista_productos);

            for producto in cargar_lista_productos["productos"]:

                self.crear_producto(
                    producto["Tipo de Producto"], producto["Nombre"], producto["Marca"], producto["Precio/Unidad"], producto["Stock"]
                );
        
        self.log_app("'lista_productos.json' cargada en lista de productos");
    
    def cargar_json_clientes(self):
        self.log_app("Cargando 'lista_clientes.json' en lista de clientes");

        with open("lista_clientes.json", "r") as lista_clientes:

            cargar_lista_clientes = json.load(lista_clientes);
            
            for cliente in cargar_lista_clientes["clientes"]:

                self.crear_cliente(
                    cliente["ID_Cliente"], cliente["Nombre"], cliente["Apellidos"], cliente["Correo"], cliente["Telefono"], cliente["Direccion"]
                );
        
        self.log_app("'lista_clientes.json' cargada en lista de clientes");
    
    def cargar_json_pedidos(self):
        self.log_app("Cargando 'lista_pedidos.json' en lista de pedidos");

        with open("lista_pedidos.json", "r") as lista_pedidos:

            cargar_lista_pedidos = json.load(lista_pedidos);
            
            for pedido in cargar_lista_pedidos["pedidos"]:

                self.crear_pedido(
                    pedido["ID_Pedido"], pedido["ID_Cliente"], pedido["Producto"], pedido["Cantidad"], pedido["Precio_total"], pedido["Fecha_pedido"]
                );

        self.log_app("'lista_pedidos.json' cargada en lista de pedidos");
    
    # ----------------------------- FUNCIONES ANALÍTICA -----------------------------

    def crear_csv_pedidos(self):
        self.log_app("Guardando csv pedidos");

        with open("csv_pedidos.csv", "w") as csv_pedidos:

            columnas = "ID_Pedido,ID_Cliente,Producto,Cantidad,Precio_total,Fecha_pedido";
            csv_pedidos.write(columnas + "\n");
            for pedido in self.pedidos:
                fila = pedido.formato_csv() + "\n";
                csv_pedidos.write(fila);
        
        self.log_app("Csv guardado");

