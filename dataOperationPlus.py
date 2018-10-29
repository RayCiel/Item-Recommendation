import csv

def readTrain(input_trainpath):
    train = []
    with open(input_trainpath, "r") as in_traincsv:
        tmp = csv.reader(in_traincsv, delimiter = '\t')
        for line in tmp:
            train.append(line)
    return train
    '''    column1 = [row for row in tmp]
    user_column = [i[1] for i in column1]
    item_column = [i[2] for i in column1]
    score_column = [i[3] for i in column1]
    day_column = [i[4] for i in column1]
    time_column = [i[5] for i in column1]
    user_id = []
    item_id = []
    score = []
    day = []
    time = []
    for i in range(len(user_column)):
        if i == 0:
            continue
        user_id.append(user_column[i])
        item_id.append(user_column[i])
        score.append(score_column[i])
        day.append(day_column[i])
        time.append(time_column[i])
    train = [user_id, item_id, score, day, time]
    return train'''

def readTest(input_path):
    with open(input_path, "r") as in_csv:
        tmp = csv.reader(in_csv, delimiter = '\t')
        test = []
        for line in tmp:
            test.append(line)
    return test
    '''        column1 = [row for row in tmp]
        user_column = [i[1] for i in column1]
        item_column = [i[2] for i in column1]
        day_column = [i[3] for i in column1]
        time_column = [i[4] for i in column1]
        user_id = []
        item_id = []
        day = []
        time = []
        for i in range(len(user_column)):
            if i == 0:
                continue
            user_id.append(user_column[i])
            item_id.append(user_column[i])
            day.append(day_column[i])
            time.append(time_column[i])
        test = [user_id, item_id, day, time]
        return test'''

def readFeature(input_path):
    featureList = []
    with open(input_path, "r") as in_txt:
        tmp = in_txt.readlines()
        for line in tmp:
            #curLine
            line = line.replace("\t", " ")
            curLine = line.split(" ")
            featureList.append(curLine)
            #print(curLine[0] + " "+curLine[1] + " " + curLine)
            #print(line[0] + " "+line[1])

    #    featureList = in_txt.read().split('\t')
    #print(featureList[0])
    #print(featureList[1])
    return featureList

def trainPrepare(trainList, featureList, output_path):
    fout_train = open(output_path, "w")
    user_max = 0
    item_max = 0
    day_max = 0
    time_max = 0
    feature1_max = 0
    feature2_max = 0
    addfeature1_max = 0
    addfeature2_max = 0
    addfeature3_max = 0
    addfeature4_max = 0
    for line in trainList:
        #print(line)
        user_max = max(user_max, int(line[0]))
        item_max = max(item_max, int(line[1]))
        day_max = max(day_max, int(line[3]))
        time_max = max(time_max, int(line[4]))
    for line in featureList:
        feature1_max = max(feature1_max, int(line[1]))
        feature2_max = max(feature2_max, int(line[2]))
        addfeature1_max = max(addfeature1_max, int(line[3]))
        addfeature2_max = max(addfeature2_max, int(line[4]))
        addfeature3_max = max(addfeature3_max, int(line[5]))
        addfeature4_max = max(addfeature4_max, int(line[6]))
    n1 = user_max
    n2 = n1 + item_max
    n3 = n2 +feature1_max
    n4 = n3 + feature2_max
    n5 = n4 + addfeature1_max
    n6 = n5 + addfeature2_max
    n7 = n6 + addfeature3_max
    n8 = n7 + addfeature4_max
    n9 = n8 + day_max
    n10 = n9 + time_max
    for i in range(len(trainList)):
        if i % 100 == 0:
            print("Done.." + str(i))
        #print(str(i) +" " + str(len(trainList))+ " " + str(trainList[i]))
        item = int(trainList[i][1])
        fout_train.write(str(trainList[i][2]) + " "
        + str(trainList[i][0]) + ":" + str(1) + " "
        + str(int(trainList[i][1]) + n1) + ":" + str(1) + " ")
        if int(featureList[item][1]) > -1:
            fout_train.write(str(int(featureList[item][1]) + n2) + ":" + str(1) + " ")
        if int(featureList[item][2]) > -1:
            fout_train.write(str(int(featureList[item][2]) + n3) + ":" + str(1) + " ")
        if int(featureList[item][3]) > -1:
            fout_train.write(str(int(featureList[item][3]) + n4) + ":" + str(1) + " ")
        if int(featureList[item][4]) > -1:
            fout_train.write(str(int(featureList[item][4]) + n5) + ":" + str(1) + " ")
        if int(featureList[item][5]) > -1:
            fout_train.write(str(int(featureList[item][5]) + n6) + ":" + str(1) + " ")
        if int(featureList[item][6]) > -1:
            fout_train.write(str(int(featureList[item][6]) + n7) + ":" + str(1) + " ")
        fout_train.write(str(int(trainList[i][3]) + n8) + ":" + str(1) + " "
        + str(int(trainList[i][4]) + n9) + ":" + str(1) + '\n')
    fout_train.close()

def testPrepare(testList, featureList, output_path):
    fout_test = open(output_path, "w")
    user_max = 0
    item_max = 0
    day_max = 0
    time_max = 0
    feature1_max = 0
    feature2_max = 0
    addfeature1_max = 0
    addfeature2_max = 0
    addfeature3_max = 0
    addfeature4_max = 0
    for line in testList:
        user_max = max(user_max, int(line[0]))
        item_max = max(item_max, int(line[1]))
        day_max = max(day_max, int(line[2]))
        time_max = max(time_max, int(line[3]))
    for line in featureList:
        feature1_max = max(feature1_max, int(line[1]))
        feature2_max = max(feature2_max, int(line[2]))
        addfeature1_max = max(addfeature1_max, int(line[3]))
        addfeature2_max = max(addfeature2_max, int(line[4]))
        addfeature3_max = max(addfeature3_max, int(line[5]))
        addfeature4_max = max(addfeature4_max, int(line[6]))
    n1 = user_max
    n2 = n1 + item_max
    n3 = n2 +feature1_max
    n4 = n3 + feature2_max
    n5 = n4 + addfeature1_max
    n6 = n5 + addfeature2_max
    n7 = n6 + addfeature3_max
    n8 = n7 + addfeature4_max
    n9 = n8 + day_max
    n10 = n9 + time_max
    for i in range(len(testList)):
        item = int(testList[i][1])
        fout_test.write("0" + " " +
        str(testList[i][0]) + ":" + str(1) + " "
        + str(int(testList[i][1]) + n1) + ":" + str(1) + " ")
        if int(featureList[item][1]) > -1:
            fout_test.write(str(int(featureList[item][1]) + n2) + ":" + str(1) + " ")
        if int(featureList[item][2]) > -1:
            fout_test.write(str(int(featureList[item][2]) + n3) + ":" + str(1) + " ")
        if int(featureList[item][3]) > -1:
            fout_test.write(str(int(featureList[item][3]) + n4) + ":" + str(1) + " ")
        if int(featureList[item][4]) > -1:
            fout_test.write(str(int(featureList[item][4]) + n5) + ":" + str(1) + " ")
        if int(featureList[item][5]) > -1:
            fout_test.write(str(int(featureList[item][5]) + n6) + ":" + str(1) + " ")
        if int(featureList[item][6]) > -1:
            fout_test.write(str(int(featureList[item][6]) + n7) + ":" + str(1) + " ")
        fout_test.write(str(int(testList[i][2]) + n8) + ":" + str(1) + " "
        + str(int(testList[i][3]) + n9) + ":" + str(1) + '\n')
    fout_test.close()

train_path = "train.tsv"
test_path = "test.tsv"
feature_path = "feature.txt"
valid_path = "valid.tsv"
out_valid = "out_valid_plus.txt"
out_train = "out_train_plus.txt"
out_test = "out_test_plus.txt"
trainList = readTrain(train_path)
print("trainList Done..")
validList = readTrain(valid_path)
print("validList Done..")
testList = readTest(test_path)
print("testList Done..")
featureList = readFeature(feature_path)
print("featureList Done..")
trainPrepare(trainList, featureList, out_train)
print("train Prepared..")
trainPrepare(validList, featureList, out_valid)
print("valid Prepared..")
testPrepare(testList, featureList, out_test)
print("test Prepared..")
