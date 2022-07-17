import os

root = "/home/martin/"
grabacionesFolder = root+"PsyBrainy/Grabaciones"


if __name__ == "__main__":

    def getMonthName(month):
        año = month[:5]
        mes = ""
        mes2 = int(month[6:])

        if mes2 == 1:
            mes = "Enero"
        elif mes2 == 2:
            mes = "Febrero"
        elif mes2 == 3:
            mes = "Marzo"
        elif mes2 == 4:
            mes = "Abril"
        elif mes2 == 5:
            mes = "Mayo"
        elif mes2 == 6:
            mes = "Junio"
        elif mes2 == 7:
            mes = "Julio"
        elif mes2 == 8:
            mes = "Agosto"
        elif mes2 == 9:
            mes = "Septiembre"
        elif mes2 == 10:
            mes = "Octubre"
        elif mes2 == 11:
            mes = "Noviembre"
        elif mes2 == 12:
            mes = "Diciembre"
        else:
            mes = "Error"
        return año + "-" + str(mes2) + "-" + mes

    os.makedirs(grabacionesFolder, exist_ok=True)
    for filename in os.listdir(root):
        name, extension = os.path.splitext(root + filename)

        if extension in [".mkv"]:
            newFolder = grabacionesFolder
            os.makedirs(newFolder , exist_ok=True)
            os.makedirs(newFolder + getMonthName(name[12:20]) , exist_ok=True)
            os.replace( root + filename , newFolder + getMonthName(name[12:20]) + "/" + filename)