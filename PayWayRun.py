import os
import sys

arguments = sys.argv

root = os.environ.get("FRONT") + "/"
command = " -e yarn " + arguments[1]

def runMicroFront( paths, comnd ):
    newTab = "tilix -a session-add-down -w "
    os.system(newTab + paths + comnd)

if __name__ == "__main__":

    for project in os.listdir(root):

        path = root + project

        if project == "ui-backoffice":
            runMicroFront( path , command )
            runMicroFront( path + "/layout" , command )
        elif project == "ui-payway-styleguide":
            runMicroFront( path , "" )
            runMicroFront( path , "" )
        else:    
            runMicroFront( path , command )