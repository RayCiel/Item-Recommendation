import csv

input_csv2 = "output-ave4.csv"
input_csv1 = "lib-1.1.20-460.csv"
fin_csv1 = open(input_csv1, "r")
fin_csv2 = open(input_csv2, "r")
#fin_csv3 = open(input_csv3, "r")
fout_csv = open("output-ave5.csv", "w")
csv1 = csv.reader(fin_csv1)
csv2 = csv.reader(fin_csv2)
#csv3 = csv.reader(fin_csv3)
tmp1 = []
tmp2 = []
#tmp3 = []
for line in csv1:
    #fout_csv.write(line[0] + "," + (str((float(line[1]) + float(csv2[i][1]))/2)) + '\n')
    tmp1.append(line)
for line in csv2:
    tmp2.append(line)
#for line in csv3:
#    tmp3.append(line)
fout_csv.write("uid#iid" + "," + "pred" + '\n')
#print(len(tmp3))
for i in range(1, len(tmp1)):
    fout_csv.write(tmp1[i][0] + "," + (str((float(tmp1[i][1]) + float(tmp2[i][1])) / 2)) + '\n')

fout_csv.close()
