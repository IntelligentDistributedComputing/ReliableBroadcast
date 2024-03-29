##################################################################################################################################
#
#   IMPORTS
#
##################################################################################################################################

#
from termcolor import colored
#
import logging
#

##################################################################################################################################
#
#   VARIABLES
#
##################################################################################################################################

logging.basicConfig(level=logging.INFO, format='%(message)s')

# Logging levels:
#   1. DEBUG
#   2. INFO
#   3. WARNING
#   4. ERROR
#   5. CRITICAL

##################################################################################################################################
#
#   PRINT
#
##################################################################################################################################


def logInfoMessage(message):
    text = colored(message, 'white')
    logging.info(str(text))

# ----------------------------------------------------------------


def logDebugMessage(message):
    text = colored("(DEBUG) - "+message, 'blue')
    logging.debug(str(text))

# ----------------------------------------------------------------


def logErrorMessage(message):
    text = colored("(ERROR) - "+message, 'red')
    logging.error(str(text))
