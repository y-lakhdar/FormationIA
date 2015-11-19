from abc import abstractmethod

__author__ = 'jbecirovski'


class TacticBase:
    """
    Tactic contain:
    + Contain Sequence of Skills for each bots
    + Manage Skill attribution
    """
    def __init__(self, p_name):
        assert isinstance(p_name, str)
        self.name = p_name

    @abstractmethod
    def getSkill(self, p_id, p_bb):
        """
        :return: Specific Skill
        """
        pass

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return 'Tactic: ' + self.name