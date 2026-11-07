from player import Player
from statistics_service import StatisticsService


class PlayerReaderStub:
    def __init__(self):
        self._players = [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri", "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89),
        ]

    def get_players(self):
        return self._players


def create_service():
    return StatisticsService(PlayerReaderStub())


def test_search_returns_player_matching_name():
    service = create_service()

    assert service.search("Gretzky").name == "Gretzky"


def test_search_returns_none_when_no_player_matches():
    service = create_service()

    assert service.search("Unknown") is None


def test_team_returns_players_from_requested_team():
    service = create_service()

    assert [player.name for player in service.team("EDM")] == [
        "Semenko",
        "Kurri",
        "Gretzky",
    ]


def test_top_returns_requested_number_in_descending_points_order():
    service = create_service()

    assert [player.name for player in service.top(2)] == ["Gretzky", "Lemieux"]


