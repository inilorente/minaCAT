import pandas as pd



##########################################################################################################

#Introducir aquí la ruta del archivo cat entre comillas. NOTA: Las barras de la ruta deben ir duplicadas.

# Ejemplo: C:\\Users\\fulanito\\Escritorio\\archivo.cat



archivocat= "C:\\Users\\02052\\Desktop\\CSV_CATASTRO\\CAT\\ALCORCON_2016-09-24.cat"



##########################################################################################################



#Separación de registros##################################################################################



print 'Leyendo CAT original...'

df0 = pd.read_csv(archivocat, delimiter="··", header=None, encoding = 'ascii')

df0['reg'] = df0[0].str.slice(0,2)

df11 = df0[df0['reg']=='11']

df14 = df0[df0['reg']=='14']

df15 = df0[df0['reg']=='15']

#########################################################################################################

#Generación de atributos según esquema de Catastro ######################################################

#Registro 11 Registro de Finca. Existe uno por cada parcela catastral####################################

print 'Procesando Registro 11...'

df11.is_copy = False

df11['A_TREG'] = 11

df11['B_PCAT'] = df11[0].str.slice(30,44)

df11['C_SUPP'] = df11[0].str.slice(295,305)

df11['D_SUPCT'] = df11[0].str.slice(305,312)

df11['E_SUPCSR'] = df11[0].str.slice(312,319)

df11['F_SUPCBR'] = df11[0].str.slice(319,326)

df11['G_SUPCUB'] = df11[0].str.slice(326,333)

#Registro 14 Registro de Construcción. Existe uno por cada construcción de cada unidad constructiva en cada parcela catastral

print 'Procesando Registro 14...'

df14.is_copy = False

df14['A_TREG'] = 14

df14['B_PCAT'] = df14[0].str.slice(30,44)

df14['C_NBF'] = df14[0].str.slice(50,54)

df14['D_NUC'] = df14[0].str.slice(54,58)

df14['E_SUPT'] = df14[0].str.slice(83,90)

df14['F_TIPOL'] = df14[0].str.slice(104,109)

#Registro 15 Registro de Bien Inmueble. Existirá uno por cada bien inmueble en cada parcela catastral.

print 'Procesando Registro 15...'

df15.is_copy = False

df15['A_TREG'] = 15

df15['B_PCAT'] = df15[0].str.slice(30,44)

df15['C_NBF'] = df15[0].str.slice(44,48)

df15['D_ANT'] = df15[0].str.slice(371,375)

df15['E_USO'] = df15[0].str.slice(427,428)

df15['F_SUPCON'] = df15[0].str.slice(441,451)

df15['G_SUPSOL'] = df15[0].str.slice(451,461)


# Archivos de salida  ##################################################################################

print 'Escribiendo salida...'

rutar11 = "C:\\Users\\02052\\Desktop\\CSV_CATASTRO\\CSV\\CAT_ALCORCON_REG11.csv" #Ruta del registro 11 entre comillas. NOTA: Introducir la extensión .csv#

rutar14 = "C:\\Users\\02052\\Desktop\\CSV_CATASTRO\\CSV\\CAT_ALCORCON_REG14.csv" #Ruta del registro 14 entre comillas. NOTA: Introducir la extensión .csv#

rutar15 = "C:\\Users\\02052\\Desktop\\CSV_CATASTRO\\CSV\\CAT_ALCORCON_REG15.csv" #Ruta del registro 15 entre comillas. NOTA: Introducir la extensión .csv#



# Comandos de salida. NO TOCAR ########################################################################

del df11[0]

df11.to_csv(rutar11)

del df14[0]

df14.to_csv(rutar14)

del df15[0]

df15.to_csv(rutar15)

print '¡Hecho!'
