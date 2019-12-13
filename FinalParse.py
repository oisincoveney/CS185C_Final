# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 16:57:45 2019

@author: Benjamin
"""
import argparse
import numpy as np
from sklearn.decomposition import PCA
from sklearn import svm
import os


parser = argparse.ArgumentParser()
parser.add_argument("--n", "-n", help="Number of components for PCA", type=int, default=-1)
args = parser.parse_args()

listOfTime = []
normTime = []
totalList = []
label = []
challengeList = []

ChallengeLabel=[]


challengeDateDir = r"C:\Users\rooke\Projects\CS185C_Final\data\Challenge"

DatesOnlyFile = r"C:\Users\rooke\Projects\CS185C_Final\data\DatesOnly.txt"

#This checks the Date labels
DatesOnly =[]
with open(DatesOnlyFile) as fp:
    for count,line in enumerate(fp):
        x = float(line)
        DatesOnly.append(x)

FinalLabels =[]
for time in DatesOnly:
    int_time = int(time)
    if (time<=157585800000):
        FinalLabels.append(-1) 
    else:
        FinalLabels.append(1)
#
        
        

#Process Dates since we believe they indicate the sample label
for file in os.listdir(challengeDateDir):
    filePath = os.path.join(challengeDateDir,file)
    modificationTime = os.path.getmtime(filePath)
    print(modificationTime)
    listOfTime.append(modificationTime)
    
    
for time in listOfTime:
    int_time = int(time)
    if (time<1575858000):
        normTime.append(-1) 
    else:
        normTime.append(1)
print("Times turned to labels in Name order")
print(normTime)

#for each file, we convert to an array of floats and add it to an array
TrainSet1 = r"C:\Users\rooke\Projects\CS185C_Final\data\Renos800.txt"
TrainSet2 = r"C:\Users\rooke\Projects\CS185C_Final\data\CeeInject800.txt"
test = r"C:\Users\rooke\Projects\CS185C_Final\data\CeeInjectTest.txt"

outputFile = r"C:\Users\rooke\Projects\CS185C_Final\data\ChallengeStatToOrder.txt"


#Renos
with open(TrainSet1) as fp:
    for count, line in enumerate(fp):
        line = line.strip('[')
        line = line.replace(']','')
        result = [x.strip() for x in line.split(',')]
        x = np.asarray(result)
        x = x.astype(float)
        totalList.append(x)
        label.append(-1)

#CeeInject
with open(TrainSet2) as fp:
    for count, line in enumerate(fp):
        line = line.strip('[')
        line = line.replace(']','')
        result = [x.strip() for x in line.split(',')]
        x = np.asarray(result)
        x = x.astype(float)
        totalList.append(x)
        label.append(1)

#TestDataSet
with open(test) as fp:
    for count, line in enumerate(fp):
        line = line.strip('[')
        line = line.replace(']','')
        result = [x.strip() for x in line.split(',')]
        x = np.asarray(result)
        x = x.astype(float)
        challengeList.append(x)


# PCA
if args.n >= 0:
    pca = PCA(n_components=args.n)
    pca.fit(totalList)
    totalList = pca.transform(totalList)
    challengeList = pca.transform(challengeList)

#SVM calculations
clf = svm.SVC(gamma = 'auto',kernel = 'rbf',C=2)
clf.fit(totalList,label)
output = clf.predict(challengeList)
output = output.astype(int)
print("SVM output")
print(output)
count = 0
count2 = 0

#check differences. For training data, we should ideally end up 100/0 in some way
#for challenge, ideally show a 100 split
for v in output:
   if(v <0):
       count+=1
   else:
        count2+=1
print("Renos",count)
print("CeeInject",count2)


FinalOutput =[]

print()
print("Cheet Label output")
print(FinalLabels)

correct=0
for out, final in zip(output, FinalLabels):
    if(out==final):
        correct+=1
print()
print("Correct values checked against Date")
print(correct)
print()



Names = []
temp = []
with open(outputFile) as fp:
    temp = fp.readlines()
    
for line in temp:
    line.replace("\n"," ")
    Names.append(line)

FinalResult = []
for out, name in zip(output,Names):
    if(out<0):
        n = name.replace("\n"," ")+"R"
    else:
         n = name.replace("\n"," ")+"C"
    FinalResult.append(n)

#print(FinalResult)

#for i in range(100):
    #print(FinalResult[i])