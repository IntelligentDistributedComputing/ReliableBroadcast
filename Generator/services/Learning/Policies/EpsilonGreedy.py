
#
#   Epsilon Greedu with Counter-based approach
#

##################################################################################################################################
#
#   IMPORTS
#
##################################################################################################################################

#
import random
import numpy
#
from services.Learning.Policies.Greedy import Greedy
from services.Learning.Policies.Policy import Policy
from services.Learning.Policies.Random import Random
#

##################################################################################################################################
#
#   CLASS
#
##################################################################################################################################


class EpsilonGreedy(Policy):

    ##################################################################################################################################
    #
    #   VARIABLES
    #
    ##################################################################################################################################

    _greedy = None
    _random = None

    # ------------------
    # configurations
    # ------------------
    _epsilon = 1
    _max_epsilon = 1
    _min_epsilon = 0.001
    _decay_rate = 0.01
    _counter = 0

    ##################################################################################################################################
    #
    #   CONSTRUCTOR
    #
    ##################################################################################################################################

    def __init__(self):
        super().__init__()
        self._greedy = Greedy()
        self._random = Random()

    ##################################################################################################################################
    #
    #   GET
    #
    ##################################################################################################################################

    def isEpsilonGreedy(self):
        return True

    ##################################################################################################################################
    #
    #   SET
    #
    ##################################################################################################################################

    def updateEpsilon(self):
        self._counter += 1
        self._epsilon = self._min_epsilon + \
            (self._max_epsilon - self._min_epsilon) * \
            numpy.exp(-self._decay_rate*self._counter)

    ##################################################################################################################################
    #
    #   LOGIC
    #
    ##################################################################################################################################

    def runPolicy(self, input):

        # ------------------
        # input
        # ------------------
        state = input["state"]
        actions = input["actions"]
        knowledge = input["knowledge"]

        # ------------------
        # decide action
        # ------------------
        extra = {}
        if(random.uniform(0, 1) > self._epsilon):
            # select best action
            action_selected, extra = self._greedy.runPolicy(input)
        else:
            # explore randomly
            action_selected, extra = self._random.runPolicy(
                input)  # random.choice(actions)

        # ------------------
        # epsilon
        # ------------------
        extra["epsilon"] = self._epsilon

        return action_selected, extra
