# -*- coding: utf-8 -*-
"""
#==============================================================================
                #                   .~- reVEmind ~-.
                #                      v-0.1_alpha
                #                Created on 1/16/14
                #
                #                   @author: ProC3ss
                #
#==============================================================================

"""
from os import listdir
from os.path import isfile, join
import sqlite3 as lite
from datetime import datetime
import locale
import PyQt4
import PyQt4.QtSql


from ui_files.revemind_ui import Ui_EveAnalyze
from classes.Attack import *
from classes.Engagement import *
locale.setlocale(locale.LC_TIME, '')


class reVEmind(PyQt4.QtGui.QMainWindow):
    def __init__(self, dbpath, parent=None):
        PyQt4.QtGui.QMainWindow.__init__(self, parent)
        self.ui = Ui_EveAnalyze()
        self.ui.setupUi(self)

        self.setModels()
        self.econ = lite.connect(dbpath)
        self.ecursor = self.econ.cursor()

        self.__LogDirs = None
        self.__TimeFrame = None

        PyQt4.QtCore.QObject.connect(self.ui.actionSelect_Folder, PyQt4.QtCore.SIGNAL("triggered()"), self.setLogDir)
        PyQt4.QtCore.QObject.connect(self.ui.actionImport_All_Files, PyQt4.QtCore.SIGNAL("triggered()"), self.importFiles)
        PyQt4.QtCore.QObject.connect(self.ui.logCalendar, PyQt4.QtCore.SIGNAL("clicked(QDate)"), self.pickedDate)
        PyQt4.QtCore.QObject.connect(self.ui.pushButton, PyQt4.QtCore.SIGNAL("pressed()"), self.findEngagements)

    @property
    def LogDirs(self):
        print "LogDirs Property"
        dirs = []
        if self.__LogDirs is None:
            qry = PyQt4.QtSql.QSqlQuery()
            if qry.exec_("SELECT FolderId, folder_path FROM LogDirs"):
                while qry.next():
                    dirs.insert(-1, [str(qry.value(0).toString()), str(qry.value(1).toString())])
                self.__LogDirs = dirs
        return self.__LogDirs

    @property
    def TimeFrame(self):
        if self.__TimeFrame is None:
            self.__TimeFrame = [0,0]
        return self.__TimeFrame

    @TimeFrame.setter
    def TimeFrame(self, tframe):
        model = PyQt4.QtSql.QSqlQueryModel(self)
        a = "SELECT * FROM Attacks WHERE timestamp BETWEEN '%s' AND '%s'" % (tframe[0], tframe[1])
        print ""
        model.setQuery(a)
        self.ui.loglineViewer.setModel(None)
        self.ui.loglineViewer.setModel(model)

        self.current_engagement = Engagement()
        self.current_engagement.time_frame = (tframe[0], tframe[1])
        self.updateValues()
        self.__TimeFrame = [tframe[0], tframe[1]]

    def pickedDate(self):
        s = self.sender()
        model = PyQt4.QtSql.QSqlQueryModel(self)
        thedate = s.selectedDate().toPyDate().strftime('%Y.%m.%d')
        self.TimeFrame = [thedate, str(thedate + ' 23:59:59')]


    def updateValues(self):
        self.updateGraph()
        self.updatePilotwindow()
        self.updateOverviewStats()

    def updateOverviewStats(self):
        stats = self.ui.listStats
        eng = self.current_engagement
        stats.clear()
        a = str("Dealt - Hits: " + str(len(eng.hits_dealt)) + str("\t Total Damage: ") + str(self.current_engagement.dmg_dealt))
        stats.addItem(a)
        a = str("Recvd - Hits: " + str(len(eng.hits_received)) + str("\t Total Damage: ") + str(self.current_engagement.dmg_received))
        stats.addItem(a)
        a = str("\n\tTotal Pilots:" + str(len(eng.pilots)))
        stats.addItem(a)

    def updateGraph(self):
        theplot = self.ui.plot_widget
        theplot.clear()
        dlt_x = [int(''.join(s[5][11:].split(':'))) for s in self.current_engagement.hits_dealt]
        dlt_y = [s[3] for s in self.current_engagement.hits_dealt]
        rcvd_x = [int(''.join(s[5][11:].split(':'))) for s in self.current_engagement.hits_received]
        rcvd_y = [s[3] for s in self.current_engagement.hits_received]
        if len(rcvd_x) > 0:
            theplot.setRange(xRange=(min(rcvd_x[0], dlt_x[0]), max(dlt_x[-1], rcvd_x[-1])), yRange=(0, max(max([s for s in rcvd_y]), max([s for s in dlt_y]))))
            # theplot.setRange(xRange=(000000, 240000))
            theplot.plot(y=dlt_y, x=dlt_x, pen=(1, 3))
            theplot.plot(y=rcvd_y, x=rcvd_x, pen=(2, 1))
            # theplot.
            # theplot.yAxis.setLabel("y")

    def updatePilotwindow(self):
        win = self.ui.pilotStack
        win.hide()
        for i in range(0, len(win) + 1):
            win.removeItem(0)
        # win.clear
        qcapp = str(self)
        vhdrs = ("Num Hits", "Total Damage", "Avg DPS", "Best Hit", "Hit Efficiency" )
        hhdrs = ("Dealt", "Received")

        tf0 = self.current_engagement.time_frame[0]
        tf1 = self.current_engagement.time_frame[1]
        # tf1 = self.TimeFrame[1]
        for row, pilot in enumerate(self.current_engagement.pilots):
            widg = PyQt4.QtGui.QTableWidget(win)
            widg.setColumnCount(len(hhdrs))
            widg.setRowCount(len(vhdrs))
            widg.setHorizontalHeaderLabels(hhdrs)
            widg.setVerticalHeaderLabels((vhdrs))

            item = PyQt4.QtGui.QTableWidgetItem()
            qry = "SELECT COUNT(damageAmmount), timestamp FROM Attacks WHERE (attacker IS '%s') AND (timestamp BETWEEN '%s' AND '%s')" % (str(pilot), tf0, tf1)
            tot_hits_dlt = str([s[0] for s in self.ecursor.execute(qry).fetchall()][0])
            item.setText(PyQt4.QtGui.QApplication.translate(qcapp, tot_hits_dlt, None, PyQt4.QtGui.QApplication.UnicodeUTF8))
            widg.setItem(0, 0, item)

            item = PyQt4.QtGui.QTableWidgetItem()
            qry = "SELECT SUM(damageAmmount), timestamp FROM Attacks WHERE (attacker IS '%s') AND (timestamp BETWEEN '%s' AND '%s')" % (str(pilot), tf0, tf1)
            tot_dmg_dlt = str([s[0] for s in self.ecursor.execute(qry).fetchall()][0])
            item.setText(PyQt4.QtGui.QApplication.translate(qcapp, tot_dmg_dlt, None, PyQt4.QtGui.QApplication.UnicodeUTF8))
            widg.setItem(1, 0, item)

            item = PyQt4.QtGui.QTableWidgetItem()
            qry = "SELECT MAX(damageAmmount), timestamp FROM Attacks WHERE (attacker IS '%s') AND (timestamp BETWEEN '%s' AND '%s')" % (str(pilot), tf0, tf1)
            top_dmg_dlt = str((self.ecursor.execute(qry).fetchone())[0])
            item.setText(PyQt4.QtGui.QApplication.translate(qcapp, top_dmg_dlt, None, PyQt4.QtGui.QApplication.UnicodeUTF8))
            widg.setItem(3, 0, item)

            item = PyQt4.QtGui.QTableWidgetItem()
            qry = "SELECT AVG(hitType), timestamp FROM Attacks WHERE (attacker IS '%s') AND (timestamp BETWEEN '%s' AND '%s')" % (str(pilot), tf0, tf1)
            avg_rcvd = str((self.ecursor.execute(qry).fetchone())[0])
            if avg_rcvd is None: avg_rcvd = "-"
            item.setText(PyQt4.QtGui.QApplication.translate(qcapp, avg_rcvd, None, PyQt4.QtGui.QApplication.UnicodeUTF8))
            widg.setItem(4, 0, item)

            item = PyQt4.QtGui.QTableWidgetItem()
            qry = "SELECT COUNT(damageAmmount), timestamp FROM Attacks WHERE (attacked IS '%s') AND (timestamp BETWEEN '%s' AND '%s')" % (str(pilot), tf0, tf1)
            tot_hits_taken = str([s[0] for s in self.ecursor.execute(qry).fetchall()][0])
            if tot_hits_taken is None: top_dmg_taken = "-"
            item.setText(PyQt4.QtGui.QApplication.translate(qcapp, tot_hits_taken, None, PyQt4.QtGui.QApplication.UnicodeUTF8))
            widg.setItem(0, 1, item)

            item = PyQt4.QtGui.QTableWidgetItem()
            qry = "SELECT SUM(damageAmmount), timestamp FROM Attacks WHERE (attacked IS '%s') AND (timestamp BETWEEN '%s' AND '%s')" % (str(pilot), tf0, tf1)
            top_dmg_taken = str([s[0] for s in self.ecursor.execute(qry).fetchall()][0])
            if top_dmg_taken is None: top_dmg_taken = "-"
            item.setText(PyQt4.QtGui.QApplication.translate(qcapp, top_dmg_taken, None, PyQt4.QtGui.QApplication.UnicodeUTF8))
            widg.setItem(1, 1, item)

            item = PyQt4.QtGui.QTableWidgetItem()
            qry = "SELECT MAX(damageAmmount), timestamp FROM Attacks WHERE (attacked IS '%s') AND (timestamp BETWEEN '%s' AND '%s')" % (str(pilot), tf0, tf1)
            top_hit_taken = str((self.ecursor.execute(qry).fetchone())[0])
            if top_hit_taken is None: top_hit_taken = "-"
            item.setText(PyQt4.QtGui.QApplication.translate(qcapp, top_hit_taken, None, PyQt4.QtGui.QApplication.UnicodeUTF8))
            widg.setItem(3, 1, item)

            item = PyQt4.QtGui.QTableWidgetItem()
            qry = "SELECT AVG(hitType), timestamp FROM Attacks WHERE (attacked IS '%s') AND (timestamp BETWEEN '%s' AND '%s')" % (str(pilot), tf0, tf1)
            avg_rcvd = str((self.ecursor.execute(qry).fetchone())[0])
            if avg_rcvd is None: avg_rcvd = "-"
            item.setText(PyQt4.QtGui.QApplication.translate(qcapp, avg_rcvd, None, PyQt4.QtGui.QApplication.UnicodeUTF8))
            widg.setItem(4, 1, item)
            widg.resizeRowsToContents()
            # widg.resizeColumnsToContents()
            win.insertItem(row, widg, str(pilot))

        win.show()
        # print "b"

    def createDB(self):
        self.ecursor.execute("DROP TABLE IF EXISTS LogDirs")
        self.ecursor.execute("CREATE TABLE LogDirs(FolderId INTEGER PRIMARY KEY, folder_path TEXT NOT NULL, type TEXT, description TEXT)")

        self.ecursor.execute("DROP TABLE IF EXISTS FilesImported")
        self.ecursor.execute("CREATE TABLE FilesImported(FileId INTEGER PRIMARY KEY, FolderId INTEGER NOT NULL, filename TEXT NOT NULL, completed INTEGER DEFAULT 0, FOREIGN KEY(FolderId) REFERENCES LogDirs(Id))")

        self.ecursor.execute("DROP TABLE IF EXISTS Attacks")
        self.ecursor.execute("CREATE TABLE Attacks(attacker TEXT, hitType TEXT, attacked TEXT, damageAmmount INTEGER, weapon TEXT, timestamp DATETIME, FileId INTEGER, FOREIGN KEY(FileId) REFERENCES FilesImported(FileId))")
        self.econ.commit()
        return 1

    def setModels(self):
        model = PyQt4.QtSql.QSqlQueryModel(self)
        a = "SELECT * FROM Attacks WHERE timestamp LIKE '%s' ORDER BY timestamp DESC" % str(self.ui.logCalendar.selectedDate().toPyDate().strftime('%Y.%m.%d'))
        model.setQuery(a)
        self.ui.loglineViewer.setModel(model)
        self.ui.loglineViewer.resizeColumnsToContents()
        return None

    def setLogDir(self):
        # print "setLogDir"
        if(self.createDB() == 1):
            # print "99"
            fpath = PyQt4.QtGui.QFileDialog.getExistingDirectory()
            self.log_folder = fpath
            self.ecursor.execute("INSERT INTO LogDirs(folder_path, type) VALUES (?, ?)", [str(self.log_folder), str("Combat")])
            self.econ.commit()
            self._log_dirs = None


    def listFiles(self, folderpath):
        folderpath = str(folderpath)
        files = [ f for f in listdir(folderpath) if isfile(join(folderpath,f)) ]
        return files

    def commitFileName(self, folderid, filename):
        self.ecursor.execute("INSERT INTO FilesImported(FolderId, filename) VALUES (?, ?)", [folderid, str(filename)])
        self.econ.commit()
        lid = self.ecursor.lastrowid
        return lid

    def check_ifImported(self, val):
        qry = str("SELECT filename, folder_path, completed FROM FilesImported NATURAL JOIN LogDirs WHERE folder_path LIKE '%s' AND filename LIKE '%s' AND completed=1") % (val[0], val[1])
        self.ecursor.execute(qry)
        if(len(self.ecursor.fetchall()) > 0):
            print "already done"
            return 0
        else:
            return 1

    def importFiles(self):
        # print "113"
        for logdir in self.LogDirs:
            for f in list(self.listFiles(logdir[1])):
                logpath = join(str(logdir[1]), f)
                if(self.check_ifImported((logdir[1], f)) == 1):
                    lid = self.commitFileName(logdir[0], f)
                    aa = Attack().readlog(logpath)
                    bb = [s.asArray() for s in aa]
                    [d.insert(int(len(d)), lid) for d in bb]
                    # print "line 68"
                    try:
                        self.writeLogFile(bb)
                    except:
                        raise
                    finally:
                        try:
                            self.econ.commit()
                        except:
                            raise
                        finally:
                            self.ecursor.execute(str("UPDATE FilesImported SET completed=1 WHERE FileId=%s;" % lid))
                            self.econ.commit()

    def writeLogFile(self, vals):
        vals = [s for s in vals]
        self.ecursor.executemany("INSERT INTO Attacks VALUES (?, ?, ?, ?, ?, ?, ?)", vals)

    def updateImports(self):
        print "Updating folders from LogDirs"
        logdirs = self.LogDirs
        for dir in self.LogDirs:
            files = self.listFiles(dir[1])

    def findEngagements(self):
        found = list()
        engagement = list()
        attacks = self.ecursor.execute("SELECT * FROM Attacks").fetchall()
        engagement.append(attacks[0])
        previous = datetime.strptime(attacks[0][5], "%Y.%m.%d %H:%M:%S")
        for attack in attacks[1:]:
            current = datetime.strptime(attack[5], "%Y.%m.%d %H:%M:%S")
            if(abs(current - previous).total_seconds() > 90):
                found.append(engagement)
                engagement = list()
            engagement.append(attack)
            previous = current
        # print "Break"
        return found


