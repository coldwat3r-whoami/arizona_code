'''
WK-6 STARTER SCRIPT
CYBV 312
Professor Hosmer
FEBRUARY 2022
'''

# Libraries in starter script
import os
import re
import logging
import platform
import socket
import uuid

# Libraries I added
import psutil
import logging
import hashlib
import sys
import time

def getSystemInfo():
    try:
        info={}
        info['platform']=platform.system()
        info['platform-release']=platform.release()
        info['platform-version']=platform.version()
        info['architecture']=platform.machine()
        info['hostname']=socket.gethostname()
        info['ip-address']=socket.gethostbyname(socket.gethostname())
        info['mac-address']=':'.join(re.findall('..', '%012x' % uuid.getnode()))
        info['processor']=platform.processor()
        info['ram']=str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB"
        return info
    except Exception as e:
        logging.exception(e)
        return False


def main():
    
    # Remove any old logging script
    if os.path.isfile('Desantiago-Nicholas-ScriptLog.txt'):   # REPLACE YOURNAME with Your Name
        os.remove("Desantiago-Nicholas-ScriptLog.txt")
    
    # configure the python logger, Replace YOURNAME
    logging.basicConfig(filename='Desantiago-Nicholas-ScriptLog.txt', level=logging.DEBUG, format='%(process)d-%(levelname)s-%(asctime)s %(message)s')
    logging.info("Script Start\n")
    
    investigator = input("Investigator Name:  ")   # Enter Your Name at this prompt
    organization = input("Class Code  :       ")   # Enter the Class at this prompt i.e. CYBV-312 YOUR SECTION
    
    sysInfo = getSystemInfo()
    
    if sysInfo:
        ''' YOUR CODE GOES HERE 
            Write all collected information to the log file
        '''
        logging.info("  Investigator: "+investigator)
        logging.info("  Organization: "+organization)
        logging.info("  Purpose: Week 6 Logging Assignment")
        logging.info("="*70+str('\n\n\n'))
        logging.info("  System is: "+platform.system())
        logging.info("  Release is: "+platform.system())
        logging.info("  Version is: "+platform.version())
        logging.info("  Machine is: "+platform.machine())
        logging.info("  Hostname is: "+socket.gethostname())
        logging.info("  IP Address is: "+socket.gethostbyname(socket.gethostname()))
        logging.info("  MAC Address is "+':'.join(re.findall('..', '%012x' % uuid.getnode())))
        logging.info("  Processor is: "+platform.processor())
        logging.info("  Ram is: "+str(round(psutil.virtual_memory().total / (1024.0 **3)))+" GB")
        logging.info("="*70+str('\n\n\n'))
        
        
def GetFileMetaData(fileName):
	try:
		metaData =	os.stat(fileName)
			#Use the stat method to obtain meta data
		fileSize = metaData.st_size
			#Extract fileSize and MAC Times
		timeLastAccess = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(metaData.st_atime))
		timeLastModified = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(metaData.st_mtime))
		timeCreated = time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime(metaData.st_ctime))
		macTimeList =[timeLastModified, timeLastAccess, timeCreated]
			#Group the MAC Times in a List
		return True, None, fileSize, macTimeList

	except Exception as err:
		return False, str(err), None, None   

def WalkingDirs():

	dirToScan = input("Please enter directory to scan: ")
	print("Thouroughly walking directory now. Please wait...")
	time.sleep(1) #googled how to pause in Python and Gen AI provided this
	print("Looking under every rock. Almost done...")
	time.sleep(1)

    for root, dirs, fileList in os.walk(dirToScan):
        
        try:

            for nextFile in fileList:
				# Get the absolute path of the file--to be used for reporting and getting the file hash
                path = os.path.join(root, nextFile)
                absPath = os.path.abspath(path)
				# Call the GetFileMetadata function (from week 2 solution)
                success, errInfo, fileSize, macList = GetFileMetaData(absPath)
				# Open each file in read binary mode
            with open (absPath, 'rb') as targetFile:
				# Read the contents of the file and get the file hash
                fileContents = targetFile.read()
                sha256Obj = hashlib.sha256()
                sha256Obj.update(fileContents)
                hexDigest = sha256Obj.hexdigest()
                logging.info("  User specified directory: "+dirToScan)
                logging.info("="*70+str('\n\n\n'))
        
        except Exception as err:
            print("\n\nScript Aborted     ", "Exception =     ", err)

if __name__ == '__main__':
    
    print("\n\nWeek-6 Logging Starter Script - Nicholas Desantiago \n")
    main()
    WalkingDirs()
    print("\nScript End")

