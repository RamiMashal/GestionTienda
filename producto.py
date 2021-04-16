class Producto():

    def __init__(self, tipo, nombre, marca, precio, stock):
        self.tipo = tipo;
        self.nombre = nombre;
        self.marca = marca;
        self.precio = precio;
        self.stock = stock;
    
    def __repr__(self):
        
        return f"{self.tipo}\t{self.nombre}\t{self.marca}\t{self.precio}\t{self.stock}";

    def formato_json(self):
        
        return {
            "Tipo de Producto": self.tipo,
            "Nombre": self.nombre,
            "Marca": self.marca,
            "Precio/Unidad": self.precio,
            "Stock": self.stock
        };