'''
Script:Week 3 Scripting Assignment Starting Point
Author:Nicholas Desantiago
Date:September 2024
Version:1.0
Purpose:Directory Metadata and Hashing

ASSIGNMENT DETAILS
Create a new script with the following requirements:
Allow the user to specify a starting directory using the built - in Python input() function

Using os.walk()
Acquire the following information for each file(subdirectories included)
:
			File		Path    (absolute path)
	File		Size
			MAC		Times    (in human readable form)
		SHA -		256	Hash value

		Store		the	results in a prettytable with the headings:
		AbsPath      , FileSize, LastModified, LastAccess, CreatedTime, HASH

		Display	the	prettytable sorted by FileSize
		Catch		and	report any errors

		Submit:
		1)
	Your final	script
			2)
	A screenshot from within WingIDE of a successful execution

			'''

''' IMPORT STANDARD LIBRARIES '''
import os
#File System Methods
import sys
#System Methods
import time
#Time Conversion Methods
import hashlib
#Python standard library hashlib


''' IMPORT 3RD PARTY LIBRARIES '''
from prettytable import PrettyTable
#pip install prettytable

''' DEFINE PSEUDO CONSTANTS '''


''' LOCAL FUNCTIONS '''

def GetFileMetaData(fileName):
	'''
	obtain	filesystem metadata
	from the specified file
	specifically , fileSize and MAC Times
	return	True  , None, fileSize and MacTimeList
	'''
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

''' LOCAL CLASSES '''
#NONE

''' MAIN ENTRY POINT '''

if __name__ == '__main__':

	dirToScan = input("Please enter directory to scan: ")
	myTable = PrettyTable(["AbsPath", "FileSize", "LastModified", "LastAccess", "CreatedTime", "SHA-256 HASH"])
	print("Thouroughly walking directory now. Please wait...")
	time.sleep(1) #googled how to pause in Python and Gen AI provided this
	print("Looking under every rock. Almost done...")
	time.sleep(1)
	for root, dirs, fileList in os.walk(dirToScan):

		try:

			#For each of the files in the file list, do the following:
			for nextFile in fileList:
				#Get the absolute path of the file--to be used for reporting and getting the file hash
				path = os.path.join(root, nextFile)
				absPath = os.path.abspath(path)
				#Call the GetFileMetadata function (from week 2 solution)
				success, errInfo, fileSize, macList = GetFileMetaData(absPath)
				#Open each file in read binary mode
			with open (absPath, 'rb') as targetFile:
				#Read the contents of the file and get the file hash
				fileContents = targetFile.read()
				sha256Obj = hashlib.sha256()
				sha256Obj.update(fileContents)
				hexDigest = sha256Obj.hexdigest()
				myTable.add_row([absPath, fileSize, macList[0], macList[1], macList[2], hexDigest])
		except Exception as err:
			print("\n\nScript Aborted     ", "Exception =     ", err)
	print("\nFully walked directories for: ", dirToScan, "\n")
	myTable.align = "l"
	print(myTable)
