class Cliente():

    def __init__(self, id_cliente, nombre, apellidos, correo, telefono, direccion):
        self.id_cliente = id_cliente;
        self.nombre = nombre;
        self.apellidos = apellidos;
        self.correo = correo;
        self.telefono = telefono;
        self.direccion = direccion;
    
    def __repr__(self):
        
        return f"{self.id_cliente}\t{self.nombre}\t{self.apellidos}\t{self.correo}\t{self.telefono}\t{self.direccion}";

    def formato_json(self):

        return {
            "ID_Cliente": self.id_cliente,
            "Nombre": self.nombre,
            "Apellidos": self.apellidos,
            "Correo": self.correo,
            "Telefono": self.telefono,
            "Direccion": self.direccion
        };

    direccion_csv = "";

    def formato_direccion_csv(self, direccion_csv):
        direccion_csv = "";
        for clave, valor  in self.direccion.items():
            direccion_csv += f"{clave}: {valor} ";
        return direccion_csv;

    def formato_csv(self):

        return f"{self.id_cliente},{self.nombre},{self.apellidos},{self.correo},{self.telefono},{self.formato_direccion_csv(self.direccion_csv)}";