from RULEngine.Game.Team import Team
from RULEngine.Game.Ball import Ball
from RULEngine.Util.Pose import Pose, Position
from FormationStrat.Tactics.TacticBase import TacticBase
from FormationStrat.Skills.SkillBase import SkillBase
from FormationStrat.Plays.PlayBase import PlayBase

__author__ = 'jbecirovski'


class BlackBoard:
    def __init__(self, team, op_team, ball):
        assert isinstance(team, Team)
        assert isinstance(op_team, Team)
        assert isinstance(ball, Ball)
        self.__team = team
        self.__opTeam = op_team
        self.__ball = ball
        self.__data = {'team':[{'tar1':Position(), 'tar2':Position(), 'T':None, 'S':None, 'nP':Pose()} for x in range(6)],
                     'Game':{'P':None, 'Seq':0}}

    # --- Getter/Setter TEAM ---
    def getPose(self, p_id):
        return self.__team.players[p_id].pose
    def getPosition(self, p_id):
        return self.__team.players[p_id].pose.position
    def getOrientation(self, p_id):
        return self.__team.players[p_id].pose.orientation

    # --- Next Pose ---
    def getNextPose(self, p_id):
        return self.__data['team'][p_id]['nP']
    def setNextPose(self, p_id, p_pose):
        assert isinstance(p_pose, Pose)
        self.__data['team'][p_id]['nP'] = p_pose

    # --- Next Target 1 ---
    def getFirstTarget(self, p_id):
        return self.__data['team'][p_id]['tar1']
    def setFirstTarget(self, p_id, p_pst):
        assert isinstance(p_pst, Position)
        self.__data['team'][p_id]['tar1'] = p_pst

    # --- Next Target 2 ---
    def getSecondTarget(self, p_id):
        return self.__data['team'][p_id]['tar2']
    def setSecondTarget(self, p_id, p_pst):
        assert isinstance(p_pst, Position)
        self.__data['team'][p_id]['tar2'] = p_pst

    # --- Tactic ---
    def getTactic(self, p_id):
        return self.__data['team'][p_id]['T']
    def setTactic(self, p_id, p_tactic):
        assert isinstance(p_tactic, TacticBase)
        self.__data['team'][p_id]['T'] = p_tactic

    # --- Skill ---
    def getSkill(self, p_id):
        return self.__data['team'][p_id]['S']
    def setSkill(self, p_id, p_skill):
        assert isinstance(p_skill, SkillBase)
        self.__data['team'][p_id]['S'] = p_skill

    # -- Game --
    def getCurPlay(self):
        return self.__data['Game']['P']
    def setCurPlay(self, p_play):
        assert isinstance(p_play, PlayBase)
        self.__data['Game']['P'] = p_play

    def getCurSequence(self):
        return self.__data['Game']['Seq']
    def setCurSequence(self, i):
        assert isinstance(i, int)
        if not self.getCurSequence() == i:
            self.__data['Game']['Seq'] = i
    def incrSequence(self):
        self.__data['Game']['Seq'] += 1
    def decrSequence(self):
        if not self.getCurSequence() == 0:
            self.__data['Game']['Seq'] -= 1

    # -- Ball ---
    def getBall(self):
        return self.__ball.position


    # --- Getter/Setter opTEAM ---
    def getEnemyPose(self, p_id):
        return self.__opTeam.players[p_id].pose
    def getEnemyPosition(self, p_id):
        return self.__opTeam.players[p_id].pose.position
    def getEnemyOrientation(self, p_id):
        return self.__opTeam.players[p_id].pose.orientation