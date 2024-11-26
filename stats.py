import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import csv
import statistics

# Create a dataset
data = []
final = []

counter = 0

with open("importance_h_hf.csv", "r", encoding='utf-8-sig') as f:
        data_reader = csv.reader(f)
        for row in data_reader:
            if row[0]:
                if counter < 9:
                    data.append(float(row[3]))
                    counter+=1

avg = sum(data)/len(data)
std = statistics.pstdev(data)

for p in data:
     z = (p-avg)/std
     final.append(z)


nfinal = np.reshape(final,(3,3))

all_mortality= ([["*Diastolic BP\n(p<0.001)", "*BNP\n(p=0.011)", "*Hemoglobin\nA1c\n(p=0.007)"], ["*Vitamin D\n(p=0.003)", "Days from\nLHC to Transplant\n(p=0.131)", "Urine Output\nVolume\n(p=0.107)"], 
                 ["*Left Ventricular\nEjection Fraction\n(p<0.001)", "*Family History\nof CKD\n(p<0.001)", "*History of\nDrug-treated\nHypotension\n(p=0.009)"]])

cv_death= ([["*BNP\n(p<0.001)", "Days from\nLHC to Transplant\n(p=0.157)", "*Diastolic BP\n(p=0.001)"], ["*Aspirin Use\n(p=0.011)", "*Obstructive\nSleep Apnea\n(p=0.027)", "*Proximal LAD\n Stenosis %\n(p=0.006)"], 
            ["*Systolic BP\n(p=0.016)", "*Left Atrial\nVolume\n(p=0.028)", "*Abnormal LHC\nFindings\n(p<0.001)"]])

hf= ([["*BNP\n(p<0.001)", "*Diastolic\nBP\n(p<0.001)", "*HDL-C\n(p=0.027)"], ["*PTH\n(p<0.001)", "*Resting\nHeart Rate\n(p<0.001)", "Family History\nof CKD\n(p=0.050)"], 
      ["*Days from\nPretransplant\nEvaluation to\nTransplant\n(p=0.007)", "*Vitamin D\n(p<0.001)", "*Triglycerides\n(p<0.001)"]])

mi= ([["*BNP\n(p=0.010)", "*Systolic BP\n(0.021)", "Triglycerides\n(p=0.069)"], ["*Total Cholesterol\n(p<0.001)", "*LDL-C\n(p<0.001)", "*Aspirin Use\n(p=0.009)"], 
      ["Diastolic BP\n(p=0.287)", "Diltiazem Use\n(p=0.097)", "*No ACEi or\nARB Use\n(p=0.002)"]])

arrhythmia= ([["Furosemide Use", "Pre HDL-C", "Wall motion abnormalities"], ["BMI", "LA min 4 chamber area", "Distal LCx Stenosis %"], ["Carvedilol Use", "Mid LCx Stenosis %", "Pre Vitamin D"]])
angina= ([["Aspirin Use", "Target HR on Stress Test", "RCA Calcium Score"], ["LM Calcium Score", "No CCB Use", "LA max 2 chamber length"], ["FH of CKD", "Obstructive CAD", "Proximal LCx Stenosis %"]])
revasc= ([["Nitrates", "BNP", "Pre PTH"], ["LAD Calcium Score", "Distal RCA Stenosis %", "Pre LDL-C"], ["LCX Calcium Score", "Age", "Apixaban Use"]])
stroke= ([["BNP", "Days until Transplant", "BMI"], ["Days from Echo to Transplant", "Urine Output", "Aspirin Use"], ["Diastolic BP", "No ACEi or ARB Use", "Type of Dialysis Access"]])

labels = np.array(hf)
# Default heatmap
plt.subplots(figsize=(10,8))
plt.title("Hospitalization for Heart Failure", fontsize = 25)
p1 = sns.heatmap(nfinal, annot=labels, annot_kws={"size": 16}, xticklabels=False, yticklabels=False, fmt = '', cmap='Blues_r')
plt.show()