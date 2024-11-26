import csv
import time

#range of data is column 146 to 245
def echo():
    data = []

    with open ("lhc data.csv", "r", encoding='utf-8-sig') as f:
        data_reader = csv.reader(f)
        whole_header = next(data_reader)
        #header = [whole_header[0]] + whole_header[146:246]
        counter = 0
        echodata = [""]*34
        rightcathdata = [""]*16
        nucstressdata = [""]*12
        stressdata = [""]*18
        data = []

        for row in data_reader:
              if row[1] == "":
                data.append(row)
        '''
        for row in data_reader:
            if row[1] == "Baseline Echo":
                print(echodata[5])
                if echodata[4] == "":
                    echodata = row[3:37]
                elif row[8]:
                    if time.strptime(row[8], "%m/%d/%Y") > time.strptime(echodata[5], "%m/%d/%Y"):
                        echodata = row[3:37]
           
            if row[1] == "Right Heart Cath":
                if rightcathdata[1] == "":
                    rightcathdata = row[232:216]
                elif row[201]:
                    if time.strptime(row[201], "%m/%d/%Y") > time.strptime(rightcathdata[1], "%m/%d/%Y"):
                        rightcathdata = row[232:216]

            if row[1] == "Stress Nuclear":
                if nucstressdata[2] == "":
                    nucstressdata = row[216:228]
                elif row[218]:
                    if time.strptime(row[218], "%m/%d/%Y") > time.strptime(nucstressdata[2], "%m/%d/%Y"):
                        nucstressdata = row[216:228]

            if row[1] == "Stress Echo":
                if stressdata[3] == "":
                    stressdata = row[228:246]
                elif row[231]:
                    if time.strptime(row[231], "%m/%d/%Y") > time.strptime(stressdata[3], "%m/%d/%Y"):
                        stressdata = row[228:246]
            
            if row[0] == "522" and row[1] == "Stress Echo":
                final = [int(row[0])-1] + echodata + rightcathdata + nucstressdata + stressdata
                data.append(final)
                

            if not row[2] and counter != 0:
                #final = [int(row[0])-1] + echodata + rightcathdata + nucstressdata + stressdata
                final = [int(row[0])-1] + echodata 
                echodata = [""]*34
                rightcathdata = [""]*16
                nucstressdata = [""]*12
                stressdata = [""]*18

                data.append(final)
            counter += 1
            '''

    with open('processed lhc data.csv', 'w', newline='') as g:
        writer = csv.writer(g)
        writer.writerow(whole_header)
        for row in data:
            writer.writerows([row])



echo()