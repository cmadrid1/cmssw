import FWCore.ParameterSet.Config as cms

HcalTimeSlewEP = cms.ESSource("HcalTimeSlewEP",
    appendToDataLabel = cms.string("HBHE"),                              
    # For method2/simulation
    timeSlewParametersM2 = cms.VPSet(
        cms.PSet(#Slow    
            tzero = cms.double(23.960177), slope = cms.double(-3.178648), tmax = cms.double(16.00)),
        cms.PSet(#Medium
            tzero = cms.double(13.307784), slope = cms.double(-1.556668), tmax = cms.double(10.00)),
        cms.PSet(#Fast
            tzero = cms.double(9.109694),  slope = cms.double(-1.075824), tmax = cms.double(6.25))
    ),
    # For method3                          
    timeSlewParametersM3 = cms.VPSet(        
        #cms.PSet(#Data
        #    cap = cms.double(6.0), tspar0 = cms.double(15.5),    tspar1 = cms.double(-3.2),     tspar2 = cms.double(32.0), tspar0_siPM = cms.double(0.0), tspar1_siPM = cms.double(0.0), tspar2_siPM = cms.double(0.0)),
        #cms.PSet(#MC
        #    cap = cms.double(6.0), tspar0 = cms.double(12.2999), tspar1 = cms.double(-2.19142), tspar2 = cms.double(0.0),  tspar0_siPM = cms.double(0.0), tspar1_siPM = cms.double(0.0), tspar2_siPM = cms.double(0.0)),
        cms.PSet(#HB
            cap = cms.double(6.0), tspar0 = cms.double(12.2999), tspar1 = cms.double(-2.19142), tspar2 = cms.double(0.0),  tspar0_siPM = cms.double(0.0), tspar1_siPM = cms.double(0.0), tspar2_siPM = cms.double(0.0)),
        cms.PSet(#BE (ieta 16 and 17)
            cap = cms.double(6.0), tspar0 = cms.double(12.2999), tspar1 = cms.double(-2.19142), tspar2 = cms.double(0.0),  tspar0_siPM = cms.double(0.0), tspar1_siPM = cms.double(0.0), tspar2_siPM = cms.double(0.0)),
        cms.PSet(#HE
            cap = cms.double(6.0), tspar0 = cms.double(12.2999), tspar1 = cms.double(-2.19142), tspar2 = cms.double(0.0),  tspar0_siPM = cms.double(0.0), tspar1_siPM = cms.double(0.0), tspar2_siPM = cms.double(0.0))
    )
)

from Configuration.Eras.Modifier_run2_HE_2018_cff import run2_HE_2018
#HBHE2018  -  Medium
run2_HE_2018.toModify(
    HcalTimeSlewEP, timeSlewParametersM2 = {
        1: dict(tzero = cms.double(11.977461), slope = cms.double(-1.5610227),tmax = cms.double(10.00))})
