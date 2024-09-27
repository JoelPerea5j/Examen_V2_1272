print("Creado por Joel Alberto Perea Castorena")
print("Mat: 22308051281272")
print(" ")

print("Diccionario de Productos")
Productos={
    "Id_producto : ": 4321,
    "Nombre del Producto : ":"Pall Mall ",
    "Precio : ":75,
    "Marca: ":"Tokio: ",
    "Stock: ":160,
    "Tipo de Producto: ":"Cigarros",
    "Fecha de Creacion":"12/03/2022"
    }
print(Productos)
for pro , pros in Productos.items():
    print(pro, pros)

print("")

print("Diccionario de Sucursales")
Sucursales={
    "Id_Sucursal : ": 896342,
    "Ubicacion : ":"Ciudad Juarez, Chihuahua, Mexico",
    "telefono : ":"656 532 8322 (Numero inventado)",
    "Nombre: ":"Tabaco Imperial ",
    "Horarios: ":"De 9:00am a 10:00pm todos los dias",
    "Gerente: ":"Horacio Hernandez",
    "Administracion":"Vetas a Proveedores"
}
print(Sucursales)
for Sucu , Saco in Sucursales.items():
    print(Sucu , Saco)
print("")

print("Diccionario de Ventas")
Ventas={
    "Id_Ventas : ": 134245,
    "Producto Vendido: ":"Cigarros Tokio",
    "Genancias : ":"7253$",
    "Id_Cliente: ":2314,
    "Metodo de Pago: ":"Por tarjeta",
    "Fecha de Compra: ":"08/04/2023",
    "Total de Venta":"23456$"
}
print(Ventas)
for Ven , Tas in Ventas.items():
    print(Ven , Tas)
print("")

print("Diccionario de Empleados")
Empleados={
    "Id_Empleado : ": 94783,
    "Nombre : ":"Aldo ",
    "Apellido : ":"Saucedo de Luna",
    "Salario: ": "5214$",
    "Edad: ":22,
    "Curp: ":"ALDSAU45624TGR3T4FG",
    "RFC":"PEAC071206XXX"
}
print(Empleados)
for Emple , Ados in Empleados.items():
    print(Emple , Ados)
print("")