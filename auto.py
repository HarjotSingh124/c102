import dropbox
import time
start_time = time.time()

def upload_file():
    access_token = "sl.BCiMqMf5IQw2oolLLewYZ4om7bECWGNPUktny9-rQB4uFdx6bhwiwIRo7t7T0t1mtSm_jF7AOAzBAuJ2dCGpbxMZqLAm4DryonrDaZpORWV-5PVSP-3cRJoT76McqY8N_s5uV4Y"
    file = "auto.py"
    file_from = file
    file_to = "/Automation-master/" + (file)
    dbx = dropbox.Dropbox(access_token)
    
    with open (file_from,'rb') as f:
        dbx.files_upload(f.read(),file_to,mode = dropbox.files.WriteMode.overwrite)
        print("fileUploaded")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            upload_file()
main()
