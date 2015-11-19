from abc import abstractmethod
from RULEngine.Util.Pose import Position

__author__ = 'jbecirovski'


class SkillBase:
    """
    Skill contain:
    + Contain Sequence of Action for each bots
    + Generate Action
    """
    def __init__(self, name):
        assert isinstance(name, str)
        self.name = name

    @abstractmethod
    def act(self, p_id, p_bb):
        """
        :return: None
        """
        pass

    def __eq__(self, other):
        return self.name == other.name

    def __str__(self):
        return 'Skill: ' + self.name