# -*- coding: utf-8 -*-
"""
#==============================================================================
                #                   .~- __init__.py ~-.
                #
                #                Created on 4/2/14
                #
                #                   @author: proC3ss
"""

from reVEmind import reVEmind
import PyQt4
import sys


## the run() function allows the app to easily be launched via package extension without actually needing run.py
## (even though i have included a run.py for interoperability)

def run():
    import reVEmind
    app = PyQt4.QtGui.QApplication(sys.argv)
    db = PyQt4.QtSql.QSqlDatabase.addDatabase("QSQLITE")
    if db:
        db.setDatabaseName("ela.db")
        if not db.open():
            print "Could not open testdb database"
            print db.lastError().driverText()
            print db.lastError().databaseText()
            sys.exit(1)

    myapp = reVEmind.reVEmind()
    myapp.show()
    sys.exit(app.exec_())


