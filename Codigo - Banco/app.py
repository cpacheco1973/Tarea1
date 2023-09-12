from os import system
import time
import conexion as conn
import os

db = conn.DB()
dicc_cliente = {}
dicc_cuenta = {}
dicc_movimiento = {}
dicc_movcte = {}
lista_movmax = [0]
carga_bd = "N"
NumMov = 0

#Solicita los datos del cliente y los carga en la dicc_cliente
def insertCliente():
    limpiarPantalla()
    while True:
        while True:
            limpiarPantalla()
            print("******************************************************************************")
            print("\tLA ALCANCÍA BANK")
            print("******************************************************************************")
            print("\tInsertando Clientes")
            print("******************************************************************************")

            Cedula = int(input("Ingrese la Cedula [Digite 0 para Salir]: "))

            if Cedula == 0:
                break
            
            if (Cedula>0):
                if Cedula in dicc_cliente:
                    print("Cliente ya existe. Intente de nuevo")
                    time.sleep(3)
                else:
                    break;
            else:
                print("Debe digitar un número de cédula. Intente de nuevo")
                time.sleep(3)   

        if Cedula == 0:
            break
        
        Nombre = str(input("Ingrese el Nombre: ")).upper()
        Apellido1 = str(input("Ingrese el Apellido 1: ")).upper()
        Apellido2 = str(input("Ingrese el Apellido 2: ")).upper()

        if (Cedula>0 and len(Nombre)>0):
            if Cedula in dicc_cliente:
                print("Cliente ya existe. Intente de nuevo")
                time.sleep(3)
            else:
                dicc_cliente[Cedula]={'Nombre':Nombre,'Apellido1': Apellido1,'Apellido2': Apellido2}
        
        print("Registro ingresado con éxito")
        continuar = str(input("Desea Insetar otro Cliente [S/N]: ")).upper()
        limpiarPantalla()
        if (continuar == 'N'):
            break
        
    print("Registro ingresado con éxito")

#Imprime los datos del cliente.
def readCliente():
    limpiarPantalla()
    print("******************************************************************************")
    print("\tLA ALCANCÍA BANK")
    print("******************************************************************************")
    print("\tListado de Clientes")
    print("******************************************************************************")
    print("Cedula          Nombre               Apellido 1           Apellido 2          ")
    print("******************************************************************************")

    for Cedula, sub_cliente in dicc_cliente.items():
        Nombre=""
        Apellido1=""
        Apellido2=""
        for datos, valor in sub_cliente.items():
            if (datos == "Nombre"):
                Nombre = valor
            elif (datos == "Apellido1"):
                Apellido1 = valor
            elif (datos == "Apellido2"):
                Apellido2 = valor
                
        print(f"{Cedula:{15}}",f"{Nombre:{20}}",f"{Apellido1:{20}}",f"{Apellido2:{20}}")

    print("*************************** ULTIMA LINEA **************************************")
    print("Espere un momento...")
    time.sleep(5)
    system("clear")

#Inserta los datos de la cuenta
def insertCuenta():
    limpiarPantalla()
    Nombre = ""
    Apellido1 = ""
    Apellido2 = ""

    #Solicita los datos del cliente al que se le agregará la cuenta.
    while True:
        print("******************************************************************************")
        print("\tLA ALCANCÍA BANK")
        print("******************************************************************************")
        print("\tInsertando Cuenta de un Cliente")
        print("******************************************************************************")
        Cedula = int(input("Ingrese la Cedula [Digite 0 para Salir]: "))

        if Cedula == 0:
            break

        #Valida si el cliente ya tiene cuenta asignada.
        if Cedula in dicc_cuenta:
            print("Cliente ya tiene cuenta asignada. Intente de nuevo")
            time.sleep(3)
        else:
            #Valida si el cliente existe en la lista de clientes
            if Cedula in dicc_cliente:
                contador = 0
                Nombre=""
                Apellido1=""
                Apellido2=""

                Nombre = dicc_cliente[Cedula]['Nombre']
                Apellido1 = dicc_cliente[Cedula]['Apellido1']
                Apellido2 = dicc_cliente[Cedula]['Apellido2']

                break
            else:
                print("Cliente no existe. Intente de nuevo")
                time.sleep(3)
         
    #Muestra el cliente consultado y solicita la cuenta.        
    limpiarPantalla()
    print("******************************************************************************")
    print("\tLA ALCANCÍA BANK")
    print("******************************************************************************")
    print("\tInsertando Cuenta de un Cliente")
    print("******************************************************************************")  
    print("    ",Cedula," - ",Nombre," ",Apellido1," ",Apellido2)
    print("******************************************************************************")
    
    NumeroCuenta = int(input("Ingrese el Numero de Cuenta: "))
    Estado = str(input("Ingrese el Estado de la Cuenta [ACTIVO / INACTIVO]: ")).upper()
    MontoDisponible = 0

    if (NumeroCuenta>0 and len(Estado)>0):
        if Cedula not in dicc_cuenta:
            dicc_cuenta[Cedula]={'NumeroCuenta':NumeroCuenta,'MontoDisponible':MontoDisponible,'Estado':Estado}
        
    print("Registro ingresado con éxito")

# Muestra el reporte de los datos de la cuenta          
def readCuenta():
    limpiarPantalla()
    print("******************************************************************************")
    print("\tLA ALCANCÍA BANK")
    print("******************************************************************************")
    print("\tListado de Cuentas")
    print("******************************************************************************")
    print("Cedula            Numero Cuenta      Monto Disponible    Estado          ")
    print("******************************************************************************")


    for Cedula, sub_cuenta in dicc_cuenta.items():
        NumeroCuenta=0
        NumCuentaRep=""
        MontoDisponible=0
        MontoDispRep=""
        Estado=""
        for datos, valor in sub_cuenta.items():
            if (datos == 'NumeroCuenta'):
                NumeroCuenta = valor
            elif (datos == 'MontoDisponible'):
                MontoDisponible = valor
            elif (datos == 'Estado'):
                Estado = valor

        print(f"{Cedula:{15}}",f"{NumeroCuenta:{15}}","    ",f"{MontoDisponible:.2f}","               ",Estado)

    print("*************************** ULTIMA LINEA **************************************")
    print("Espere un momento...")
    time.sleep(3)
    system("clear")

def insertMovs():
    limpiarPantalla()
    Nombre = ""
    Apellido1 = ""
    Apellido2 = ""
    NumeroCuenta = 0
    MontoDisponible = 0
    Estado = ""
    sumaResta = 1
    valido = "S"

    #Solicita los datos del cliente al que se le agregará la cuenta.
    while True:
        limpiarPantalla()
        print("******************************************************************************")
        print("\tLA ALCANCÍA BANK")
        print("******************************************************************************")
        print("\tInsertando Movimientos de una Cuenta de un Cliente")
        print("******************************************************************************")
        Cedula = int(input("Ingrese la Cedula [Digite 0 para Salir]: "))

        if Cedula == 0:
            break
        
        
        #Valida si el cliente ya tiene cuenta asignada.
        if Cedula in dicc_cliente:
            Nombre = dicc_cliente[Cedula]['Nombre']
            Apellido1 = dicc_cliente[Cedula]['Apellido1']
            Apellido2 = dicc_cliente[Cedula]['Apellido2']
            valido = "S"
        else:
            valido = "N"
            print("Cliente no existe. Intente de nuevo.")
            time.sleep(3)
            
        
        if Cedula in dicc_cuenta:
            NumeroCuenta = dicc_cuenta[Cedula]['NumeroCuenta']
            MontoDisponible = dicc_cuenta[Cedula]['MontoDisponible']
            Estado = dicc_cuenta[Cedula]['Estado']
            valido = "S"
            
            if Estado == 'INACTIVO':
                valido = "N"
                print("Cuenta Inactiva. Intente de nuevo")
                time.sleep(3)
                
        else:
            valido = "N"
            print("Cliente no tiene cuenta asignada. Intente de nuevo")
            time.sleep(3)

        if valido == "S":
            #Muestra el cliente y ccuenta consultado y solicita el movimiento.
            while True:
                while True:
                    Tipo = ""
                    Fecha = ""
                    Monto = 0.0
                    limpiarPantalla()
                    print("******************************************************************************")
                    print("\tLA ALCANCÍA BANK")
                    print("******************************************************************************")
                    print("\tInsertando Movimientos de una Cuenta de un Cliente")
                    print("******************************************************************************")   
                    print("    ",Cedula," - ",Nombre," ",Apellido1," ",Apellido2)
                    print("    ","Cuenta - ",NumeroCuenta)
                    print("******************************************************************************")
                    
                    Tipo = str(input("Ingrese Tipo de Movimiento [DEB / CRE]: ")).upper()
                    Fecha = str(input("Ingrese la Fecha del Movimiento: "))
                    Monto = float(input("Ingrese el Monto del: "))

                    if (Monto>0):
                        sumaResta = 1
                        if (Tipo == "DEB" and Monto>MontoDisponible):
                            print("No hay monto disponible para hacer este DEBITO. Intente de nuevo.")
                            time.sleep(3)
                        else:
                            if (Tipo == "CRE"):
                                sumaResta = 1
                            else:
                                sumaResta = -1
                            break;
                    else:
                        print("El monto es menor que 0. Intente de nuevo.")
                        
                NumeroMovimiento = lista_movmax[0]
                NumeroMovimiento += 1    
                dicc_movimiento[NumeroMovimiento]={'Cedula':Cedula,'Tipo':Tipo,'Fecha':Fecha,'Monto':Monto,'NumeroCuenta':NumeroCuenta}
                
                #Actualiza el disponible de la cuenta.
                Monto = Monto * sumaResta
                MontoDisponible = MontoDisponible + Monto
                dicc_cuenta[Cedula]['MontoDisponible'] = MontoDisponible
                
                lista_movmax[0] = NumeroMovimiento

                continuar = str(input("Desea Insetar otro Movimiento [S/N]: ")).upper()
                limpiarPantalla()
                if (continuar == 'N'):
                    break
                
            print("Registro ingresado con éxito")        

# Muestra el reporte de los datos de los movimientos          
def readMovsCliente():
    limpiarPantalla()
    print("******************************************************************************")
    print("\tLA ALCANCÍA BANK")
    print("******************************************************************************")
    print("\tListado de Movmimientos por Cliente")
    print("******************************************************************************")

    while True:
        NumeroMovimiento=0
        NumeroCuenta=0
        NumCuentaRep=""
        MontoDisponible=0
        MontoDispRep=""
        Estado=""
        Tipo=""
        Fecha=""
        Monto=""
        
        Cedula = int(input("Ingrese la Cedula [Digite 0 para Salir]: "))

        if Cedula not in dicc_cliente:
            print("Cliente No Existe. Intente de nuevo")
            time.sleep(3)
        else:
            if Cedula not in dicc_cuenta:
                print("Cliente no tiene cuenta asignada. Intente de nuevo")
                time.sleep(3)
            else:
                dicc_movcte = {clave: subdiccionario for clave, subdiccionario in dicc_movimiento.items() if subdiccionario['Cedula'] == Cedula}

                if Cedula == 0:
                    break

                limpiarPantalla()
                print("******************************************************************************")
                print("\tLA ALCANCÍA BANK")
                print("******************************************************************************")
                print("\tListado de Movmimientos por Cliente")
                print("******************************************************************************")
                print("Cliente: ",Cedula," - ",dicc_cliente[Cedula]['Nombre']," ",dicc_cliente[Cedula]['Apellido1']," ",dicc_cliente[Cedula]['Apellido2'])
                print("Estado de la Cuenta: ",dicc_cuenta[Cedula]['Estado'])
                print("******************************************************************************")
                print("Cuenta               Mov    Tipo   Fecha         Monto          ")
                print("******************************************************************************")
                
                for NumeroMovimiento, sub_mov in dicc_movcte.items():

                    for datos, valor in sub_mov.items():
                        if (datos == 'Cedula'):
                            Cedula = valor
                        elif (datos == 'Tipo'):
                            Tipo = valor
                        elif (datos == 'Fecha'):
                            Fecha = valor
                        elif (datos == 'Monto'):
                            Monto = valor
                        elif (datos == 'NumeroCuenta'):
                            NumeroCuenta = valor
                        
                        
                    print(f"{NumeroCuenta:{15}}"," ",f"{NumeroMovimiento:{5}}","    ",Tipo," ",Fecha," ",f"{Monto:.2f}")

                break
        
    print("*************************** ULTIMA LINEA **************************************")
    print("Espere un momento...")
    time.sleep(5)
    system("clear")
    

#Lee los datos de la base de datos  los carga en las listas.
def readDatabase():

    indice = 0
    
    print("Cargando Listas desde Base de Datos")
    print("Cargando Lista Clientes desde Base de Datos")
    
    #Lee los datos de la tabla clientes y los carga en la dicc_cliente 
    sql = "SELECT Cedula,Nombre,Apellido1,Apellido2 FROM Cliente order by Cedula"
    result = db.ejecutar_consulta(sql)
    for data in result:
        Cedula = data[0]
        Nombre = data[1]
        Apellido1 = data[2]
        Apellido2 = data[3]

        if Cedula not in dicc_cliente:
            dicc_cliente[Cedula]={'Nombre':Nombre,'Apellido1': Apellido1,'Apellido2': Apellido2}
        
    print("Cargando Lista Cuentas desde Base de Datos")

    #Lee los datos de la tabla cuenta y los carga en la dicc_cuenta 
    sql = "SELECT NumeroCuenta,Cedula,MontoDisponible,Estado FROM Cuenta order by Cedula,NumeroCuenta"
    result = db.ejecutar_consulta(sql)
    for data in result:
        NumeroCuenta = data[0]
        Cedula = data[1]
        MontoDisponible = data[2]
        Estado = data[3]

        if Cedula not in dicc_cuenta:
            dicc_cuenta[Cedula]={'NumeroCuenta':NumeroCuenta,'MontoDisponible':MontoDisponible,'Estado':Estado}

    print("Cargando Lista Movimientos desde Base de Datos")

    #Lee los datos de la tabla movimiento y los carga en la dicc_movimiento 
    sql = "SELECT NumeroMovimiento,Tipo,Fecha,Monto,NumeroCuenta,Cedula FROM Movimiento order by Cedula,NumeroMovimiento"
    result = db.ejecutar_consulta(sql)
    for data in result:
        NumeroMovimiento = data[0]
        Tipo = data[1]
        Fecha = data[2]
        Monto = data[3]
        NumeroCuenta = data[4]
        Cedula = data[5]

        dicc_movimiento[NumeroMovimiento]={'Cedula':Cedula,'Tipo':Tipo,'Fecha':Fecha,'Monto':Monto,'NumeroCuenta':NumeroCuenta}
             
    #Obtiene el número de movimiento mas alto y lo almacena en NumMov 
    sql = "SELECT max(NumeroMovimiento) FROM Movimiento"
    result = db.ejecutar_consulta(sql)

    for data in result:
        if data[0] == None:
            NumMov = 0
        else:
            NumMov = data[0]

        lista_movmax[0] = NumMov

    print("Carga desde Base de Datos FINALIZADA")
    time.sleep(3)

#Escribe los datos de las listas en la base de datos.   
def writeDatabase():
    print("Guardando Listas en Base de Datos")
    print("Guardando Lista Cliente en Base de Datos")
    
    #Almacena la dicc_cliente en la tabla Cliente de la base de datos.
    for Cedula, sub_cliente in dicc_cliente.items():
        Nombre=""
        Apellido1=""
        Apellido2=""
        for datos, valor in sub_cliente.items():
            if (datos == "Nombre"):
                Nombre = valor
            elif (datos == "Apellido1"):
                Apellido1 = valor
            elif (datos == "Apellido2"):
                Apellido2 = valor
                
        #Validar si cédula ya existe.
        sql = "SELECT 'S' FROM Cliente WHERE Cedula = ?"
        parametros = (Cedula,)
        result = db.ejecutar_consulta(sql,parametros)

        existe=""
        for data in result:
            existe= data[0]
            
        if (len(existe) == 0):
            #Si cedula no existe, insertarla
            sql = "INSERT INTO Cliente(Cedula,Nombre,Apellido1,Apellido2) VALUES (?,?,?,?)"
            parametros = (Cedula,Nombre,Apellido1,Apellido2)
            db.ejecutar_consulta(sql,parametros)

    print("Guardando Lista Cuenta en Base de Datos")

    #Almacena la dicc_cuenta en la tabla Cuenta de la base de datos.
    for Cedula, sub_cuenta in dicc_cuenta.items():
        
        NumeroCuenta=0
        Estado=""
        MontoDisponible=0
        for datos, valor in sub_cuenta.items():
            if (datos == 'NumeroCuenta'):
                NumeroCuenta = valor
            elif (datos == 'MontoDisponible'):
                MontoDisponible = valor
            elif (datos == 'Estado'):
                Estado = valor
            
        #Validar si cédula ya existe.
        sql = "SELECT 'S' FROM Cuenta WHERE Cedula = ?"
        parametros = (Cedula,)
        result = db.ejecutar_consulta(sql,parametros)

        existe=""
        for data in result:
            existe= data[0]
            
        if (len(existe) == 0):
            #Si cedula no existe, insertarla
            sql = "INSERT INTO Cuenta(NumeroCuenta,Cedula,MontoDisponible,Estado) VALUES (?,?,?,?)"
            parametros = (NumeroCuenta,Cedula,MontoDisponible,Estado)
            db.ejecutar_consulta(sql,parametros)
        else:
            if (len(existe) != 0):
                #Si cedula existe, actualizar monto disponible y estado
                sql = "UPDATE Cuenta SET MontoDisponible=?,Estado=? WHERE Cedula=? and NumeroCuenta=?"
                parametros = (MontoDisponible,Estado,Cedula,NumeroCuenta)
                db.ejecutar_consulta(sql,parametros)

    print("Guardando Lista Movimiento en Base de Datos")

    #Almacena la dicc_movimiento en la tabla movimiento de la base de datos.
    for NumeroMovimiento, sub_movimiento in dicc_movimiento.items():
        Cedula = 0
        Tipo = ""
        Fecha = ""
        Monto = 0
        NumeroCuenta=0
        for datos, valor in sub_movimiento.items():
            if (datos == 'Cedula'):
                Cedula = valor
            elif (datos == 'Tipo'):
                Tipo = valor
            elif (datos == 'Fecha'):
                Fecha = valor
            elif (datos == 'Monto'):
                Monto = valor
            elif (datos == 'NumeroCuenta'):
                NumeroCuenta = valor
            
        #Validar si cédula y movimiento ya existe.

        sql = "SELECT 'S' FROM Movimiento WHERE Cedula = ? and NumeroMovimiento = ?"
        parametros = (Cedula,NumeroMovimiento,)
        result = db.ejecutar_consulta(sql,parametros)

        existe=""
        for data in result:
            existe= data[0]
            
        if (len(existe) == 0):
            #Si cedula y movimiento no existe, insertarla
            sql = "INSERT INTO Movimiento(NumeroMovimiento,Tipo,Fecha,Monto,NumeroCuenta,Cedula) VALUES (?,?,?,?,?,?)"
            parametros = (NumeroMovimiento,Tipo,Fecha,Monto,NumeroCuenta,Cedula)
            db.ejecutar_consulta(sql,parametros)

    print("Listas guardadas en Base de Datos")
    time.sleep(3)            

#Limpiar pantalla
def limpiarPantalla():
    os.system('cls')

#Menú principal
while True:
    limpiarPantalla()
    
    #Valida si la base de datos esta cargada, y si no la carga en la lista.
    if (carga_bd == "N"):
      readDatabase()
      carga_bd="S"
      
    limpiarPantalla() 
    print("******************************************************************************")
    print("\tLA ALCANCÍA BANK")
    print("******************************************************************************")
    print("\tCLIENTES")
    print("\t[1] - Insertar un cliente")
    print("\t[2] - Consultar clientes")
    print("\tCUENTAS")
    print("\t[3] - Insertar cuenta")
    print("\t[4] - Consultar cuentas")
    print("\tMOVIMIENTOS")
    print("\t[5] - Insertar movimientos")
    print("\t[6] - Consultar movimiento Cliente")
    print("******************************************************************************")
    print("\t[7] - Salir del sistema")
    print("******************************************************************************")

    opcion = int(input("Seleccione una opcion: "))

    if (opcion == 1):
        insertCliente()
        limpiarPantalla()
    elif (opcion == 2):
        readCliente()
        limpiarPantalla()
    elif (opcion == 3):
        insertCuenta()
        limpiarPantalla()   
    elif (opcion == 4):
        readCuenta()
        limpiarPantalla() 
    elif (opcion == 5):
        insertMovs()
        limpiarPantalla() 
    elif (opcion == 6):
        readMovsCliente()
        limpiarPantalla() 
    elif (opcion == 7):
        writeDatabase()
        limpiarPantalla()
        break
    else:
        print("Selecciono una opcion incorrecta. Intente de nuevo...")

    
        
