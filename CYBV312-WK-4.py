'''
Script:  Week 4 Scripting Assignment
Author:  Nicholas Desantiago
Date:    September 2024
Version: 1.5
Purpose: File contents and chunking
 
'''

''' IMPORT STANDARD LIBRARIES '''
import sys
import os
import re
import time


''' IMPORT 3RD PARTY LIBRARIES '''
from prettytable import PrettyTable

''' DEFINE PSEUDO CONSTANTS '''


''' LOCAL FUNCTIONS '''


''' LOCAL CLASSES '''


''' MAIN ENTRY POINT '''

try:
    
    scanFile = input("Please enter filename to process: ")
    chunkSize = int(input("What size chunks? "))
    myTable = PrettyTable(["Occurs", "URL"])
    myTable.title = 'Sorted URL Results' # found this here: "https://stackoverflow.com/questions/35321722/python-prettytable-add-title-above-the-tables-header"
    urlPattern = re.compile(b'\w+:\/\/[\w@][\w.:@]+\/?[\w\.?=%&=\-@/$,]*')
    wordDictionary = {}

        
    if os.path.isfile(scanFile):  # Verify file is real
        fileSize = os.path.getsize(scanFile)
        # Display details of file 
        print("\nProcessing file:    ", scanFile)
        print("Total FileSize:    ", "{:,}".format(fileSize))
        print("in chunks of:      ", "{:,}".format(chunkSize), "Bytes\n")
    
        # Open and Loop through the file by chunk
        bytesProcessed = 0
        chunkCnt = 0
        cnt = 0
        
        with open(scanFile, 'rb') as targetFile:
            while True:
                fileChunk = targetFile.read(chunkSize)
                urlMatches = urlPattern.findall(fileChunk)
                
                for eachWord in urlMatches:
                    try:
                        cnt = wordDictionary[eachWord]
                        cnt += 1
                        wordDictionary[eachWord] = cnt
                    except:
                        wordDictionary[eachWord] = 1

                bytesProcessed += len(fileChunk)
                
                if fileChunk:  # if we still have data
                    chunkCnt += 1
                                           
                else:
                    # File has been processed
                    print("\nProcessed:", "{:,}".format(bytesProcessed))
                    for name, value in wordDictionary.items():
                        myTable.add_row([value, name])              
                    break
    else:
        print(scanFile, "is not a valid file")
        sys.exit("Script Aborted")

except Exception as err:
    print("\n\nScript Aborted     ", "Exception =     ", err)        

myTable.align = "l"
print(myTable.get_string(sortby="Occurs", reversesort=True))
   