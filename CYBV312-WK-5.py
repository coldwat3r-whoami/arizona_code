"""
Nicholas Desantiago
CYBV 312
September 2024
Week 5 Assignment
"""
import itertools
import hashlib
import pickle
from prettytable import PrettyTable

rainbowTable = {}
myTable = PrettyTable(["Rainbows"])

print("Create Simple Rainbow Table")
for variations in range(4,8):
    for pwTuple in itertools.product("abc123&", repeat=variations):
        pw = ""
        md5Hash = hashlib.md5()
        for eachChr in pwTuple:
            pw = pw+"".join(eachChr)
        pw = bytes(pw, 'ascii')
        md5Hash.update(pw)
        md5Digest = md5Hash.hexdigest()
        rainbowTable[md5Digest] = pw

# Create and open a Pickle file    
pickleFileWrite = open('./pickledRainbow.db', 'wb')
print("Serializing a list:")

# Dumping the rainbow table data to Pickle file and closing
pickle.dump(rainbowTable, pickleFileWrite)                      
pickleFileWrite.close()

# Getting the first and last 5 items from rainbow table    
firstFive = list(rainbowTable.items())[:5]
lastFive = list(rainbowTable.items())[-5:]

# Formatting into prettytable
for eachRainbow in firstFive:
    myTable.add_row([eachRainbow])

for eachRainbow in lastFive:
    myTable.add_row([eachRainbow])

print("Rainbow Size: ", len(rainbowTable), "\n")
print(myTable)
    
            
            
            