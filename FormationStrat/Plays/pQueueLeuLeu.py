from FormationStrat.Plays.PlayBase import PlayBase
from FormationStrat.Tactics.tFollowPrevPlayer import tFollowPrevPlayer

__author__ = 'jbecirovski'


class pQueueLeuLeu(PlayBase):
    """
    Play contain:
    + Contain Sequence of Tactics for each bots
    + Manage Tactic attribution
    """
    def __init__(self, blackboard):
        PlayBase.__init__(self, self.__class__.__name__)
        self.__data = [tFollowPrevPlayer() for x in range(6)]

    def getTactics(self, p_bb):
        """
        :return: list like [TacticB0, TacticB1, ..., TacticB5]
        """
        return self.__data