class Pedido():

    def __init__(self, id_pedido, id_cliente_pedidos, producto, cantidad, precio_total, fecha_pedido):
        self.id_pedido = id_pedido;
        self.id_cliente_pedidos = id_cliente_pedidos;
        self.producto = producto;
        self.cantidad = cantidad;
        self.precio_total = precio_total;
        self.fecha_pedido = fecha_pedido;
    
    def __repr__(self):
        
        return f"{self.id_pedido}\t{self.id_cliente_pedidos}\t{self.producto}\t{self.cantidad}\t{self.precio_total}\t{self.fecha_pedido}";
    
    def formato_json(self):
        
        return {
            "ID_Pedido": self.id_pedido,
            "ID_Cliente": self.id_cliente_pedidos,
            "Producto": self.producto,
            "Cantidad": self.cantidad,
            "Precio_total": self.precio_total,
            "Fecha_pedido": self.fecha_pedido,
        };