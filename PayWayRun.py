import os
import sys

arguments = sys.argv

root = os.environ.get("FRONT") + "/"
command = " -e yarn " + arguments[1]

def runMicroFront( structure ):
    newTab = "tilix -a session-add-down -w "
    paths = structure[0]
    comnd = structure[1]
    if paths.__contains__("ui-payway-styleguide"):
        os.system(newTab + paths)
        os.system(newTab + paths)
    elif paths == root + "ui-backoffice":
        os.system(newTab + paths + comnd)
        os.system(newTab + paths + "/layout" + comnd)
    else:
        os.system(newTab + paths + comnd)

def buildPathAndCommand( project ):
    print("_______________________________________")
    print("·Abriendo " + project)
    path = root + project
    print("   -corre comando" + command[3:])
    print("_______________________________________")
    print("")
    return path , command


if __name__ == "__main__":

    proyectosList = os.listdir(root)

    list( map( runMicroFront , map( buildPathAndCommand , proyectosList ) ))
