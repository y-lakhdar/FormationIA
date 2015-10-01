from RULEngine.Strategy.Strategy import Strategy

class ExampleStrategy(Strategy):
    def __init__(self, field, referee, team, opponent_team, is_team_yellow=False):
        Strategy.__init__(self, field, referee, team, opponent_team)

    def on_start(self):
        pass
        #Code here

    def on_halt(self):
        self.on_start() #No referee yet.

    def on_stop(self):
        self.on_start() #No referee yet.
