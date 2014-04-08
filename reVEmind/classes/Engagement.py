# -*- coding: utf-8 -*-
"""
#==============================================================================
                #                   .~- Engagement ~-.
                #
                #                Created on 2/9/14
                #
                #                   @author: proC3ss
                #
#==============================================================================

"""
from Attack import *
import sqlite3 as lite

class Engagement(object):
    def __init__(self):
        self.__time_frame = None
        self.__weapons = None
        self.__pilots = None
        self.__hits_dealt = None #[s.asArray() for s in loglines if s.asArray()[0] != 'You']
        self.__hits_received = None #[s.asArray() for s in combatlines if s.asArray()[0] == 'You']
        self.__dmg_received = None #sum([int(s.asArray()[3]) for s in combatlines if s.asArray()[0] == 'You'])
        self.__dmg_dealt = None #sum([int(s.asArray()[3]) for s in combatlines if s.asArray()[0] != 'You'])
        self.__db = None
        self.__econ = None
        self.__ecurs = None

    @property
    def db(self):
        if self.__db is None:
            self.__db = 'ela.db'
        return self.__db

    @db.setter
    def db(self, val):
        self.__db = val

    @property
    def econ(self):
        if self.__econ is None:
            self.__econ = lite.connect(self.db)
        return self.__econ

    @property
    def ecurs(self):
        if self.__ecurs is None:
            self.__ecurs = self.econ.cursor()
        return self.__ecurs

    @property
    def time_frame(self):
        if self.__time_frame is None:
            return ['Not', 'Set']
        return self.__time_frame

    @time_frame.setter
    def time_frame(self, val):
        if len(val)!= 2:
            print "Please call timeframe with a 2 value array of date/datetimes"
        self.__time_frame = (val[0], val[1])
        self.getData()

    @property
    def weapons(self):
        if self.__weapons is None:
            a = list()
            self.__weapons = a
        return self.__weapons
    @property
    def pilots(self):
        if self.__pilots is None:
            a = list()
            self.__pilots = a
        return self.__pilots

    def getData(self):
        a = "SELECT * FROM Attacks WHERE timestamp BETWEEN '%s' AND '%s' ORDER BY timestamp" % (self.time_frame[0], self.time_frame[1])
        combatlines = self.ecurs.execute(a).fetchall()
        self.hits_dealt = [s for s in combatlines[0:-1] if s[0] == 'You']
        self.hits_received = [s for s in combatlines[0:-1] if s[2] == 'You']
        self.dmg_received = sum([int(s[3]) for s in combatlines[0:-1] if s[2] == 'You'])
        self.dmg_dealt = sum([int(s[3]) for s in combatlines[0:-1] if s[0] == 'You'])
        for event in combatlines:
            if event[4] not in self.weapons:
                self.weapons.insert(-1, event[4])
            if event[0] not in self.pilots:
                self.pilots.insert(-1, event[0])

    def getPilotStats(self, val):
        pilot = val
        qry_tot_dmg_taken = "SELECT damageAmmount FROM Attacks WHERE attacked LIKE '%s'" % str(pilot)
        qry_tot_dmg_dlt = "SELECT damageAmmount FROM Attacks WHERE attacker LIKE '%s'" % str(pilot)
        a = "SELECT * FROM Attacks WHERE timestamp BETWEEN '%s' AND '%s' ORDER BY timestamp" % (self.time_frame[0], self.time_frame[1])
        combatlines = self.ecurs.execute(a).fetchall()

        hits_dealt = [s for s in combatlines[0:-1] if s[0] == 'You']
        hits_received = [s for s in combatlines[0:-1] if s[0] != 'You']
        dmg_received = sum([int(s[3]) for s in combatlines[0:-1] if s[0] != 'You'])
        dmg_dealt = sum([int(s[3]) for s in combatlines[0:-1] if s[0] == 'You'])

        qry_tot_hits_taken = "SELECT COUNT(damageAmmount) FROM Attacks WHERE attacked LIKE '%s'" % str(pilot)
        qry_tot_hits_dlt = "SELECT COUNT(damageAmmount) FROM Attacks WHERE attacker LIKE '%s'" % str(pilot)
        qry_top_dmg_taken = "SELECT MAX(damageAmmount) FROM Attacks WHERE attacked LIKE '%s'" % str(pilot)
        qry_top_dmg_dlt = "SELECT MAX(damageAmmount) FROM Attacks WHERE attacker LIKE '%s'" % str(pilot)

        qry_avg_hit = "SELECT AVG(hitType) FROM Attacks WHERE attacker LIKE '%s'" % str(pilot)


if __name__ == '__main__':
    import datetime
    import sys
    import pyqtgraph as pg
    from pyqtgraph.Qt import QtGui
    def graph(self):
        self.win = pg.GraphicsWindow(title="Attack Event")
        self.win.resize(1000,600)
        self.win.setWindowTitle('Attack Event')
        pg.setConfigOptions(antialias=True)
        x = [datetime.datetime.strptime(s.asArray()[5], "%Y.%m.%d %H:%M:%S") for s in combatlines if s.asArray()[0] == 'You']
        y = [int(s.asArray()[3]) for s in combatlines if s.asArray()[0] == 'You']
        p1 = self.win.addPlot(title="Event")
        p1.plot(y)
        self.win.nextRow()
    app = QtGui.QApplication([])
    a = Engagement()

    fpath = QtGui.QFileDialog.getOpenFileName()
    combatlines = Attack().readlog(fpath)
    print str(a)
    print "--------"
    for s in a.pilots:
        print s
    print "--------"
    for s in a.weapons:
        print s
    a.graph()

    sys.exit(app.exec_())

