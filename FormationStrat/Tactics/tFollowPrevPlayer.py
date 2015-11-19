from RULEngine.Util.Pose import Position

from FormationStrat.Tactics.TacticBase import TacticBase
from FormationStrat.Skills.sGoToTarget import sGoToTarget
from FormationStrat.Skills.sStop import sStop

__author__ = 'jbecirovski'


class tFollowPrevPlayer(TacticBase):
    """
    Tactic contain:
    + Contain Sequence of Skills for each bots
    + Manage Skill attribution
    """
    def __init__(self):
        TacticBase.__init__(self, self.__class__.__name__)
    def getSkill(self, p_id, p_bb):
        """
        :return: Specific Skill
        """
        if p_id == 0:
            p_bb.setFirstTarget(p_id, p_bb.getBall())
        else:
            p_bb.setFirstTarget(p_id, p_bb.getPosition(p_id - 1))

        pst_tar = p_bb.getFirstTarget(p_id)
        pst_bot = p_bb.getPosition(p_id)
        dst = ((pst_tar.x - pst_bot.x)**2 + (pst_tar.y - pst_bot.y)**2)**0.5
        if dst > 500:
            return sGoToTarget()
        else:
            return sStop()