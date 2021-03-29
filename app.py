from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# #Login to Google Drive and create drive object
gauth = GoogleAuth()
gauth.LocalWebserverAuth()
drive = GoogleDrive(gauth)

# # Importing os and glob to find all videos inside subfolder
# import glob, os
# os.chdir("/home/pi/Desktop/images/icon")
# for file in glob.glob("*.PNG"):
#     print(file)
#     with open(file,"r") as f:
#         fn = os.path.basename(f.name)
#         file_drive = drive.CreateFile({'title': fn })  
#     file_drive.SetContentString(f.read()) 
#     file_drive.Upload()
#     print("The file: " + fn + " has been uploaded")
#    
# print "All files have been uploaded"



file1 = drive.CreateFile({'title': 'Hello.txt'})  

file1.SetContentString('no no no') 

file1.Upload()