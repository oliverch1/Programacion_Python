import random
import string
import csv
import datetime

def genera_secuencia(N): #2PTOS
    #crear lista alfanumerico y con numeros
    caracteres = list(string.ascii_uppercase) + list(string.digits)
    #caracteres.remove('Ñ') Remover la Ñ en caso de que esté, pero ya no es necesario
    #sacar secuencia de N sin repeticiones
    secuencia = ''.join(random.sample(caracteres, N))
    return secuencia

def suma_montos(monto1, monto2):  #2PTOS
    #eliminar la coma antes de convertir a float
    monto1 = float(monto1.replace(',','')) 
    monto2 = float(monto2.replace(',',''))
    #sumar y redondear a 2 decimales
    suma = round(monto1 + monto2,2)
    #retornar en formato string la suma
    return f'{suma:,.2f}'

def unidades(num): #2PTOS
    #creamos un diccionario con los valores string de los numero del 0 al 9
    cadena = {
        0:'cero',
        1: 'uno',
        2: 'dos',
        3: 'tres',
        4: 'cuatro',
        5: 'cinco',
        6: 'seis',
        7: 'siete',
        8: 'ocho',
        9: 'nueve'
        }
    #mapeamos el numero correspondiente y retornamos
    return cadena.get(num)

def decenas(num): #2PTOS
    cadena = ''
    #separamos el numero en unidades y decenas para un manejo mas comodo
    numero = [int(i) for i in str(num)]
    uni,dece = numero[1],numero[0]
    buscador = dece*10
    #creamos un lista con las decenas base y otro en el rango 11-15
    decena_base = {10:'diez',20:'veinte',30:'treinta',40:'cuarenta',50:'cincuenta',
                   60:'sesenta',70:'setenta',80:'ochenta',90:'noventa'}
    decena_rango_1 = {11:'once',12:'doce',13:'trece',14:'catorce',15:'quince'}
    #prceso de conversion del numero a string 
    if (dece*uni) != 0:
        if num>10 and num<16:
            cadena=decena_rango_1.get(num)
        elif num>15 and num<20:
            cadena='dieci'+unidades(uni)
        elif num>20 and num<30:
            cadena='veinti'+unidades(uni)
        elif num>30:
            cadena=decena_base.get(buscador)+' y '+unidades(uni)
        else:
            None
    else:
        cadena=decena_base.get(num)
    #retorno del string
    return cadena

def centenas(num): #2PTOS
    cadena = ''
    #separamos los digitos del numero
    numeros = [int(i) for i in str(num)]
    centena,decena,unidad=numeros[0],numeros[1],numeros[2]
    #concatenamos la decena y unidad para un control de los numero mayores de 10
    deceuni = int(str(decena)+str(unidad))
    #auxiliar para las centenas base
    buscador=centena*100
    #diccionario para las centenas base
    centena_base={100:'ciento',200:'doscientos',300:'trescientos',400:'cuatrocientos',500:'quinientos',
                  600:'seiscientos',700:'setecientos',800:'ochocientos',900:'novecientos'}
    #proceso de conversion a string el numero
    if (centena*100)==num and (centena*100) != 100:
        cadena = centena_base.get(num)
    elif num == 100:
        cadena = 'cien'
    else:
        if decena == 0:
            cadena = centena_base.get(buscador)+' '+unidades(unidad)
        else:
            cadena = centena_base.get(buscador)+' '+decenas(deceuni)
    #retorno del string
    return cadena

def num2str(num): #2 PTOS
    def caso_especial_1(C,D,U,millar,deceuni,cendeceuni):
        caso_cadena = ''

        casos_millar = {1:'un mil',21:'veinti un mil',31:'treinta y un mil',41:'cuarenta y un mil',51:'cincuenta y un mil',
                        61:'sesenta y un mil',71:'setenta y un mil',81:'ochenta y un mil',91:'noventa y un mil'}

        if C==0 and D==0 and U==0:
            caso_cadena = casos_millar.get(millar)
        else:
            if cendeceuni < 10:
                caso_cadena = casos_millar.get(millar)+' '+unidades(U)
            elif 9<cendeceuni<100:
                caso_cadena = casos_millar.get(millar)+' '+decenas(deceuni)
            else:
                caso_cadena = casos_millar.get(millar)+' '+centenas(cendeceuni)
        return caso_cadena     

    def validacion(dato):
        valores = [1,21,31,41,51,61,71,81,91]
        return dato in valores
    
    def conversion_general_1(C,D,U,millar,deceuni,cendeceuni):
        general_cadena = ''
        if (C+D+U)==0:
            general_cadena = decenas(millar)+' mil'
        else:
            if cendeceuni<10:
                general_cadena = decenas(millar)+' mil '+unidades(U)
            elif 9<cendeceuni<100:
                general_cadena = decenas(millar)+' mil '+decenas(deceuni)
            else:
                general_cadena = decenas(millar)+' mil '+centenas(cendeceuni)
        return general_cadena     

    cadena = ''
    if num < 10000:
        numeros = [int(i) for i in str(num)]
        M,C,D,U = numeros[0],numeros[1],numeros[2],numeros[3]
        deceuni = int(str(D)+str(U))
        cendeceuni = int(str(C)+str(D)+str(U))

        M_base = {1:'mil',2:'dos mil',3:'tres mil',4:'cuatro mil',5:'cinco mil',6:'seis mil',7:'siete mil',
                  8:'ocho mil',9:'nueve mil'}
        
        if (M*1000)==num:
            cadena = M_base.get(M)
        else:
            if cendeceuni<10:
                cadena = M_base.get(M)+' '+unidades(U)
            elif cendeceuni>9 and cendeceuni<100:
                cadena = M_base.get(M)+' '+decenas(deceuni)
            else:
                cadena = M_base.get(M)+' '+centenas(cendeceuni)
    elif 10000<=num<100000:
        numeros = [int(i) for i in str(num)]
        M2,M1,C,D,U = numeros[0],numeros[1],numeros[2],numeros[3],numeros[4]
        deceuni = int(str(D)+str(U))
        cendeceuni = int(str(C)+str(D)+str(U))
        millar = int(str(M2)+str(M1))
        if validacion(millar) is True:
            cadena = caso_especial_1(C,D,U,millar,deceuni,cendeceuni)
        else:
            cadena = conversion_general_1(C,D,U,millar,deceuni,cendeceuni)
    else:
        numeros = [int(i) for i in str(num)]
        M3,M2,M1,C,D,U = numeros[0],numeros[1],numeros[2],numeros[3],numeros[4],numeros[5]
        deceuni = int(str(D)+str(U))
        cendeceuni = int(str(C)+str(D)+str(U))
        millar_dece = int(str(M2)+str(M1))
        millar_cen = int(str(M3)+str(M2)+str(M1))
        if validacion(millar_dece) is True:
            if (M3*100)==100:
                cadena = 'ciento '+caso_especial_1(C,D,U,millar_dece,deceuni,cendeceuni)
            else:
                cadena = centenas(M3*100)+' '+caso_especial_1(C,D,U,millar_dece,deceuni,cendeceuni)
        else:
            if cendeceuni<10:
                cadena = centenas(millar_cen)+' mil '+centenas(cendeceuni)
            elif 9<cendeceuni<100:
                cadena = centenas(millar_cen)+' mil '+centenas(cendeceuni)
            else:
                cadena = centenas(millar_cen)+' mil '+centenas(cendeceuni)
    
    return cadena

def monto2str(monto):  #2 PTOS

    def reemplazando_texto(numero):
        if numero.endswith(" uno"):
            numero = numero[:-4]+" un"
        return numero

    cadena,cadena_entera,cadena_decimal = '','',''

    numero = monto.replace(',','')
    ente,deci = numero.split('.')
    entero,decimal = int(ente),int(deci)
    
    #leer el numero entero en formato bancario 
    if entero<10:
        if entero == 1:
            cadena_entera = 'un nuevo sol '
        else:
            cadena_entera = unidades(entero)+' NUEVOS SOLES '
    elif 9<entero<20:
        cadena_entera = decenas(entero)+' NUEVOS SOLES '
    else:
        if ente.endswith('1') and not ente.endswith('11'):
            if entero<100:
                cadena_entera = reemplazando_texto(decenas(entero))+' NUEVOS SOLES '
            elif 99<entero<1000:
                cadena_entera = reemplazando_texto(centenas(entero))+' NUEVOS SOLES '
            else:
                cadena_entera = reemplazando_texto(num2str(entero))+' NUEVOS SOLES '
        else:
            if entero<100:
                cadena_entera = decenas(entero)+' NUEVOS SOLES '
            elif 99<entero<1000:
                cadena_entera = centenas(entero)+' NUEVOS SOLES '
            else:
                cadena_entera = num2str(entero)+' NUEVOS SOLES '

    #leer el numero decimal en formato bancario
    if decimal<10:
        if decimal == 1:
            cadena_decimal = ' un centimo'
        else:
            cadena_decimal = unidades(decimal)+' centimos'
    else:
        if deci.endswith('1') and not deci.endswith('11'):
            cadena_decimal = reemplazando_texto(decenas(decimal))+' centimos'
        else:
            cadena_decimal = decenas(decimal)+' centimos'
    cadena = f"{cadena_entera} con {cadena_decimal}"
    return cadena.upper()

def cheques(filename):  #3 PTOS.
    info_cheques = {}
    with open(filename,mode='r',encoding='UTF-8') as cheques:
        #usando el reader de csv para tener mas cuidado al momento de separarar los datos
        lectura = csv.reader(cheques)
        #obviamos la cabecera
        cabecera = next(lectura)

        #iteramos sobre cada linea restante del archivo
        for linea in lectura:
            clave = linea[0]
            nombre = linea[1]
            monto = linea[2]
            codigo_pago = genera_secuencia(8)
            if clave in info_cheques:
                info_cheques[clave][1] = suma_montos(info_cheques[clave][1],monto)
            else:
                info_cheques[clave] = [nombre,monto,codigo_pago]
    return info_cheques

def genera_cheque(id_archivo, list_info):  #3 PTOS.
    
    fecha = datetime.datetime.now().strftime("%d/%m/%Y")#fecha y hora actual
    monto = monto2str(list_info[1])#convierte el monto a formato bancario
    nombre_archivo = f"cheque_{id_archivo}.txt"#se crea el archivo txt para su reporte
    
    with open(nombre_archivo,mode='w',encoding='UTF-8') as cheque:
        cheque.write("-"*50+'\n')
        cheque.write(f"Fecha: {fecha}\n")
        cheque.write(f"Cliente: {list_info[0]}\n")
        cheque.write(f"Codigo de pago: {list_info[2]}\n")
        cheque.write(f"Paguese al portador el monto de:\n\n")
        cheque.write(f" "*6+monto+'\n\n')
        cheque.write(f"-"*50)
    
    print(f"Cheque generado: {nombre_archivo}")

#PROGRAMA PRINCIPAL

# Se lee el registro de los pagos a proveedores en un archivo CSV (formato texto)
registro = cheques("data_pagos.txt")

# Se recorre al diccionario retornado y se generan los archivos de texto con las impresiones por cheque
for id_proveedor, payment_info in registro.items():
    genera_cheque(id_proveedor, payment_info)
