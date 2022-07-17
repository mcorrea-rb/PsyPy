import os

root = "/home/martin/"
grabacionesFolder = root+"PsyBrainy/Grabaciones"


if __name__ == "__main__":

    def getMonthName(month):
        mes = ""
        mesNumero = int(month[6:])

        mesesresp = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
        
        for i in range(len(mesesresp)):
            if mesNumero == i+1:
                mes = mesesresp[i]
                break

        return month + "-" + mes

    os.makedirs(grabacionesFolder, exist_ok=True)
    for filename in os.listdir(root):
        name, extension = os.path.splitext(root + filename)

        if extension in [".mkv"]:
            newFolder = grabacionesFolder
            os.makedirs(newFolder , exist_ok=True)
            os.makedirs(newFolder + getMonthName(name[12:20]) , exist_ok=True)
            os.replace( root + filename , newFolder + getMonthName(name[12:20]) + "/" + filename)