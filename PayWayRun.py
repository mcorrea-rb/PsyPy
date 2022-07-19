import os
import sys

param = sys.argv[1]
root = os.environ.get("FRONT") + "/"


def run(query):
    os.system(query)

def runMicroFront( structure ):
    newTab = "tilix -a session-add-down -w "
    paths , comnd , project = structure

    abriendo = "_______________________________________\n·Abriendo " + project
    correComando = "   -corre comando" + comnd[3:] + "\n_______________________________________\n"
    npm = "   -corre comando npm run start\n_______________________________________\n"


    print(abriendo)
    if project=="ui-payway-styleguide":
        print(npm + "\n" + abriendo + "\n" + npm)
        run(newTab + paths + " -e npm run start ")
        run(newTab + paths + " -e npm run styleguidist ")
    elif project == "ui-backoffice":
        print(correComando + "\n" + abriendo + "/layout" + "\n" + correComando)
        run(newTab + paths + comnd)
        run(newTab + paths + "/layout" + comnd)
    else:
        print(correComando)
        run(newTab + paths + comnd)
    

def buildPathAndCommand( project ):
    command = " -e yarn " + param
    path = root + project
    return path , command , project


if __name__ == "__main__":

    proyectosList = os.listdir(root)

    list( map( runMicroFront , map( buildPathAndCommand , proyectosList ) ) )
