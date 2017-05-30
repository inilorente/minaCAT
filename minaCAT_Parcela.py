import pandas as pd



##########################################################################################################

#Introducir aquí la ruta del archivo cat entre comillas. NOTA: Las barras de la ruta deben ir duplicadas.

# Ejemplo: C:\\Users\\fulanito\\Escritorio\\archivo.cat



archivocat= "E:\\EARTHLING\\12_minaCAT\\CAT\\11_27_U_2017-01-20.CAT"



##########################################################################################################



#Separación de registros##################################################################################



print 'Leyendo CAT original...'

df0 = pd.read_csv(archivocat, delimiter="··", header=None)

df0['reg'] = df0[0].str.slice(0,2)

df11 = df0[df0['reg']=='11']

df14 = df0[df0['reg']=='14']

df15 = df0[df0['reg']=='15']

#########################################################################################################

#Generación de atributos según esquema de Catastro ######################################################

#Registro 11 Registro de Finca. Existe uno por cada parcela catastral####################################

print 'Procesando Registro 11...'

df11.is_copy = False

df11['AA_TREG'] = 11

df11['AB_PCAT'] = df11[0].str.slice(30,44)

df11['AC_SUPP'] = df11[0].str.slice(295,305)

df11['AD_SUPCT'] = df11[0].str.slice(305,312)

df11['AE_SUPCSR'] = df11[0].str.slice(312,319)

df11['AF_SUPCBR'] = df11[0].str.slice(319,326)

df11['AG_SUPCUB'] = df11[0].str.slice(326,333)

#Registro 14 Registro de Construcción. Existe uno por cada construcción de cada unidad constructiva en cada parcela catastral

print 'Procesando Registro 14...'

df14.is_copy = False

df14['BA_TREG'] = 14

df14['BB_PCAT'] = df14[0].str.slice(30,44)

df14['BC_NBF'] = df14[0].str.slice(50,54)

df14['BD_NUC'] = df14[0].str.slice(54,58)

df14['BE_USO'] = df14[0].str.slice(70,73)

df14['BF_SUPT'] = df14[0].str.slice(83,90)

df14['BG_TIPOL'] = df14[0].str.slice(104,109)

#Registro 15 Registro de Bien Inmueble. Existirá uno por cada bien inmueble en cada parcela catastral.

print 'Procesando Registro 15...'

df15.is_copy = False

df15['CA_TREG'] = 15

df15['CB_PCAT'] = df15[0].str.slice(30,44)

df15['CC_NBF'] = df15[0].str.slice(44,48)

df15['CD_ANT'] = df15[0].str.slice(371,375)

df15['CE_USO'] = df15[0].str.slice(427,428)

df15['CF_SUPCON'] = df15[0].str.slice(441,451)

df15['CG_SUPSOL'] = df15[0].str.slice(451,461)


# Archivos de salida  ##################################################################################

print 'Escribiendo salida...'

rutar11 = "E:\\EARTHLING\\12_minaCAT\\CSV_minacat\\CAT_CADIZ27_REG11.csv" #Ruta del registro 11 entre comillas. NOTA: Introducir la extensión .csv#

rutar14 = "E:\\EARTHLING\\12_minaCAT\\CSV_minacat\\CAT_CADIZ27_REG14.csv" #Ruta del registro 14 entre comillas. NOTA: Introducir la extensión .csv#

rutar15 = "E:\\EARTHLING\\12_minaCAT\\CSV_minacat\\CAT_CADIZ27_REG15.csv" #Ruta del registro 15 entre comillas. NOTA: Introducir la extensión .csv#



# Comandos de salida. NO TOCAR ########################################################################

del df11[0]

df11.to_csv(rutar11)

del df14[0]

df14.to_csv(rutar14)

del df15[0]

df15.to_csv(rutar15)

print '¡Hecho!'
