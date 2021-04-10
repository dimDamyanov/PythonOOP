from project.player.player import Player


class Beginner(Player):
    HEALTH_POINTS = 50

    def __init__(self, username: str):
        super().__init__(username, Beginner.HEALTH_POINTS)
