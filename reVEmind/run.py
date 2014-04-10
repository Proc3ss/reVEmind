# -*- coding: utf-8 -*-
"""
#==============================================================================
                #                   .~- run.py ~-.
                #
                #                Created on 4/9/14
                #
                #                   @author: proc3ss
                #
#==============================================================================


I decided to implement a run file and keep reVEmind.py a little cleaner for build purposes

"""
import sys, os
import PyQt4 as PyQt4
import reVEmind
mypath = os.path.dirname(os.path.abspath(sys.argv[0]))
dbpath = ''.join((mypath, "\ela.db"))

def Run():
    app = PyQt4.QtGui.QApplication(sys.argv)
    db = PyQt4.QtSql.QSqlDatabase.addDatabase("QSQLITE")
    if db:
        db.setDatabaseName(dbpath)
        if not db.open():
            print "Could not open testdb database"
            print db.lastError().driverText()
            print db.lastError().databaseText()
            sys.exit(1)
    myapp = reVEmind.reVEmind(dbpath)
    myapp.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    Run()
#
#
#
# # if __name__ == "__main__":
# #     import os, sys
# #     os.chdir()
# #     import reVEmind
# #     from reVEmind import __init__ as reve
# #     reve.runApp()
