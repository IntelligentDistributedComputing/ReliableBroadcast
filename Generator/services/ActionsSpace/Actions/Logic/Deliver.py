#
#   This file represents the DELIVER() action

##################################################################################################################################
#
#   IMPORTS
#
##################################################################################################################################

#
from services.ActionsSpace.Actions.Logic.Finish import FINISH
#
import inputs.GenerationInputs as GenerationInputs
import utils.GlobalVariables.TextVariables as Vars

##################################################################################################################################
#
#   CLASS
#
##################################################################################################################################


class DELIVER(FINISH):

    ##################################################################################################################################
    #
    #   VARIBLES
    #
    ##################################################################################################################################

    ##################################################################################################################################
    #
    #   CONSTRUCTOR
    #
    ##################################################################################################################################

    def __init__(self, message):
        super().__init__(Vars.DELIVER, "DELIVER("+message.getLabel()+")",
                         message, GenerationInputs.getLogicReward(Vars.DELIVER))

    ##################################################################################################################################
    #
    #   SET
    #
    ##################################################################################################################################

    def setMessage(self, message):
        self._message = message

    ##################################################################################################################################
    #
    #   GET
    #
    ##################################################################################################################################

    def getExtraConditionLabel(self):
        return " and not already delivered"

    ##################################################################################################################################
    #
    #   LOGIC
    #
    ##################################################################################################################################

    def __eq__(self, action):
        return super().__eq__(action) and (type(action) is DELIVER)

    # ----------------------------------------------------------------

    def isDELIVER(self):
        return True

    ##################################################################################################################################
    #
    #   PROMELA
    #
    ##################################################################################################################################

    # def getPROMELADefinition(self):
    #    label = ""
    #    label += "/*********** DELIVER ***********/\n"
    #    label += "if\n"
    #    label += ":: messages_delivered[ID].m[msg]==0 ->\n"
    #    label += "messages_delivered[ID].m[msg]++;\n"
    #    label += "::else;\n"
    #    label += "fi;\n"
    #    return label