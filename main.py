import dotenv
import os
import email_extraction
import pdfminer_multiple
import resume
dotenv_file = dotenv.find_dotenv()
dotenv.load_dotenv(dotenv_file)

while True:
    os.environ["API_PATH_PDF"] = input("enter path where you want to download ")

    dotenv.set_key(dotenv_file, "API_PATH_PDF", os.environ["API_PATH_PDF"])
    path=os.environ["API_PATH_PDF"]
    if not os.path.exists(path+'/'):
        val=input("this directory does not exist, enter path again yes or no")
        if val=="yes":
            continue
        elif val=="no":
            val1=input("do you want to create directory in this path yes or no")
            if val1=="yes":
                os.mkdir(path+'/')
                email_extraction.attachment_download(path)
                break
            elif val1=="no":
                exit()
            else:
                print("invalid input")
        else:
             print("enter either yes or no only")

    elif os.path.exists(path+'/'):

        email_extraction.attachment_download(path)
        break
 

os.environ["API_PATH_TXT"] = input("enter path where you want to STORE CONVERTED TXT FILES ")

dotenv.set_key(dotenv_file, "API_PATH_TXT", os.environ["API_PATH_TXT"])
pdfDir = os.environ["API_PATH_PDF"] + '/'
txtDir = os.environ["API_PATH_TXT"] +'/'
pdfminer_multiple.convertMultiple(pdfDir, txtDir)

resume.scanner(os.environ["API_PATH_TXT"] +'/')


