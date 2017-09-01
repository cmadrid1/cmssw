# ------------------------------------
# -- This file contains some basic 
# -- information about the 2015 test 
# -- beam runs.
# --
# -- Originally created by: 
# -- Nadja Strobbe & Jay Dittmann
# ------------------------------------

# EMAPS
EMAP_default = "EMAP-QIE11-L00-21AUG2015-04.txt"
EMAP_specialODU = "EMAP-QIE11-SPECIAL-ODU-22AUG2015-02.txt"
EMAP_2017 = "EMAP_AC05_01AUG2017_NOMINAL.txt"
# runtable format:
# runTable[runnumber] = [eta, phi, nev, beamcounters, beamtype, QIE shunt, emap]


#######################
# table for Aug 13
# Phase 2 eta-phi scan
#######################

runTable_Aug13 = {}

runTable_Aug13[8530] = (8100, 40500, 300000, "", "", "1", EMAP_default)
runTable_Aug13[8531] = (8200, 40500, 300000, "", "", "1", EMAP_default)
runTable_Aug13[8532] = (8310, 40500, 300000, "", "", "1", EMAP_default)
runTable_Aug13[8533] = (8310, 40500, 107500, "", "", "1", EMAP_default)
runTable_Aug13[8535] = (8390, 40500, 400000, "", "", "1", EMAP_default)


#######################
# table for Aug 14 scan
# full eta-phi scan
#######################

runTable_Aug14 = {}

runTable_Aug14[8536] = (9583, 23400, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8537] = (9964, 23400, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8538] = (10285, 23400, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8539] = (10597, 23400, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8540] = (10884, 23400, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8541] = (11154, 23400, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8542] = (11419, 23400, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8543] = (11688, 23400, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8544] = (11963, 23400, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8545] = (12241, 23400, 50000, "14", "150m", "1", EMAP_default) 

runTable_Aug14[8546] = (9583, 3482, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8547] = (9964, 3482, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8548] = (10285, 3482, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8549] = (10597, 3482, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8550] = (10884, 3482, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8551] = (11154, 3482, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8552] = (11419, 3482, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8553] = (11688, 3482, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8556] = (11963, 3482, 50000, "14", "150m", "1", EMAP_default) 
runTable_Aug14[8557] = (12241, 3482, 50000, "14", "150m", "1", EMAP_default) 


#########################################
# Muon data - Large stat for Ph2
#########################################

runTable_Ph2_Aug14 = {}

runTable_Ph2_Aug14[8558] = (10884, 23400, 300000, "", "", "1", EMAP_default)
runTable_Ph2_Aug14[8559] = (12241, 23400, 300000, "", "", "1", EMAP_default)
runTable_Ph2_Aug14[8560] = (9583, 23400, 300000, "", "", "1", EMAP_default)
runTable_Ph2_Aug14[8561] = (9583, 3482, 300000, "", "", "1", EMAP_default)
runTable_Ph2_Aug14[8566] = (8390, 40500, 305000, "", "", "1", EMAP_default)
runTable_Ph2_Aug14[8570] = (8450, 40500, 176231, "", "ped", "1", EMAP_default)

runTable_Ph2_Aug15 = {}

runTable_Ph2_Aug15[8578] = (8479, 40500, 300000, "", "150m", "1", EMAP_default)
runTable_Ph2_Aug15[8579] = (8370, 40500, 500000, "", "150m", "1", EMAP_default)
runTable_Ph2_Aug15[8580] = (8370, 40500, 500000, "", "150m", "1", EMAP_default)
runTable_Ph2_Aug15[8581] = (8500, 40500, 1000000, "", "150m", "1", EMAP_default)

#########################################
# Muon data - finely binned eta-phi scan
#########################################

runTable_Aug15 = {}

runTable_Aug15[8582] = (9884,40500,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8583] = (9884,36800,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8584] = (9884,33100,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8585] = (9884,29400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8586] = (9884,25700,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8587] = (9884,22000,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8588] = (9884,18300,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8589] = (9884,14600,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8590] = (9884,10900,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8591] = (9884,7200,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8592] = (9884,3482,5000,"134","150m", "1", EMAP_default)

runTable_Aug15[8594] = (9503,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8593] = (9573,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8595] = (9643,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8596] = (9713,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8597] = (9783,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8598] = (9853,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8599] = (9923,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8600] = (9993,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8601] = (10063,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8602] = (10133,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8603] = (10205,23400,5000,"134","150m", "1", EMAP_default)

runTable_Aug15[8604] = (10804,40500,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8606] = (10804,36800,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8607] = (10804,33100,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8608] = (10804,29400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8609] = (10804,25700,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8610] = (10804,22000,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8611] = (10804,18300,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8612] = (10804,14600,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8614] = (10804,10900,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8615] = (10804,7200,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8616] = (10804,3482,5000,"134","150m", "1", EMAP_default)

runTable_Aug15[8617] = (10517,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8618] = (10572,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8619] = (10627,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8620] = (10682,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8621] = (10737,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8622] = (10792,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8624] = (10847,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8625] = (10903,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8626] = (10957,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8627] = (11012,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8628] = (11067,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8629] = (11074,23400,5000,"134","150m", "1", EMAP_default)

runTable_Aug15[8630] = (8200,40500,489257,"134","150m", "1", EMAP_default)

runTable_Aug15[8632] = (11884,40500,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8633] = (11884,36799,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8634] = (11884,33099,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8636] = (11884,29101,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8637] = (11884,25700,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8638] = (11884,22101,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8639] = (11884,21999,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8640] = (11884,18299,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8641] = (11884,14599,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8642] = (11884,10900,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8643] = (11884,7200,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8644] = (11884,3482,5000,"134","150m", "1", EMAP_default)

runTable_Aug15[8645] = (11609,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8646] = (11664,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8647] = (11717,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8648] = (11774,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8649] = (11826,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8650] = (11882,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8651] = (11939,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8652] = (11992,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8653] = (12048,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8654] = (12104,23400,5000,"134","150m", "1", EMAP_default)
runTable_Aug15[8655] = (12158,23400,5000,"134","150m", "1", EMAP_default)

######################################
# Pion data from before beam was lost
###################################### 

runTable_pions_Aug15 = {}

runTable_pions_Aug15[8656] = (10804, 23400, 241547, "134", "50p", "1", EMAP_default)

######################################
# Pion data - Round A
###################################### 

runTable_pions_ODU12 = {}

#runTable[runnumber] = [eta, phi, nev, beamcounters, beamtype, shunt]
runTable_pions_ODU12[8749] = (10350,23400,100000,"14","150p","1/5", EMAP_default)
runTable_pions_ODU12[8750] = (10350,23400,100000,"14","150p","1/11.5", EMAP_default)
runTable_pions_ODU12[8751] = (10650,23400,100000,"14","150p","1/5", EMAP_default)
runTable_pions_ODU12[8752] = (10650,24300,100000,"14","150p","1/11.5", EMAP_default)
runTable_pions_ODU12[8755] = (10925,24300,100000,"14","150p","1/5", EMAP_default)
runTable_pions_ODU12[8756] = (10925,24300,100000,"14","150p","1/11.5", EMAP_default) # might contain events with bad links

runTable_pions_ODU12[8757] = (10350,23400,100000,"14","100p","1", EMAP_default)
runTable_pions_ODU12[8758] = (10350,23400,250000,"14","100p","1/5", EMAP_default)
runTable_pions_ODU12[8759] = (10350,23400,250000,"14","100p","1/5", EMAP_default)
runTable_pions_ODU12[8760] = (10350,23400,250000,"14","100p","1/5", EMAP_default)
runTable_pions_ODU12[8761] = (10350,23400,250000,"14","100p","1/5", EMAP_default)
runTable_pions_ODU12[8762] = (10350,23400,100000,"14","100p","1/11.5", EMAP_default)
runTable_pions_ODU12[8763] = (10650,23400,100000,"14","100p","1", EMAP_default)
runTable_pions_ODU12[8764] = (10650,23400,30321,"14","100p","1/5", EMAP_default)
runTable_pions_ODU12[8765] = (10650,23400,32000,"14","100p","1/5", EMAP_default)
runTable_pions_ODU12[8766] = (10650,23400,70000,"14","100p","1/5", EMAP_default)
runTable_pions_ODU12[8767] = (10650,23400,100000,"14","100p","1/11.5", EMAP_default)
runTable_pions_ODU12[8768] = (10925,23400,100000,"14","100p","1", EMAP_default)
runTable_pions_ODU12[8769] = (10925,23400,100000,"14","100p","1/5", EMAP_default)
runTable_pions_ODU12[8770] = (10925,23400,100000,"14","100p","1/11.5", EMAP_default)

runTable_pions_ODU12[8794] = (10350, 23400, 100000, "14", "300p", "1/5", EMAP_default)
runTable_pions_ODU12[8793] = (10350, 23400, 100000, "14", "300p", "1/11.5", EMAP_default) # links reinitialized during run (before 25k events)
runTable_pions_ODU12[8781] = (10650, 23400, 20000, "14", "300p", "1/5", EMAP_default)
runTable_pions_ODU12[8782] = (10650, 23400, 41519, "14", "300p", "1/5", EMAP_default)
runTable_pions_ODU12[8784] = (10650, 23400, 40000, "14", "300p", "1/5", EMAP_default)
runTable_pions_ODU12[8777] = (10650, 23400, 84962, "14", "300p", "1/11.5", EMAP_default)
runTable_pions_ODU12[8780] = (10650, 23400, 20000, "14", "300p", "1/11.5", EMAP_default)
runTable_pions_ODU12[8774] = (10925, 23400, 100000, "14", "300p", "1/5", EMAP_default) # beam was displaced for ~4-5mins
runTable_pions_ODU12[8773] = (10925, 23400, 100000, "14", "300p", "1/11.5", EMAP_default) # beam was displaced for ~3mins

runTable_pions_ODU12[8795] = (10350, 23400, 100000, "14", "200p", "1/5", EMAP_default)
runTable_pions_ODU12[8796] = (10350, 23400, 100000, "14", "200p", "1/11.5", EMAP_default)
runTable_pions_ODU12[8797] = (10650, 23400, 100000, "14", "200p", "1/5", EMAP_default)
runTable_pions_ODU12[8798] = (10650, 23400, 100000, "14", "200p", "1/11.5", EMAP_default)
runTable_pions_ODU12[8799] = (10925, 23400, 100000, "14", "200p", "1/5", EMAP_default)
runTable_pions_ODU12[8800] = (10925, 23400, 100000, "14", "200p", "1/11.5", EMAP_default)

runTable_pions_ODU12[8810] = (10350, 23400, 100000, "14", "30p", "1", EMAP_default)
runTable_pions_ODU12[8809] = (10350, 23400, 100000, "14", "30p", "1/5", EMAP_default)
runTable_pions_ODU12[8807] = (10650, 23400, 100000, "14", "30p", "1", EMAP_default)
runTable_pions_ODU12[8806] = (10650, 23400, 100000, "14", "30p", "1/5", EMAP_default)
runTable_pions_ODU12[8803] = (10925, 23400, 100000, "14", "30p", "1", EMAP_default)
runTable_pions_ODU12[8801] = (10925, 23400, 100000, "14", "30p", "1/5", EMAP_default)

runTable_pions_ODU12[8811] = (10350, 23400, 100000, "14", "50p", "1", EMAP_default)
runTable_pions_ODU12[8812] = (10350, 23400, 100000, "14", "50p", "1/5", EMAP_default)
runTable_pions_ODU12[8813] = (10650, 23400, 100000, "14", "50p", "1", EMAP_default)
runTable_pions_ODU12[8814] = (10650, 23400, 100000, "14", "50p", "1/5", EMAP_default)
runTable_pions_ODU12[8815] = (10925, 23400, 100000, "14", "50p", "1", EMAP_default)
runTable_pions_ODU12[8816] = (10925, 23400, 100000, "14", "50p", "1/5", EMAP_default)

runTable_pions_ODU12[8820] = (10350, 23400, 100000, "14", "150p", "1", EMAP_default)
runTable_pions_ODU12[8819] = (10350, 23400, 100000, "14", "150p", "1/3", EMAP_default)
runTable_pions_ODU12[8818] = (10350, 23400, 100000, "14", "150p", "1/9", EMAP_default)
runTable_pions_ODU12[8817] = (10925, 23400, 100000, "14", "150p", "1/11.5", EMAP_default)


######################################
# Muon data - Round B
###################################### 

runTable_muons_specialODU = {}

runTable_muons_specialODU[8849] = (10000, 3482, 5000, "134", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8850] = (10350, 3482, 5000, "134", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8851] = (10650, 3482, 5000, "134", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8852] = (10000, 23400, 5000, "134", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8853] = (10350, 23400, 5000, "134", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8854] = (10650, 23400, 5000, "134", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8855] = (10000, 40500, 5000, "134", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8856] = (10350, 40500, 5000, "134", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8857] = (10650, 40500, 5000, "134", "150m", "1", EMAP_specialODU)

runTable_muons_specialODU[8858] = (10000, 3482, 10000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8859] = (10350, 3482, 10000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8860] = (10650, 3482, 10000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8861] = (10000, 23400, 10000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8862] = (10350, 23400, 10000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8863] = (10650, 23400, 10000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8864] = (10000, 40500, 10000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8865] = (10350, 40500, 10000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU[8866] = (10650, 40500, 10000, "14", "150m", "1", EMAP_specialODU)

######################################
# Pion data - Round C
###################################### 

runTable_pions_specialODU = {}

runTable_pions_specialODU[8867] = (10350, 23400, 100000, "14", "30p", "1", EMAP_specialODU)
runTable_pions_specialODU[8869] = (10350, 23400, 1000, "14", "30p", "1/5", EMAP_specialODU)
runTable_pions_specialODU[8870] = (10350, 23400, 100000, "14", "30p", "1/5", EMAP_specialODU)

runTable_pions_specialODU[8872] = (10350, 23400, 100000, "14", "50p", "1", EMAP_specialODU) # beam shape vertically centered during run
runTable_pions_specialODU[8873] = (10350, 23400, 100000, "14", "50p", "1/5", EMAP_specialODU)

runTable_pions_specialODU[8874] = (10350, 23400, 100000, "14", "100p", "1", EMAP_specialODU)
runTable_pions_specialODU[8875] = (10350, 23400, 250000, "14", "100p", "1/5", EMAP_specialODU)
runTable_pions_specialODU[8876] = (10350, 23400, 250000, "14", "100p", "1/5", EMAP_specialODU)
runTable_pions_specialODU[8877] = (10350, 23400, 250000, "14", "100p", "1/5", EMAP_specialODU)
runTable_pions_specialODU[8878] = (10350, 23400, 250000, "14", "100p", "1/5", EMAP_specialODU)
runTable_pions_specialODU[8879] = (10350, 23400, 100000, "14", "100p", "1/11.5", EMAP_specialODU)

runTable_pions_specialODU[8880] = (10350, 23400, 100000, "14", "150p", "1/5", EMAP_specialODU)
runTable_pions_specialODU[8881] = (10350, 23400, 100000, "14", "150p", "1/11.5", EMAP_specialODU)
runTable_pions_specialODU[8882] = (10350, 23400, 100000, "14", "200p", "1/5", EMAP_specialODU)
runTable_pions_specialODU[8883] = (10350, 23400, 100000, "14", "200p", "1/11.5", EMAP_specialODU)
runTable_pions_specialODU[8884] = (10350, 23400, 100000, "14", "300p", "1/5", EMAP_specialODU)
runTable_pions_specialODU[8885] = (10350, 23400, 100000, "14", "300p", "1/11.5", EMAP_specialODU)

runTable_pions_specialODU[8913] = (10350, 23400, 100000, "14", "150p", "1", EMAP_specialODU)
runTable_pions_specialODU[8914] = (10350, 23400, 100000, "14", "150p", "1/3", EMAP_specialODU)
runTable_pions_specialODU[8915] = (10350, 23400, 100000, "14", "150p", "1/9", EMAP_specialODU)
runTable_pions_specialODU[8932] = (10350, 23400, 50000, "14", "300p", "1", EMAP_specialODU)
runTable_pions_specialODU[8931] = (10350, 23400, 50000, "14", "300p", "1/3", EMAP_specialODU)
runTable_pions_specialODU[8930] = (10350, 23400, 50000, "14", "300p", "1/9", EMAP_specialODU)
runTable_pions_specialODU[8936] = (10350, 23400, 50000, "14", "200p", "1", EMAP_specialODU)
runTable_pions_specialODU[8935] = (10350, 23400, 50000, "14", "200p", "1/3", EMAP_specialODU)
runTable_pions_specialODU[8934] = (10350, 23400, 50000, "14", "200p", "1/9", EMAP_specialODU)

runTable_pions_specialODU[8938] = (10450, 30300, 100000, "14", "150p", "1", EMAP_specialODU) # Was supposed to be muons
runTable_pions_specialODU[8939] = (10450, 30300, 100000, "14", "150p", "1", EMAP_specialODU) # Was supposed to be muons
runTable_pions_specialODU[8940] = (10450, 30300, 51525, "14", "150p", "1", EMAP_specialODU) # Was supposed to be muons
runTable_pions_specialODU[8943] = (10450, 30300, 100000, "14", "150p", "1", EMAP_specialODU) # Was supposed to be muons, temp RM1 SiPMs at 12-13C

######################################
# Muon data - Phase 2 long runs
###################################### 

runTable_muons_specialODU_forPhase2 = {}

runTable_muons_specialODU_forPhase2[8887] = (10460, 28900, 250000, "14", "150m", "1", EMAP_specialODU) # most likely link issue
runTable_muons_specialODU_forPhase2[8888] = (10460, 28900, 250000, "14", "150m", "1", EMAP_specialODU) # most likely link issue
runTable_muons_specialODU_forPhase2[8889] = (10460, 28900, 250000, "14", "150m", "1", EMAP_specialODU) # link stability issue

runTable_muons_specialODU_forPhase2[8890] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8891] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8892] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8893] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8894] = (10450, 30300, 138225, "14", "150m", "1", EMAP_specialODU)

runTable_muons_specialODU_forPhase2[8895] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8896] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8900] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8901] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8903] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8904] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)

runTable_muons_specialODU_forPhase2[8905] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU) # links reinitialized by shifters, unclear whether there was real problem
runTable_muons_specialODU_forPhase2[8906] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU) # links reinitialized by shifters, unclear whether there was real problem
runTable_muons_specialODU_forPhase2[8907] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8908] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8909] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU) # links reinitialized by shifters, unclear whether there was real problem
runTable_muons_specialODU_forPhase2[8910] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8911] = (10450, 30300, 250000, "14", "150m", "1", EMAP_specialODU)

runTable_muons_specialODU_forPhase2[8950] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8951] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8952] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8953] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8954] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8955] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8957] = (10450, 30800, 58025, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8959] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8960] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8961] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)
runTable_muons_specialODU_forPhase2[8963] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU)

runTable_muons_specialODU_forPhase2[8964] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # temp 25C and increasing
runTable_muons_specialODU_forPhase2[8965] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # temp 32C and increasing
runTable_muons_specialODU_forPhase2[8967] = (10450, 30800, 10000, "14", "150m", "1", EMAP_specialODU) # temp 39C, no HPD, no CM
runTable_muons_specialODU_forPhase2[8968] = (10450, 30800, 10000, "14", "150m", "1", EMAP_specialODU) # temp 40C, no HPD, no CM
runTable_muons_specialODU_forPhase2[8969] = (10450, 30800, 50000, "14", "150m", "1", EMAP_specialODU) # temp 41-42C, no HPD, no CM
runTable_muons_specialODU_forPhase2[8970] = (10450, 30800, 50000, "14", "150m", "1", EMAP_specialODU) # temp 40-41C, no HPD, no CM
runTable_muons_specialODU_forPhase2[8972] = (10450, 30800, 50000, "14", "150m", "1", EMAP_specialODU) # temp 36C, no HPD, no CM
runTable_muons_specialODU_forPhase2[8973] = (10450, 30800, 50000, "14", "150m", "1", EMAP_specialODU) # temp 35C, no HPD, no CM
runTable_muons_specialODU_forPhase2[8975] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # temp 34C, no HPD, no CM
runTable_muons_specialODU_forPhase2[8976] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # temp 34C, no HPD, no CM

runTable_muons_specialODU_forPhase2[8981] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8982] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8983] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8984] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8985] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8987] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8988] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8989] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8990] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8991] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8992] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8993] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8994] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8995] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8996] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8997] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8998] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[8999] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9000] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9001] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9002] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9003] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9004] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9005] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9006] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9007] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9008] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9009] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9010] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9011] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9012] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9013] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM
runTable_muons_specialODU_forPhase2[9014] = (10450, 30800, 100000, "14", "150m", "1", EMAP_specialODU) # no HPD, no CM


######################################
# Testbeam 2017
###################################### 
runtable2017 = {}

runtable2017[3234] = (10350,3482,10000,"124","150m","1",EMAP_2017)
runtable2017[3233] = (10350,3482,10000,"124","150m","6",EMAP_2017)
runtable2017[3232] = (10650,3482,10000,"124","150m","1",EMAP_2017)
runtable2017[3231] = (10650,3482,10000,"124","150m","6",EMAP_2017)
runtable2017[3230] = (10975,3482,10000,"124","150m","1",EMAP_2017)
runtable2017[3229] = (10975,3482,10000,"124","150m","6",EMAP_2017)
runtable2017[3228] = (10350,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3227] = (10350,23400,10000,"124","150m","6",EMAP_2017)
runtable2017[3226] = (10650,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3225] = (10650,23400,10000,"124","150m","6",EMAP_2017)
runtable2017[3224] = (10975,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3223] = (10975,23400,10000,"124","150m","6",EMAP_2017)
runtable2017[3222] = (10350,40500,10000,"124","150m","1",EMAP_2017)
runtable2017[3221] = (10350,40500,10000,"124","150m","6",EMAP_2017)
runtable2017[3220] = (10650,40500,10000,"124","150m","1",EMAP_2017)
runtable2017[3219] = (10650,40500,10000,"124","150m","6",EMAP_2017)
runtable2017[3217] = (10975,40500,10000,"124","150m","1",EMAP_2017)
runtable2017[3218] = (10975,40500,10000,"124","150m","6",EMAP_2017)
runtable2017[3379] = (10350,57600,3379,"124","150m","1",EMAP_2017)
runtable2017[3380] = (10350,57600,10000,"124","150m","1",EMAP_2017)
runtable2017[3381] = (10350,57600,10000,"124","150m","6",EMAP_2017)
runtable2017[3382] = (10650,57600,10000,"124","150m","1",EMAP_2017)
runtable2017[3383] = (10650,57600,10000,"124","150m","6",EMAP_2017)
runtable2017[3384] = (10975,57600,10000,"124","150m","1",EMAP_2017)
runtable2017[3385] = (10975,57600,10000,"124","150m","6",EMAP_2017)
runtable2017[3473] = (10350,57600,10000,"124","200m","1",EMAP_2017)
runtable2017[3474] = (10650,57600,10000,"124","200m","1",EMAP_2017)
runtable2017[3475] = (10975,57600,10000,"124","200m","1",EMAP_2017)
runtable2017[3195] = (10650,23400,100000,"124","30p","1",EMAP_2017)
runtable2017[3196] = (10650,23400,100000,"124","30p","6",EMAP_2017)
runtable2017[3197] = (10650,23400,100000,"124","30p","1",EMAP_2017)
runtable2017[3198] = (10650,23400,100000,"124","30p","1",EMAP_2017)
runtable2017[3199] = (10650,23400,100000,"124","30p","6",EMAP_2017)
runtable2017[3200] = (10650,23400,100000,"124","30p","6",EMAP_2017)
runtable2017[3187] = (10650,23400,100000,"124","50p","1",EMAP_2017)
runtable2017[3189] = (10650,23400,100000,"124","50p","6",EMAP_2017)
runtable2017[3190] = (10650,23400,100000,"124","50p","1",EMAP_2017)
runtable2017[3191] = (10650,23400,2000,"124","50p","1",EMAP_2017)
runtable2017[3192] = (10650,23400,100000,"124","50p","1",EMAP_2017)
runtable2017[3193] = (10650,23400,100000,"124","50p","6",EMAP_2017)
runtable2017[3194] = (10650,23400,100000,"124","50p","6",EMAP_2017)
runtable2017[3201] = (10650,23400,100000,"124","80p","1",EMAP_2017)
runtable2017[3202] = (10650,23400,100000,"124","80p","6",EMAP_2017)
runtable2017[3203] = (10650,23400,100000,"124","80p","1",EMAP_2017)
runtable2017[3204] = (10650,23400,100000,"124","80p","1",EMAP_2017)
runtable2017[3205] = (10650,23400,100000,"124","80p","6",EMAP_2017)
runtable2017[3206] = (10650,23400,100000,"124","80p","6",EMAP_2017)
runtable2017[3207] = (10650,23400,100000,"124","100p","1",EMAP_2017)
runtable2017[3208] = (10650,23400,100000,"124","100p","6",EMAP_2017)
runtable2017[3209] = (10650,23400,100000,"124","100p","1",EMAP_2017)
runtable2017[3210] = (10650,23400,100000,"124","100p","1",EMAP_2017)
runtable2017[3211] = (10650,23400,100000,"124","100p","6",EMAP_2017)
runtable2017[3212] = (10650,23400,100000,"124","100p","6",EMAP_2017)
runtable2017[3137] = (10650,23400,30000,"124","150p","1",EMAP_2017)
runtable2017[3239] = (10650,23400,25000,"124","150p","1",EMAP_2017)
runtable2017[3139] = (10650,23400,30000,"124","150p","6",EMAP_2017)
runtable2017[3240] = (10650,23400,100000,"124","150p","6",EMAP_2017)
runtable2017[3138] = (10650,23400,30000,"124","150p","1",EMAP_2017)
runtable2017[3241] = (10650,23400,56324,"124","150p","1",EMAP_2017)
runtable2017[3242] = (10650,23400,45000,"124","150p","1",EMAP_2017)
runtable2017[3243] = (10650,23400,19100,"124","150p","1",EMAP_2017)
runtable2017[3349] = (10650,23400,50000,"124","150p","1",EMAP_2017)
runtable2017[3140] = (10650,23400,30000,"124","150p","1",EMAP_2017)
runtable2017[3350] = (10650,23400,50000,"124","150p","1",EMAP_2017)
runtable2017[3351] = (10650,23400,50000,"124","150p","6",EMAP_2017)
runtable2017[3352] = (10650,23400,50000,"124","150p","6",EMAP_2017)
runtable2017[3143] = (10650,23400,30000,"124","200p","1",EMAP_2017)
runtable2017[3328] = (10650,23400,31000,"124","200p","1",EMAP_2017)
runtable2017[3329] = (10650,23400,25000,"124","200p","1",EMAP_2017)
runtable2017[3145] = (10650,23400,30000,"124","200p","6",EMAP_2017)
runtable2017[3330] = (10650,23400,50000,"124","200p","6",EMAP_2017)
runtable2017[3146] = (10650,23400,30000,"124","200p","1",EMAP_2017)
runtable2017[3331] = (10650,23400,50000,"124","200p","1",EMAP_2017)
runtable2017[3148] = (10650,23400,30000,"124","200p","1",EMAP_2017)
runtable2017[3332] = (10650,23400,50000,"124","200p","1",EMAP_2017)
runtable2017[3150] = (10650,23400,30000,"124","250p","1",EMAP_2017)
runtable2017[3176] = (10650,23400,100000,"124","250p","1",EMAP_2017)
runtable2017[3353] = (10650,23400,50000,"124","250p","1",EMAP_2017)
runtable2017[3154] = (10650,23400,7600,"124","250p","6",EMAP_2017)
runtable2017[3156] = (10650,23400,5600,"124","250p","6",EMAP_2017)
runtable2017[3157] = (10650,23400,6400,"124","250p","6",EMAP_2017)
runtable2017[3158] = (10650,23400,15200,"124","250p","6",EMAP_2017)
runtable2017[3354] = (10650,23400,50000,"124","250p","6",EMAP_2017)
runtable2017[3160] = (10650,23400,2200,"124","250p","1",EMAP_2017)
runtable2017[3161] = (10650,23400,6000,"124","250p","1",EMAP_2017)
runtable2017[3162] = (10650,23400,30000,"124","250p","1",EMAP_2017)
runtable2017[3355] = (10650,23400,50000,"124","250p","1",EMAP_2017)
runtable2017[3175] = (10650,23400,30000,"124","250p","1",EMAP_2017)
runtable2017[3356] = (10650,23400,50000,"124","250p","1",EMAP_2017)
runtable2017[3178] = (10650,23400,47300,"124","300p","1",EMAP_2017)
runtable2017[3179] = (10650,23400,55000,"124","300p","1",EMAP_2017)
runtable2017[3322] = (10650,23400,100000,"124","300p","1",EMAP_2017)
runtable2017[3177] = (10650,23400,100000,"124","300p","6",EMAP_2017)
runtable2017[3323] = (10650,23400,100000,"124","300p","6",EMAP_2017)
runtable2017[3180] = (10650,23400,30000,"124","300p","1",EMAP_2017)
runtable2017[3324] = (10650,23400,100000,"124","300p","1",EMAP_2017)
runtable2017[3183] = (10650,23400,13000,"124","300p","1",EMAP_2017)
runtable2017[3325] = (10650,23400,100000,"124","300p","1",EMAP_2017)
runtable2017[3326] = (10650,23400,100000,"124","300p","6",EMAP_2017)
runtable2017[3327] = (10650,23400,100000,"124","300p","6",EMAP_2017)
runtable2017[3321] = (10650,23400,50000,"124","350p","6",EMAP_2017)
runtable2017[3271] = (10650,40500,50000,"124","30p","1",EMAP_2017)
runtable2017[3272] = (10650,40500,50000,"124","30p","6",EMAP_2017)
runtable2017[3274] = (10650,40500,50000,"124","50p","6",EMAP_2017)
runtable2017[3277] = (10650,40500,9000,"124","80p","6",EMAP_2017)
runtable2017[3278] = (10650,40500,50000,"124","80p","6",EMAP_2017)
runtable2017[3348] = (10650,40500,50000,"124","100p","6",EMAP_2017)
runtable2017[3346] = (10650,40500,50000,"124","150p","6",EMAP_2017)
runtable2017[3347] = (10650,40500,50000,"124","150p","1",EMAP_2017)
runtable2017[3477] = (10720,40500,100000,"124","150p","6",EMAP_2017)
runtable2017[3319] = (10650,40500,50000,"124","200p","6",EMAP_2017)
runtable2017[3336] = (10650,40500,50000,"124","200p","6",EMAP_2017)
runtable2017[3345] = (10650,40500,50000,"124","250p","6",EMAP_2017)
runtable2017[3317] = (10650,40500,50000,"124","300p","6",EMAP_2017)
runtable2017[3334] = (10650,40500,50000,"124","300p","6",EMAP_2017)
runtable2017[3318] = (10650,40500,50000,"124","300p","1",EMAP_2017)
runtable2017[3335] = (10650,40500,50000,"124","300p","1",EMAP_2017)
runtable2017[3476] = (10720,40500,100000,"124","300p","6",EMAP_2017)
runtable2017[3316] = (10650,40500,50000,"124","350p","6",EMAP_2017)
runtable2017[3333] = (10650,40500,50000,"124","350p","6",EMAP_2017)
runtable2017[3252] = (10650,23400,30000,"124","20e","1",EMAP_2017)
runtable2017[3254] = (10650,23400,30000,"124","20e","1",EMAP_2017)
runtable2017[3253] = (10650,23400,8800,"124","20e","6",EMAP_2017)
runtable2017[3255] = (10650,23400,30000,"124","20e","6",EMAP_2017)
runtable2017[3256] = (10650,23400,30000,"124","20e","1",EMAP_2017)
runtable2017[3257] = (10650,23400,30000,"124","20e","1",EMAP_2017)
runtable2017[3261] = (10650,23400,30000,"124","30e","1",EMAP_2017)
runtable2017[3260] = (10650,23400,50000,"124","30e","6",EMAP_2017)
runtable2017[3259] = (10650,23400,30000,"124","30e","1",EMAP_2017)
runtable2017[3258] = (10650,23400,30000,"124","30e","1",EMAP_2017)
runtable2017[3265] = (10650,23400,30000,"124","80e","1",EMAP_2017)
runtable2017[3264] = (10650,23400,30000,"124","80e","6",EMAP_2017)
runtable2017[3263] = (10650,23400,30000,"124","80e","1",EMAP_2017)
runtable2017[3262] = (10650,23400,30000,"124","80e","1",EMAP_2017)
runtable2017[3269] = (10650,23400,30000,"124","120e","1",EMAP_2017)
runtable2017[3268] = (10650,23400,30000,"124","120e","6",EMAP_2017)
runtable2017[3267] = (10650,23400,30000,"124","120e","1",EMAP_2017)
runtable2017[3266] = (10650,23400,30000,"124","120e","1",EMAP_2017)
runtable2017[3302] = (10650,23400,20000,"124","200200","1",EMAP_2017)
runtable2017[3371] = (10650,23400,5000,"124","200200","1",EMAP_2017)
runtable2017[3372] = (10650,23400,20000,"124","200200","1",EMAP_2017)
runtable2017[3377] = (10650,23400,20000,"124","200200","1",EMAP_2017)
runtable2017[3373] = (10650,23400,20000,"124","200200","6",EMAP_2017)
runtable2017[3376] = (10650,23400,20000,"124","200200","6",EMAP_2017)
runtable2017[3303] = (10650,23400,20000,"124","200200","6",EMAP_2017)
runtable2017[3304] = (10650,23400,5000,"124","200200","1",EMAP_2017)
runtable2017[3290] = (10650,23400,5000,"124","250250","1",EMAP_2017)
runtable2017[3291] = (10650,23400,5000,"14","250250","1",EMAP_2017)
runtable2017[3295] = (10650,23400,2200,"124","250250","1",EMAP_2017)
runtable2017[3297] = (10650,23400,8000,"124","250250","1",EMAP_2017)
runtable2017[3292] = (10650,23400,20000,"124","250250","6",EMAP_2017)
runtable2017[3293] = (10650,23400,20000,"124","250250","1",EMAP_2017)
runtable2017[3294] = (10650,23400,20000,"124","250250","1",EMAP_2017)
runtable2017[3298] = (10650,23400,20000,"124","300300","1",EMAP_2017)
runtable2017[3299] = (10650,23400,40000,"124","300300","6",EMAP_2017)
runtable2017[3300] = (10650,23400,20000,"124","300300","1",EMAP_2017)
runtable2017[3301] = (10650,23400,20000,"124","300300","1",EMAP_2017)
runtable2017[3283] = (10650,40500,26000,"124","20e","1",EMAP_2017)
runtable2017[3282] = (10650,40500,30000,"124","20e","6",EMAP_2017)
runtable2017[3281] = (10650,40500,30000,"124","20e","1",EMAP_2017)
runtable2017[3280] = (10650,40500,30000,"124","20e","1",EMAP_2017)
runtable2017[3341] = (10650,40500,20000,"124","30e","1",EMAP_2017)
runtable2017[3342] = (10650,40500,20000,"124","30e","6",EMAP_2017)
runtable2017[3343] = (10650,40500,20000,"124","30e","1",EMAP_2017)
runtable2017[3344] = (10650,40500,20000,"124","30e","1",EMAP_2017)
runtable2017[3337] = (10650,40500,20000,"124","80e","1",EMAP_2017)
runtable2017[3338] = (10650,40500,20000,"124","80e","6",EMAP_2017)
runtable2017[3339] = (10650,40500,20000,"124","80e","1",EMAP_2017)
runtable2017[3340] = (10650,40500,20000,"124","80e","1",EMAP_2017)
runtable2017[3314] = (10650,40500,20000,"124","200200","1",EMAP_2017)
runtable2017[3374] = (10650,40500,20000,"124","200200","1",EMAP_2017)
runtable2017[3315] = (10650,40500,20000,"124","200200","6",EMAP_2017)
runtable2017[3375] = (10650,40500,20000,"124","200200","6",EMAP_2017)
runtable2017[3288] = (10650,40500,20000,"124","250250","1",EMAP_2017)
runtable2017[3286] = (10650,40500,5000,"14","250250","1",EMAP_2017)
runtable2017[3287] = (10650,40500,5000,"124","250250","1",EMAP_2017)
runtable2017[3289] = (10650,40500,4500,"124","250250","6",EMAP_2017)
runtable2017[3311] = (10650,40500,15000,"124","250250","6",EMAP_2017)
runtable2017[3312] = (10650,40500,20000,"124","250250","1",EMAP_2017)
runtable2017[3313] = (10650,40500,20000,"124","250250","1",EMAP_2017)
runtable2017[3306] = (10650,40500,20000,"124","300300","1",EMAP_2017)
runtable2017[3307] = (10650,40500,40000,"124","300300","6",EMAP_2017)
runtable2017[3308] = (10650,40500,20000,"124","300300","1",EMAP_2017)
runtable2017[3309] = (10650,40500,20000,"124","300300","1",EMAP_2017)
runtable2017[3216] = (11125,62750,100000,"14","150m","1",EMAP_2017)
runtable2017[3366] = (11125,62750,100000,"14","150m","1",EMAP_2017)
runtable2017[3378] = (11095,62750,20000,"14","150m","1",EMAP_2017)
runtable2017[3386] = (11155,62750,20000,"14","150m","1",EMAP_2017)
runtable2017[3387] = (11155,62750,20000,"14","150m","1",EMAP_2017)
runtable2017[3388] = (11170,62750,20000,"14","150m","1",EMAP_2017)
runtable2017[3390] = (11170,62750,100000,"14","150m","1",EMAP_2017)
runtable2017[3391] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3392] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3393] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3394] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3395] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3396] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3397] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3398] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3399] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3400] = (11170,62750,32700,"14","150m","1",EMAP_2017)
runtable2017[3401] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3402] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3403] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3404] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3405] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3406] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3407] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3408] = (11170,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3409] = (11170,62750,20000,"14","150m","1",EMAP_2017)
runtable2017[3410] = (11170,62750,53000,"14","150m","1",EMAP_2017)
runtable2017[3411] = (11230,62750,31000,"14","150m","1",EMAP_2017)
runtable2017[3412] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3413] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3414] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3415] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3416] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3417] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3418] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3419] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3420] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3421] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3422] = (11230,62750,250000,"14","150m","1",EMAP_2017)
runtable2017[3427] = (10650,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3428] = (10650,23400,50000,"124","270p","1",EMAP_2017)
runtable2017[3429] = (10650,23400,100000,"124","250p","1",EMAP_2017)
runtable2017[3430] = (10650,23400,50000,"124","250p","6",EMAP_2017)
runtable2017[3431] = (10650,23400,50000,"124","150p","1",EMAP_2017)
runtable2017[3432] = (10650,23400,25000,"124","200e","1",EMAP_2017)
runtable2017[3461] = (9500,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3462] = (10000,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3463] = (10350,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3464] = (10570,23400,30000,"124","150m","1",EMAP_2017)
runtable2017[3460] = (10650,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3465] = (10650,23400,20000,"124","150m","1",EMAP_2017)
runtable2017[3466] = (10730,23400,30000,"124","150m","1",EMAP_2017)
runtable2017[3467] = (10975,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3468] = (11075,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3469] = (11350,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3470] = (11625,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3471] = (11885,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3472] = (12160,23400,10000,"124","150m","1",EMAP_2017)
runtable2017[3481] = (10720,23400,100000,"124","300p","1",EMAP_2017)
runtable2017[3482] = (10720,23400,100000,"124","300p","6",EMAP_2017)
runtable2017[3487] = (10720,23400,5100,"124","300p","6",EMAP_2017)
runtable2017[3488] = (10720,23400,93700,"124","300p","6",EMAP_2017)
runtable2017[3489] = (10720,23400,19500,"124","300p","6",EMAP_2017)
runtable2017[3490] = (10720,23400,2600,"124","300p","6",EMAP_2017)
runtable2017[3493] = (10720,23400,190000,"124","300p","6",EMAP_2017)
runtable2017[3494] = (10720,23400,37900,"124","300p","6",EMAP_2017)
runtable2017[3436] = (10650,23400,50000,"124","250p","1",EMAP_2017)
runtable2017[3483] = (10720,23400,27000,"124","250p","1",EMAP_2017)
runtable2017[3484] = (10720,23400,75000,"124","250p","1",EMAP_2017)
runtable2017[3437] = (10650,23400,50000,"124","250p","6",EMAP_2017)
runtable2017[3441] = (10650,23400,100000,"124","200p","1",EMAP_2017)
runtable2017[3442] = (10650,23400,22000,"124","200p","6",EMAP_2017)
runtable2017[3443] = (10650,23400,100000,"124","200p","6",EMAP_2017)
runtable2017[3439] = (10650,23400,100000,"124","150p","1",EMAP_2017)
runtable2017[3440] = (10650,23400,100000,"124","150p","6",EMAP_2017)
runtable2017[3491] = (10720,23400,200000,"124","150p","6",EMAP_2017)
runtable2017[3495] = (10720,23400,22100,"124","150p","6",EMAP_2017)
runtable2017[3496] = (10720,23400,86200,"124","150p","6",EMAP_2017)
runtable2017[3445] = (10650,23400,100000,"124","100p","1",EMAP_2017)
runtable2017[3446] = (10650,23400,100000,"124","100p","6",EMAP_2017)
runtable2017[3480] = (10720,23400,20000,"124","80p","6",EMAP_2017)
runtable2017[3479] = (10720,23400,20000,"124","50p","6",EMAP_2017)
runtable2017[3492] = (10720,23400,50000,"124","50p","6",EMAP_2017)
runtable2017[3447] = (10650,23400,40000,"124","200e","1",EMAP_2017)
runtable2017[3458] = (10650,23400,40000,"124","200e","1",EMAP_2017)
runtable2017[3448] = (10650,23400,40000,"124","200e","6",EMAP_2017)
runtable2017[3459] = (10650,23400,40000,"124","200e","6",EMAP_2017)
runtable2017[3449] = (10650,23400,12000,"124","120e","1",EMAP_2017)
runtable2017[3450] = (10650,23400,30000,"124","120e","1",EMAP_2017)
runtable2017[3451] = (10650,23400,30000,"124","120e","6",EMAP_2017)
runtable2017[3452] = (10650,23400,30000,"124","80e","1",EMAP_2017)
runtable2017[3453] = (10650,23400,30000,"124","80e","6",EMAP_2017)
runtable2017[3454] = (10650,23400,30000,"124","30e","1",EMAP_2017)
runtable2017[3455] = (10650,23400,30000,"124","30e","6",EMAP_2017)

######################################
# Put all runs together
###################################### 

runTable_all = {}

for dictionary in [runTable_pions_ODU12, runTable_pions_Aug15,
                   runTable_Aug15, runTable_Aug14, runTable_Aug13,
                   runTable_Ph2_Aug14, runTable_Ph2_Aug15,
		   runTable_muons_specialODU, runTable_pions_specialODU,
		   runTable_muons_specialODU_forPhase2,runtable2017]:
        runTable_all.update(dictionary)

def getEmapFromRun(run):
        if run in runTable_all: 
            emapFile = runTable_all[run][6]
        else:
            if run <= 8823:
               emapFile = EMAP_default
            else:
               emapFile = EMAP_specialODU
        return emapFile


shunt_conversion = {"1" : 1.,
		    "1/5" : 1./6, # This is NOT a typo :-)
		    "1/11.5" : 1./11.5,
		    "1/3": 1./3,
		    "1/9": 1./9,
                    "6" : 1./6}

def getShuntFromRun(run):
	shunt = 1.
        if run in runTable_all: 
            shunt_string = runTable_all[run][5]
	    shunt = shunt_conversion[shunt_string]
        return shunt

