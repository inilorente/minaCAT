import pandas as pd

##########################################################################################################
#Introducir aquí la ruta del archivo cat entre comillas. NOTA: Las barras de la ruta deben ir duplicadas.
# Ejemplo: C:\\Users\\fulanito\\Escritorio\\archivo.cat

archivocat= "C:\Users\inilo\Documents\DOCTORADO\MADRID\CATASTRO\CAT\\28_900_U_2017-01-21.CAT"

##########################################################################################################

#Separación de registros##################################################################################

df0 = pd.read_csv(archivocat, delimiter="··", header=None)
# df0 = pd.read_table(archivocat, delimiter=None, header=None) #Solución posible al error de los delimitadores regex. Menor velocidad
df0['reg'] = df0[0].str.slice(0,2)
df11 = df0[df0['reg']=='11']
df13 = df0[df0['reg']=='13']
df14 = df0[df0['reg']=='14']
df15 = df0[df0['reg']=='15']
df16 = df0[df0['reg']=='16']
df17 = df0[df0['reg']=='17']

#########################################################################################################

#Generación de atributos según esquema de Catastro ######################################################

#Registro 11 Registro de Finca. Existe uno por cada parcela catastral####################################

df11.is_copy = False
df11['1_tipo_reg'] = 11
df11['24_cd'] = df11[0].str.slice(24,26)
df11['26_cmc'] = df11[0].str.slice(26,29)
df11['29_cn'] = df11[0].str.slice(29,31)
df11['31_pc'] = df11[0].str.slice(31,45)
df11['51_cp'] = df11[0].str.slice(51,53)
df11['53_np'] = df11[0].str.slice(53,78)
df11['78_cmc'] = df11[0].str.slice(78,81)
df11['81_cm'] = df11[0].str.slice(81,84)
df11['84_nm'] = df11[0].str.slice(84,124)
df11['124_nem'] = df11[0].str.slice(124,154)
df11['154_cv'] = df11[0].str.slice(154,159)
df11['159_tv'] = df11[0].str.slice(159,164)
df11['164_nv'] = df11[0].str.slice(164,25)
df11['189_pnp'] = df11[0].str.slice(189,193)
df11['198_slp'] = df11[0].str.slice(198,199)
df11['199_km'] = df11[0].str.slice(199,204)
df11['216_td'] = df11[0].str.slice(216,241)
df11['241_dp'] = df11[0].str.slice(241,246)
df11['246_dm'] = df11[0].str.slice(246,248)
df11['248_cma'] = df11[0].str.slice(248,251)
df11['251_czc'] = df11[0].str.slice(251,253)
df11['253_cpo'] = df11[0].str.slice(253,256)
df11['256_cpa'] = df11[0].str.slice(256,261)
df11['261_cpaj'] = df11[0].str.slice(261,266)
df11['266_npa'] = df11[0].str.slice(266,296)
df11['296_sup'] = df11[0].str.slice(296,306)
df11['306_sct'] = df11[0].str.slice(306,313)
df11['313_ssr'] = df11[0].str.slice(313,320)
df11['320_sbr'] = df11[0].str.slice(320,327)
df11['327_sc'] = df11[0].str.slice(327,334)
df11['334_xcen'] = df11[0].str.slice(334,343)
df11['343_ycen'] = df11[0].str.slice(343,353)
df11['582_rc_bice'] = df11[0].str.slice(582,602)
df11['602_n_bice'] = df11[0].str.slice(602,667)
df11['667_srs'] = df11[0].str.slice(667,677)

#Registro 13 Registro de Unidad Constructiva. Existe uno por cada unidad constructiva en cada parcela catastral########

df13.is_copy = False
df13['1_tipo_reg'] = 13
df13['24_cd'] = df13[0].str.slice(24,26)
df13['26_cmc'] = df13[0].str.slice(26,29)
df13['26_cmc'] = df13[0].str.slice(31,45)
df13['26_cmc'] = df13[0].str.slice(45,49)
df13['26_cmc'] = df13[0].str.slice(51,53)
df13['26_cmc'] = df13[0].str.slice(53,78)
df13['26_cmc'] = df13[0].str.slice(78,81)
df13['26_cmc'] = df13[0].str.slice(84,124)
df13['26_cmc'] = df13[0].str.slice(124,154)
df13['26_cmc'] = df13[0].str.slice(154,159)
df13['26_cmc'] = df13[0].str.slice(159,164)
df13['26_cmc'] = df13[0].str.slice(164,189)
df13['26_cmc'] = df13[0].str.slice(189,193)
df13['26_cmc'] = df13[0].str.slice(193,194)
df13['26_cmc'] = df13[0].str.slice(194,198)
df13['26_cmc'] = df13[0].str.slice(198,199)
df13['26_cmc'] = df13[0].str.slice(199,204)
df13['26_cmc'] = df13[0].str.slice(216,241)
df13['26_cmc'] = df13[0].str.slice(296,300)
df13['26_cmc'] = df13[0].str.slice(300,301)
df13['26_cmc'] = df13[0].str.slice(308,313)
df13['26_cmc'] = df13[0].str.slice(410,414)

#Registro 14 Registro de Construcción. Existe uno por cada construcción de cada unidad constructiva en cada parcela catastral

df14.is_copy = False
df14['1_tipo_reg'] = 14
df14['24_cd'] = df14[0].str.slice(24,26)
df14['26_cmc'] = df14[0].str.slice(26,29)
df14['31_pc'] = df14[0].str.slice(31,45)
df14['45_noec'] = df14[0].str.slice(45,49)
df14['51_nobf'] = df14[0].str.slice(51,55)
df14['55_cuc'] = df14[0].str.slice(55,59)
df14['59_bl'] = df14[0].str.slice(59,63)
df14['63_es'] = df14[0].str.slice(63,65)
df14['65_pt'] = df14[0].str.slice(65,68)
df14['68_pu'] = df14[0].str.slice(68,71)
df14['71_cd'] = df14[0].str.slice(71,74)
df14['74_tr'] = df14[0].str.slice(74,75)
df14['75_ar'] = df14[0].str.slice(75,79)
df14['79_aec'] = df14[0].str.slice(79,83)
df14['83_ili'] = df14[0].str.slice(83,84)
df14['84_stl'] = df14[0].str.slice(84,91)
df14['91_spt'] = df14[0].str.slice(91,98)
df14['98_sil'] = df14[0].str.slice(98,105)
df14['105_tip'] = df14[0].str.slice(105,110)
df14['112_modl'] = df14[0].str.slice(112,115)

#Registro 15 Registro de Bien Inmueble. Existirá uno por cada bien inmueble en cada parcela catastral.

df15.is_copy = False
df15['1_tipo_reg'] = 15
df15['24_cd'] = df15[0].str.slice(24,26)
df15['26_cmc'] = df15[0].str.slice(26,29)
df15['29_cn'] = df15[0].str.slice(29,31)
df15['31_pc'] = df15[0].str.slice(31,45)
df15['45_car'] = df15[0].str.slice(45,49)
df15['49_cc1'] = df15[0].str.slice(49,50)
df15['50_cc2'] = df15[0].str.slice(50,51)
df15['51_nfbi'] = df15[0].str.slice(51,59)
df15['59_iia'] = df15[0].str.slice(59,74)
df15['74_nfv'] = df15[0].str.slice(74,93)
df15['93_cp'] = df15[0].str.slice(93,95)
df15['95_np'] = df15[0].str.slice(95,120)
df15['120_cmc'] = df15[0].str.slice(120,123)
df15['123_cm'] = df15[0].str.slice(123,126)
df15['126_nm'] = df15[0].str.slice(126,166)
df15['166_nem'] = df15[0].str.slice(166,196)
df15['196_cv'] = df15[0].str.slice(196,201)
df15['201_tv'] = df15[0].str.slice(201,206)
df15['206_nv'] = df15[0].str.slice(206,231)
df15['231_pnp'] = df15[0].str.slice(231,235)
df15['235_plp'] = df15[0].str.slice(235,236)
df15['236_snp'] = df15[0].str.slice(236,240)
df15['240_slp'] = df15[0].str.slice(240,241)
df15['241_km'] = df15[0].str.slice(241,246)
df15['246_bl'] = df15[0].str.slice(246,250)
df15['250_es'] = df15[0].str.slice(250,252)
df15['252_pt'] = df15[0].str.slice(252,255)
df15['255_pu'] = df15[0].str.slice(255,258)
df15['258_td'] = df15[0].str.slice(258,283)
df15['283_dp'] = df15[0].str.slice(283,288)
df15['288_dm'] = df15[0].str.slice(288,290)
df15['290_cma'] = df15[0].str.slice(290,293)
df15['293_czc'] = df15[0].str.slice(293,295)
df15['295_cpo'] = df15[0].str.slice(295,298)
df15['298_cpa'] = df15[0].str.slice(298,303)
df15['303_cpaj'] = df15[0].str.slice(303,308)
df15['308_npa'] = df15[0].str.slice(308,338)
df15['368_noe'] = df15[0].str.slice(368,372)
df15['372_ant'] = df15[0].str.slice(372,376)
df15['428_grbice'] = df15[0].str.slice(428,429)
df15['442_sfc'] = df15[0].str.slice(442,452)
df15['452_sfs'] = df15[0].str.slice(452,462)
df15['462_cpt'] = df15[0].str.slice(462,471)

# Generación de IDs  ##################################################################################

df11 = df11.reset_index()
df13 = df13.reset_index()
df14 = df14.reset_index()
df15 = df15.reset_index()

# Archivos de salida  ##################################################################################

rutar11 = "F:\ACTUAL\\LUrB\\CATASTRO\\SEGOVIA_RG11.csv" #Ruta del registro 11 entre comillas. NOTA: Introducir la extensión .csv#
rutar13 = "F:\ACTUAL\\LUrB\\CATASTRO\\SEGOVIA_RG13.csv" #Ruta del registro 13 entre comillas. NOTA: Introducir la extensión .csv#
rutar14 = "F:\ACTUAL\\LUrB\\CATASTRO\\SEGOVIA_RG14.csv" #Ruta del registro 14 entre comillas. NOTA: Introducir la extensión .csv#
rutar15 = "F:\ACTUAL\\LUrB\\CATASTRO\\SEGOVIA_RG15.csv" #Ruta del registro 15 entre comillas. NOTA: Introducir la extensión .csv#

# Comandos de salida. NO TOCAR ########################################################################
del df11[0]
df11.to_csv(rutar11)
del df13[0]
df13.to_csv(rutar13)
del df14[0]
df14.to_csv(rutar14)
del df15[0]
df15.to_csv(rutar15)


