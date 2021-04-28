import cv2
import dropbox
import time
import random
startTime=time.time()
def takeSnapShot():
    N=random.randint(0,100)
    V=cv2.VideoCapture(0)
    result=True
    while(result):
        ret,frame=V.read()
        imageName="SnapShot"+str(N)+".jpg"
        cv2.imwrite(imageName,frame)
        result=False
    return imageName
    print("SnapShot Taken")
    V.release()
    cv2.destroyAllWindows()
def UploadFile(imageName):
    accessTolkien='NTa68lAjzZ0AAAAAAAAAAXYBkKV_dg-GgHkrWEujtFemM7PwFJ3TQMH0QkKR0-sd'
    file=imageName
    fileFrom=file
    fileto="/New Folder/"+(imageName)
    dbx=dropbox.Dropbox(accessTolkien)
    with open(fileFrom,'rb')as f:
        dbx.files_upload(f.read(),fileto,mode=dropbox.files.WriteMode.overwrite)
        print("filesUploaded")
def Main():
    while(True):
        if ((time.time()-startTime)>=60):
            name=takeSnapShot()
            UploadFile(name)
Main()