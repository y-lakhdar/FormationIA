from RULEngine.Strategy.Strategy import Strategy
from RULEngine.Command.Command import MoveTo

from FormationStrat.Data.BlackBoard import BlackBoard
from FormationStrat.Plays.pQueueLeuLeu import pQueueLeuLeu

class FormationStrategy(Strategy):
    def __init__(self, field, referee, team, opponent_team, is_team_yellow=False):
        Strategy.__init__(self, field, referee, team, opponent_team)
        self.blackboard = BlackBoard(team, opponent_team, field.ball)
        self.blackboard.setCurPlay(pQueueLeuLeu(self.blackboard))

    def on_start(self):
        # On récupère la stratégie en cours
        cur_play = self.blackboard.getCurPlay()

        # On applique STP
        for i, tactic in enumerate(cur_play.getTactics(self.blackboard)):
            tactic.getSkill(i, self.blackboard).act(i, self.blackboard)

        # On utilise le blackboard pour envoyer les commandes
        for i, player in enumerate(self.team.players):
            self._send_command(MoveTo(player, self.team, self.blackboard.getNextPose(i).position))

    def on_halt(self):
        self.on_start() #No referee yet.

    def on_stop(self):
        self.on_start() #No referee yet.
