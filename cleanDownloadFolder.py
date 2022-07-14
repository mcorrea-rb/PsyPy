import os
from zipfile import ZipFile

raiz = os.environ.get("HOME") + "/"

downloadFolder = raiz+"Descargas/"
imageFolder = raiz+"Imágenes/"
documentsFolder = raiz+"Documentos/"
videoFolder = raiz+"Vídeos/"

frontFolder = os.environ.get("FRONT") + "/"
backFolder = os.environ.get("BACK") + "/"

if __name__ == "__main__":
    for filename in os.listdir(downloadFolder):
        name, extension = os.path.splitext(downloadFolder + filename)

        if extension in [".zip"]:
            zip = ZipFile(downloadFolder + filename)
            if name.__contains__("ui-"):
                zip.extractall(frontFolder)
                print("Se descomprimio :" + filename + " en front")
            elif name.__contains__("-develop"):
                zip.extractall(backFolder)
                print("Se descomprimio :" + filename + " en back")
            else:
                zip.extractall(downloadFolder)
                print("Se descomprimio :" + filename)
            os.remove(downloadFolder + filename)
        if extension in [".jpg", ".jpeg" , ".png"]:
            os.replace(downloadFolder + filename , imageFolder + filename) 
            print("Se movio imagen :" + filename)
        if extension in [".pdf", ".doc" , ".json" , ".pptx" , ".txt" , ".csv"]:
            os.replace(downloadFolder + filename , documentsFolder + filename)
            print("Se movio documento :" + filename) 
        if extension in [".deb" , ".crdownload"]:
            print("Se borra crap")
            os.remove(downloadFolder + filename) 
        if extension in [".mp4"]:
            os.replace(downloadFolder + filename , videoFolder + filename)
            print("Se movio video :" + filename)