import os
import sys

param = sys.argv[1]

root = os.environ.get("FRONT") + "/"


def run(query):
    os.system(query)

def runMicroFront( structure ):
    newTab = "tilix -a session-add-down -w "
    paths = structure[0]
    comnd = structure[1]
    project = structure[2]

    print("_______________________________________")
    print("·Abriendo " + project)
    if project=="ui-payway-styleguide":
        print("   -sin comando")
        print("_______________________________________")
        print("")
        run(newTab + paths)
        print("_______________________________________")
        print("·Abriendo " + project)
        print("   -sin comando")
        print("_______________________________________")
        print("")
        run(newTab + paths)
    elif project == "ui-backoffice":
        print("   -corre comando" + comnd[3:])
        print("_______________________________________")
        print("")
        run(newTab + paths + comnd)
        print("_______________________________________")
        print("·Abriendo " + project + "/layout")
        print("   -corre comando" + comnd[3:])
        print("_______________________________________")
        print("")
        run(newTab + paths + "/layout" + comnd)
    else:
        print("   -corre comando" + comnd[3:])
        print("_______________________________________")
        print("")
        run(newTab + paths + comnd)
    

def buildPathAndCommand( project ):
    command = " -e yarn " + param
    path = root + project
    return path , command , project


if __name__ == "__main__":

    proyectosList = os.listdir(root)

    list( map( runMicroFront , map( buildPathAndCommand , proyectosList ) ) )
