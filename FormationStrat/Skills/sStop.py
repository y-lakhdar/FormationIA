from RULEngine.Util.Pose import Position, Pose
from FormationStrat.Skills.SkillBase import SkillBase

__author__ = 'jbecirovski'


class sStop(SkillBase):
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
        p_bb.setSkill(p_id, self)
        pst = p_bb.getPosition(p_id)
        orientation = p_bb.getOrientation(p_id)
        p_bb.setNextPose(p_id, Pose(Position(pst.x, pst.y), orientation))