import os
import sys

arguments = sys.argv

root = os.environ.get("FRONT") + "/"
command = " -e yarn " + arguments[1]

if __name__ == "__main__":

    for project in os.listdir(root):

        path = root + project

        if project == "ui-backoffice":
            os.system("tilix -a session-add-down -w " + path + command)
            os.system("tilix -a session-add-down -w " + path + "/layout" + command)
        elif project == "ui-payway-styleguide":
            os.system("tilix -a session-add-down -w " + path )
            os.system("tilix -a session-add-down -w " + path )
        else:    
            os.system("tilix -a session-add-down -w " + path + command)