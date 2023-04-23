import numpy as np
import csv

# Podatke sem našla na spletu (priloženi v drugi mapi). 

# id,ime,izvajalec,popularnost,število pesmi

file1 = open("albumi_vsi2.csv")
file2 = open("artistv_vsi.csv")
file3 = open("pesmi_vse.csv")
file4 = open("releases.csv")

csvreader1 = csv.reader(file1)
csvreader2 = csv.reader(file2)
csvreader3 = csv.reader(file3)
csvreader4 = csv.reader(file4)

data2 = []
for line in csvreader2:
    if line[0] == "id":
        pass
    elif int(line[2] ) >= 90:
        liner = [s.replace("singer", "pevec/pevka") for s in line]
        liner1 = [s.replace("band", "skupina") for s in liner]
        liner2 = [s.replace("music", "glasba") for s in liner1]

        data2.append(liner2)

artist_keys = [str(i) for i in np.array(data2)[:,0]]
filew2 = open("izvajalci_90.csv","w")

for i in data2:
    print(i[2])
    filew2.write(f"{i[0]}, {i[1]}, {str(i[2])}, {i[3]}\n") #, {i[1]}, {str(i[2])}, {i[3]}

# To check which albums belong to artists

data1 = []
for line in csvreader1:
    key = str(line[2][2:24])
    if key in artist_keys:
        data1.append(line)

filew1 = open("albumi_90..csv","w")
for i in data1:
    if len(i) == 5: # Manually correct names of albums that include commas
        filew1.write(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}\n") #, {i[1]}, {str(i[2])}, {i[3]}

# id, ime pesmi, billboard, id-izvajalec, popularnost, vrsta projekta
data3 = []
for line in csvreader3:
    liner = [s.replace("Solo", "samostojen projekt") for s in line]
    liner1 = [s.replace("Collaboration", "sodelovanje na projektu") for s in liner]

    key = str(line[3][2:24])
    if key in artist_keys:
        data3.append(liner1)

filew3 = open("pesmi_90.csv","w")
for i in data3:
    filew3.write(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}, {i[4]}, {i[5]}\n") #, {i[1]}, {str(i[2])}, {i[3]}


# id- izvajalca, id-albuma, datum izzida, določena natančnost
album_keys = [str(i) for i in np.array(data1)[:,0]]
data4 = []
for line in csvreader4:
    liner = line[0].split("\t")
    liner1 = [s.replace("year", "leto") for s in liner]
    liner2 = [s.replace("day", "dan") for s in liner1]

    #nov = liner1.split("\n")
    key = line[0].split("\t")[1]

    print(liner2)
    #key = str(str(liner1)[26:48])
    if key in album_keys:
        data4.append(liner2)

filew4 = open("izdaja_90l.csv","w")
for i in data4:
    filew4.write(f"{i[0]}, {i[1]}, {i[2]}, {i[3]}\n") #, {i[1]}, {str(i[2])}, {i[3]}

