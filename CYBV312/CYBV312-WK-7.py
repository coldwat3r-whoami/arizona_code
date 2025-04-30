'''
Searching for Images with PIL
Nicholas Desantiago
CYBV 312 Fall 2024
'''

import sys
import os
import re
import time
from PIL import Image
from prettytable import PrettyTable

myTable = PrettyTable(["File", "Ext", "Format", "Width", "Height", "Mode"])

def main():

    print("\n*** Week 7 Script Nicholas Desantiago ***\n")
    dirToScan = input("Please enter directory to scan or Q to quit: ")
    if dirToScan.lower() == 'q':
        print("\nQuitting Directory Scanner now...")
        sys.exit()
    dirToScan = re.sub('"',"", dirToScan)
    print("Thoroughly walking directory now. Please wait...")
    time.sleep(1) #googled how to pause in Python and Gen AI provided this
    print("Cleaning up the PrettyTable. Almost done...\n")
    time.sleep(1)



    for root, dirs, fileList in os.walk(dirToScan):

        try:

            for nextFile in fileList:
                path = os.path.join(root, nextFile)
                absPath = os.path.abspath(path)
              
                if os.path.isfile(absPath):
                    ext = os.path.splitext(absPath)[1]

                    try:
                        
                        with Image.open(absPath) as im:
                            myTable.add_row([absPath, ext.upper(), im.format, im.width, im.height, im.mode])
                
                    except Exception as err:
                        myTable.add_row([absPath, ext.upper(), "N/A", "N/A", "N/A", "N/A"])
            
                else:
                    print("Path Provided is Not a Directory")
        except Exception as err:
            print("Could not walk this Directory...")
main()
myTable.align = "l"
print(myTable.get_string(sortby = ("Ext"), reversesort = False))
print("\nScript Complete!\n")
print("This was a wonderful class, thanks Professor Covington!!")
print("Any suggestions for learning more Python?")
