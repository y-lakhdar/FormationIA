from RULEngine.Util.Pose import Position, Pose
from FormationStrat.Skills.SkillBase import SkillBase

__author__ = 'jbecirovski'


class sGoToTarget(SkillBase):
    """
    Skill contain:
    + Contain Sequence of Action for each bots
    + Generate Action
    """
    def __init__(self):
        SkillBase.__init__(self, self.__class__.__name__)

    def act(self, p_id, p_bb):
        """
        Next Pose is bot's first target
        :return: None
        """
        orientation = p_bb.getOrientation(p_id)
        p_bb.setSkill(p_id, self)
        tar1 = p_bb.getFirstTarget(p_id)
        p_bb.setNextPose(p_id, Pose(Position(tar1.x, tar1.y), orientation))