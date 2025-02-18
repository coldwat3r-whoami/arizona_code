'''
Script:  First Script
Author:  Nicholas Desantiago
Date:    September 2024
Version: 1.50
Purpose: Week2 Script Fix

ASSIGNMENT DETAILS
After experimenting with the First.py script and attending this weeks lecture, you are to modify/extend the First.py script as follows:

1) Allow the user to specify a directory to process using the built-in Python input() function
2) Process each entry in that directory and report:
    Full-Filepath, FileSize, MAC Times for each directory entry
    Converting each MAC epoch value into human readable form
3) Catch any errors when attempting to process files and report them

LECTURE HINTS

    PROMPT USER FOR ENTRY
        directory = input("Enter a Directory to Process: ")
    
    CONVERT EPOCH VALUES TO HUMAN READABLE UTC TIME
        Epoch= macTimes[0]
        utcTime= time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(modEpoch))
        print(utcTime)
    
'''

''' IMPORT STANDARD LIBRARIES '''
import os       # File System Methods
import sys      # System Methods
import time     # Time Conversion Methods


''' IMPORT 3RD PARTY LIBRARIES '''
from prettytable import PrettyTable

''' DEFINE PSEUDO CONSTANTS '''

# NONE

''' LOCAL FUNCTIONS '''

def GetFileMetaData(fileName):
    ''' 
        obtain filesystem metadata
        from the specified file
        specifically, fileSize and MAC Times
        
        return True, None, fileSize and MacTimeList
    '''
    try:
        
        metaData         = os.stat(fileName)       # Use the stat method to obtain meta data
        fileSize         = metaData.st_size         # Extract fileSize and MAC Times
        timeLastAccess   = metaData.st_atime
        timeLastModified = metaData.st_mtime
        timeCreated      = metaData.st_ctime
        
        macTimeList = [timeLastModified, timeLastAccess, timeCreated] # Group the MAC Times in a List
        
        Epoch0= macTimeList[0]
        utcLastAccess= time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(Epoch0))
        
        Epoch1= macTimeList[1]
        utcLastModified= time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(Epoch1))
        
        Epoch2= macTimeList[2]
        utcTimeCreated= time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(Epoch2))        
        
        return True, None, fileSize, utcLastAccess, utcLastModified, utcTimeCreated
    
    except Exception as err:
        return False, str(err), None, None

''' LOCAL CLASSES '''
# NONE

''' MAIN ENTRY POINT '''

if __name__ == '__main__':
    
    print("\nWK-2 Solution: Nicholas Desantiago - Version 1.5\n")
    myTable = PrettyTable(["File Name", "Path", "File Size", "utcLastAccess", "utcLastModified", "utcTimeCreated"])

    targetDIR = input('Enter a Directory Path i.e. c:/ >>> ')
    print()
    
    try:
        fileList = os.listdir(targetDIR)
        for eachFile in fileList:
            print("Processing: ", eachFile)
            path = os.path.join(targetDIR, eachFile)

            success, errInfo, fileSize, utcLastAccess, utcLastModified, utcTimeCreated = GetFileMetaData(path)
            
            myTable.add_row([eachFile, path, fileSize, utcLastAccess, utcLastModified, utcTimeCreated])
            
            # Your additional script code here
            
    except Exception as err:
        print("\n\nScript Aborted     ", "Exception =     ", err)
        
    print(myTable)