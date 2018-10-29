import csv

inputlib_path = "out_lib-1.1.20-460.txt"
inputtsv_path = "test.tsv"
output_path = "lib-1.1.20-460.csv"
fin_txt = open(inputlib_path, "r")
fin_tsv = open(inputtsv_path, "r")
fout_csv = open(output_path, "w")
txt = fin_txt.readlines()
tsv = csv.reader(fin_tsv, delimiter = '\t')
tmp1 = []
tmp2 = []
for line in txt:
    line = line.split("\n")
    tmp1.append(line)
for line in tsv:
    tmp2.append(line)
fout_csv.write("uid#iid" + "," + "pred" + '\n')
for i in range(len(tmp1)):
    #print(str(tmp1[0]) + " " + str(tmp2[0]))
    #print(str(i) + " " + str(len(tmp1)) + " " + str(len(tmp2)) )
    fout_csv.write(str(tmp2[i][0]) + "#" + str(tmp2[i][1]) + "," + str(tmp1[i][0]) + '\n')
fin_tsv.close()
fin_txt.close()
fout_csv.close()
