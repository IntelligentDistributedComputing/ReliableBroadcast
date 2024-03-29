#
#   This file represents the Result function
#

##################################################################################################################################
#
#   IMPORTS
#
##################################################################################################################################

import utils.Utils as Utils
import utils.Logger as Logger

##################################################################################################################################
#
#   CLASS
#
##################################################################################################################################


class ProcessInfo:

    ##################################################################################################################################
    #
    #   VARIABLES
    #
    ##################################################################################################################################

    _time = None

    ##################################################################################################################################
    #
    #   CONSTRUCTOR
    #
    ##################################################################################################################################

    def __init__(self):
        self.setTime(0)

    ##################################################################################################################################
    #
    #   GET
    #
    ##################################################################################################################################

    def getTime(self):
        return self._time

    ##################################################################################################################################
    #
    #   SET
    #
    ##################################################################################################################################

    def setTime(self, time):
        self._time = time

    # ----------------------------------------------------------------

    def addTime(self, time):
        self._time += time

    ##################################################################################################################################
    #
    #   AUXILIAR
    #
    ##################################################################################################################################

    def printProcessInfo(self):
        Logger.logInfoMessage(
            "Total time: " + str(Utils.getTimePresentation(self.getTime())))
