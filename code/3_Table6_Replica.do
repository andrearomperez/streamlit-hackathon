clear
use "/Users/fernandaamartel/Downloads/NEW7080.dta", clear
ssc install outreg2

*For Table 6
keep if COHORT > 4000

eststo clear

reg  LWKLYWGE EDUC  YR0-YR8 
eststo model1
outreg2 using "table6.doc", replace

ivregress 2sls LWKLYWGE YR0-YR8 (EDUC = QTR1YR0-QTR1YR9 QTR2YR0-QTR2YR9 QTR3YR0-QTR3YR9 YR0-YR8)
eststo model2
outreg2 using "table6.doc", append

reg  LWKLYWGE EDUC  YR0-YR8 AGEQ AGEQSQ 
eststo model3
outreg2 using "table6.doc", append

ivregress 2sls LWKLYWGE YR0-YR8 AGEQ AGEQSQ (EDUC = QTR1YR0-QTR1YR9 QTR2YR0-QTR2YR9 QTR3YR0-QTR3YR9 YR0-YR8)
eststo model4
outreg2 using "table6.doc", append

reg  LWKLYWGE EDUC  RACE MARRIED SMSA NEWENG MIDATL ENOCENT WNOCENT SOATL ESOCENT WSOCENT MT YR0-YR8  
eststo model5
outreg2 using "table6.doc", append

ivregress 2sls LWKLYWGE YR0-YR8 RACE MARRIED SMSA NEWENG MIDATL ENOCENT WNOCENT SOATL ESOCENT WSOCENT MT  (EDUC = QTR1YR0-QTR1YR9 QTR2YR0-QTR2YR9 QTR3YR0-QTR3YR9 YR0-YR8)
eststo model6
outreg2 using "table6.doc", append

reg  LWKLYWGE EDUC  RACE MARRIED SMSA NEWENG MIDATL ENOCENT WNOCENT SOATL ESOCENT WSOCENT MT YR0-YR8 AGEQ AGEQSQ 
eststo model7
outreg2 using "table6.doc", append

ivregress 2sls LWKLYWGE YR0-YR8 RACE MARRIED SMSA NEWENG MIDATL ENOCENT WNOCENT SOATL ESOCENT WSOCENT MT AGEQ AGEQSQ (EDUC = QTR1YR0-QTR1YR9 QTR2YR0-QTR2YR9 QTR3YR0-QTR3YR9 YR0-YR8)
eststo model8
outreg2 using "table6.doc", append


