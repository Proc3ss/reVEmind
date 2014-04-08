# -*- coding: utf-8 -*-
"""
#==============================================================================
                #                   .~- testing ~-.
                #
                #                Created on 1/15/14
                #
                #                   @author: proC3ss
                #
#==============================================================================

"""
import re
combat_regexp = re.compile("(?:\[ )(?P<timestamp>\d+.\d+.\d+ \d+:\d+:\d+)(?: \])(?: \(combat\) \<\S+\>\<b\>)"
                           "(?P<dammageAmmount>\d+)(?:\<[ \S]+\>)(?P<tofrom>to|from)(?:\<[ \S]+\>)"
                           "(?P<attacked>[\S]+\s+[\S]+[\[\]\(\)\w]+)(?:\<[ \S]+\> \- )(?P<attacker_weapon>"
                           "[\w ]+)(?: - )(?P<hitType>[\w]+)")
class Attack(object):
    def __init__(self):

        self.__missed = None
        self.__hitType = None
        self.__attacker_name = None
        self.__attacker_weapon = None
        self.__attacked = None
        self.__damageAmmount = None
        self.__timestamp = None
        self.__logpath = None

    def __repr__(self):
        a = "\n Attacker:  %s" % (self.attacker_name)
        a += "\n %s:  %s" % (self.hitType, self.attacked)
        a += "\n For:  %s damage" % (self.damageAmmount)
        a += "\n With:  %s" % (self.attacker_weapon)
        a += "\n At:  %s" % (self.timestamp)
        a += "\n"
        return a


    @property
    def attacker_name(self):
        if self.__attacker_name == None: return "0"
        else: return self.__attacker_name

    @attacker_name.setter
    def attacker_name(self, val):
        self.__attacker_name = val

    @property
    def hitType(self):
        if self.__hitType == None: return "Attacked"
        else: return self.__hitType

    @hitType.setter
    def hitType(self, val):
        self.__hitType = val

    @property
    def attacked(self):
        if self.__attacked is None: return "0"
        else: return self.__attacked

    @attacked.setter
    def attacked(self, val):
        self.__attacked = val

    @property
    def damageAmmount(self):
        if self.__damageAmmount == None: return "0"
        else: return self.__damageAmmount

    @damageAmmount.setter
    def damageAmmount(self, val):
        self.__damageAmmount = val

    @property
    def attacker_weapon(self):
        if self.__attacker_weapon is None: return "0"
        else: return self.__attacker_weapon

    @attacker_weapon.setter
    def attacker_weapon(self, val):
        self.__attacker_weapon = val

    @property
    def timestamp(self):
        if self.__timestamp is None: return "0"
        else: return self.__timestamp

    @timestamp.setter
    def timestamp(self, val):
        self.__timestamp = val

    @property
    def missed(self):
        if self.__missed is None: return "0"
        else: return self.__missed

    @missed.setter
    def missed(self, val):
        self.__missed = val

    @property
    def logpath(self):
        if self.__logpath is None: return "0"
        else: return self.__logpath

    @logpath.setter
    def logpath(self, val):
        self.__logpath = val


    def setVals_fromLine(self, logline, logpath):
        """
        Set the values for a single Attack from a log line
        :param logline:
        """
        lvs = combat_regexp.match(logline).groups()
        self.timestamp = lvs[0]
        self.damageAmmount = lvs[1]
        if str(lvs[2]) == "to":
            self.attacked = lvs[3]
            self.attacker_name = "You"
        if str(lvs[2]) == "from":
            self.attacked = "You"
            self.attacker_name = lvs[3]
        self.attacker_weapon = lvs[4]
        self.hitType = lvs[5]
        self.logpath = "".join(logpath)


    def asArray(self):
        return [self.attacker_name, self.hitType, self.attacked, self.damageAmmount, self.attacker_weapon, self.timestamp]
        #, self.logpath

    def readlog(self, val):
        """
        Takes an open logfile and returns an array of Attacks
        :param logfile:
        :return:
        """
        path = str(val)
        combatlines = []
        print str(path)
        logfile = open(path, "r")
        for line in logfile:
            event = Attack()
            try:
                event.setVals_fromLine(line, path)
            except:
                event = 0
            if event != 0:
                combatlines.insert(-1, event)
        return combatlines
        # ###maybe use w/ engagement class
        # weapons = []
        # pilots = []
        # if event.asArray()[4] not in weapons:
        #     weapons.insert(-1, event.asArray()[4])
        # if event.asArray()[0] not in pilots:
        #     pilots.insert(-1, event.asArray()[0])
