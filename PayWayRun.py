import os
import sys

arguments = sys.argv

raiz = os.environ.get("FRONT") + "/"
command = " -e yarn " + arguments[1]

if __name__ == "__main__":

    for project in os.listdir(raiz):
        if project == "ui-backoffice":
            os.system("tilix -a session-add-down -w " + raiz + project + command)
            os.system("tilix -a session-add-down -w " + raiz + project+ "/layout" + command)
        elif project == "ui-payway-styleguide":
            os.system("tilix -a session-add-down -w " + raiz + project )
            os.system("tilix -a session-add-down -w " + raiz + project )
        else:    
            os.system("tilix -a session-add-down -w " + raiz + project + command)