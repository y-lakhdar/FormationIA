from abc import abstractmethod

__author__ = 'jbecirovski'


class PlayBase:
    """
    Play contain:
    + Contain Sequence of Tactics for each bots
    + Manage Tactic attribution
    """
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name

    @abstractmethod
    def getTactics(self, p_bb):
        """
        :return: list like [TacticB0, TacticB1, ..., TacticB5]
        """

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return 'Play: ' + self.name