ASCIIDict = dict()
keyvalues=0
for i in range(97,123):
    keyvalues=keyvalues+1
    ASCIIDict[chr(i)] = str(i)
print(ASCIIDict)
