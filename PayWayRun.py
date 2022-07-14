import os
import sys

arguments = sys.argv

root = os.environ.get("FRONT") + "/"
command = " -e yarn " + arguments[1]

def runMicroFront( paths, comnd ):
    newTab = "tilix -a session-add-down -w "
    if paths.__contains__("ui-payway-styleguide"):
        os.system(newTab + paths + comnd)
        os.system(newTab + paths + comnd)
    elif paths == root + "ui-backoffice":
        os.system(newTab + paths + comnd)
        os.system(newTab + paths + "/layout" + comnd)
    else:
        os.system(newTab + paths + comnd)

def verifyProject(project):
    if project == "ui-payway-styleguide":
        print("sin comando")
        return ""
    else:
        print("corre comando" + command[3:])
        return command

def path(project):
    print("Abriendo " + project)
    return root + project

if __name__ == "__main__":

    proyectosList = os.listdir(root)

    list( map(runMicroFront , map( path , proyectosList ) , map(verifyProject , proyectosList ) ))
