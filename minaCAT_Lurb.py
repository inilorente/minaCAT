import pandas as pd

##########################################################################################################
#Introducir aquí la ruta del archivo cat entre comillas. NOTA: Las barras de la ruta deben ir duplicadas.
# Ejemplo: C:\\Users\\fulanito\\Escritorio\\archivo.cat

archivocat= "E:\\EARTHLING\\12_minaCAT\\40_900_U_2017-01-20.CAT"

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
df11['1_tipo_reg'] = 11
df11['24_cd'] = df11[0].str.slice(23,25)
df11['26_cmc'] = df11[0].str.slice(25,28)
df11['29_cn'] = df11[0].str.slice(28,30)
df11['31_pc'] = df11[0].str.slice(30,44)
df11['51_cp'] = df11[0].str.slice(50,52)
df11['53_np'] = df11[0].str.slice(52,77)
df11['78_cmc'] = df11[0].str.slice(77,80)
df11['81_cm'] = df11[0].str.slice(80,83)
df11['84_nm'] = df11[0].str.slice(83,123)
df11['124_nem'] = df11[0].str.slice(123,153)
df11['154_cv'] = df11[0].str.slice(153,158)
df11['159_tv'] = df11[0].str.slice(158,163)
df11['164_nv'] = df11[0].str.slice(163,24)
df11['189_pnp'] = df11[0].str.slice(188,192)
df11['198_slp'] = df11[0].str.slice(197,198)
df11['199_km'] = df11[0].str.slice(198,203)
df11['216_td'] = df11[0].str.slice(215,240)
df11['241_dp'] = df11[0].str.slice(240,245)
df11['246_dm'] = df11[0].str.slice(245,247)
df11['248_cma'] = df11[0].str.slice(247,250)
df11['251_czc'] = df11[0].str.slice(250,252)
df11['253_cpo'] = df11[0].str.slice(252,255)
df11['256_cpa'] = df11[0].str.slice(255,260)
df11['261_cpaj'] = df11[0].str.slice(260,265)
df11['266_npa'] = df11[0].str.slice(265,295)
df11['296_sup'] = df11[0].str.slice(295,305)
df11['306_sct'] = df11[0].str.slice(305,312)
df11['313_ssr'] = df11[0].str.slice(312,319)
df11['320_sbr'] = df11[0].str.slice(319,326)
df11['327_sc'] = df11[0].str.slice(326,333)
df11['334_xcen'] = df11[0].str.slice(333,342)
df11['343_ycen'] = df11[0].str.slice(342,352)
df11['582_rc_bice'] = df11[0].str.slice(581,601)
df11['602_n_bice'] = df11[0].str.slice(601,666)
df11['667_srs'] = df11[0].str.slice(666,676)


#Registro 14 Registro de Construcción. Existe uno por cada construcción de cada unidad constructiva en cada parcela catastral
print 'Procesando Registro 14...'
df14.is_copy = False
df14['1_tipo_reg'] = 14
df14['24_cd'] = df14[0].str.slice(23,25)
df14['26_cmc'] = df14[0].str.slice(25,28)
df14['31_pc'] = df14[0].str.slice(30,44)
df14['45_noec'] = df14[0].str.slice(44,48)
df14['51_nobf'] = df14[0].str.slice(50,54)
df14['55_cuc'] = df14[0].str.slice(54,58)
df14['59_bl'] = df14[0].str.slice(58,62)
df14['63_es'] = df14[0].str.slice(62,64)
df14['65_pt'] = df14[0].str.slice(64,67)
df14['68_pu'] = df14[0].str.slice(67,70)
df14['71_cd'] = df14[0].str.slice(70,73)
df14['74_tr'] = df14[0].str.slice(73,74)
df14['75_ar'] = df14[0].str.slice(74,78)
df14['79_aec'] = df14[0].str.slice(78,82)
df14['83_ili'] = df14[0].str.slice(82,83)
df14['84_stl'] = df14[0].str.slice(83,90)
df14['91_spt'] = df14[0].str.slice(90,97)
df14['98_sil'] = df14[0].str.slice(97,104)
df14['105_tip'] = df14[0].str.slice(104,109)
df14['112_modl'] = df14[0].str.slice(111,114)


#Registro 15 Registro de Bien Inmueble. Existirá uno por cada bien inmueble en cada parcela catastral.
print 'Procesando Registro 15...'
df15.is_copy = False
df15['1_tipo_reg'] = 15
df15['24_cd'] = df15[0].str.slice(23,25)
df15['26_cmc'] = df15[0].str.slice(25,28)
df15['29_cn'] = df15[0].str.slice(28,30)
df15['31_pc'] = df15[0].str.slice(30,44)
df15['45_car'] = df15[0].str.slice(44,48)
df15['49_cc1'] = df15[0].str.slice(48,49)
df15['50_cc2'] = df15[0].str.slice(49,50)
df15['51_nfbi'] = df15[0].str.slice(50,58)
df15['59_iia'] = df15[0].str.slice(58,73)
df15['74_nfv'] = df15[0].str.slice(73,92)
df15['93_cp'] = df15[0].str.slice(92,94)
df15['95_np'] = df15[0].str.slice(94,119)
df15['120_cmc'] = df15[0].str.slice(119,122)
df15['123_cm'] = df15[0].str.slice(122,125)
df15['126_nm'] = df15[0].str.slice(125,165)
df15['166_nem'] = df15[0].str.slice(165,195)
df15['196_cv'] = df15[0].str.slice(195,200)
df15['201_tv'] = df15[0].str.slice(200,205)
df15['206_nv'] = df15[0].str.slice(205,230)
df15['231_pnp'] = df15[0].str.slice(230,234)
df15['235_plp'] = df15[0].str.slice(234,235)
df15['236_snp'] = df15[0].str.slice(235,239)
df15['240_slp'] = df15[0].str.slice(239,240)
df15['241_km'] = df15[0].str.slice(240,245)
df15['246_bl'] = df15[0].str.slice(245,249)
df15['250_es'] = df15[0].str.slice(249,251)
df15['252_pt'] = df15[0].str.slice(251,254)
df15['255_pu'] = df15[0].str.slice(254,257)
df15['258_td'] = df15[0].str.slice(257,282)
df15['283_dp'] = df15[0].str.slice(282,287)
df15['288_dm'] = df15[0].str.slice(287,289)
df15['290_cma'] = df15[0].str.slice(289,292)
df15['293_czc'] = df15[0].str.slice(292,294)
df15['295_cpo'] = df15[0].str.slice(294,297)
df15['298_cpa'] = df15[0].str.slice(297,302)
df15['303_cpaj'] = df15[0].str.slice(302,307)
df15['308_npa'] = df15[0].str.slice(307,337)
df15['368_noe'] = df15[0].str.slice(367,371)
df15['372_ant'] = df15[0].str.slice(371,375)
df15['428_grbice'] = df15[0].str.slice(427,428)
df15['442_sfc'] = df15[0].str.slice(441,451)
df15['452_sfs'] = df15[0].str.slice(451,461)
df15['462_cpt'] = df15[0].str.slice(461,470)


# Archivos de salida  ##################################################################################

rutar11 = "E:\\EARTHLING\\12_minaCAT\\SEGOVIA_RG11.csv" #Ruta del registro 11 entre comillas. NOTA: Introducir la extensión .csv#
rutar14 = "E:\\EARTHLING\\12_minaCAT\\SEGOVIA_RG14.csv" #Ruta del registro 14 entre comillas. NOTA: Introducir la extensión .csv#
rutar15 = "E:\\EARTHLING\\12_minaCAT\\SEGOVIA_RG15.csv" #Ruta del registro 15 entre comillas. NOTA: Introducir la extensión .csv#

# Comandos de salida. NO TOCAR ########################################################################
del df11[0]
df11.to_csv(rutar11)
del df14[0]
df14.to_csv(rutar14)
del df15[0]
df15.to_csv(rutar15)