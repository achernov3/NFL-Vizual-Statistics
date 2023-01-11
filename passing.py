import pandas as pd

class Quarterbacks():
    """Класс для работы со статистикой квотербэков"""

    def __init__(self) -> None:
        self.QB = "quoterback.csv"
        self.TOP_TEN = 10
        self.df = pd.read_csv(self.QB)[:self.TOP_TEN] # создаю объект DataFrame 10 лучших игроков, с которым будем работать
        self.attempt = self.df["Att"]
        self.completed = self.df["Cmp"]
        self.percent = self.df["Cmp%"]
        self.yards_per_attempt = self.df["Y/A"]
        self.teams_abbreviation = {
                    "ARI": "Arizona Cardinals", 
                    "ATL": "Atlanta Falcons",
                    "BAL": "Baltimore Ravens",
                    "BUF": "Buffalo Bills",
                    "CAR": "Carolina Panthers",
                    "CHI": "Chicago Bears",
                    "CIN": "Cincinnati Bengals", 
                    "CLE": "Cleveland Browns",
                    "DAL": "Dallas Cowboys",
                    "DEN": "Denver Broncos",
                    "DET": "Detroit Lions",
                    "GNB": "Green Bay Packers",
                    "HOU": "Houston Texans",
                    "IND": "Indianapolis Colts",
                    "JAX": "Jacksonville Jaguars",
                    "KAN": "Kansas City Chiefs",
                    "LVR": "Las Vegas Raiders",
                    "LAC": "Los Angeles Chargers",
                    "LAR": "Los Angeles Rams",
                    "MIA": "Miami Dolphins",
                    "MIN": "Minnesota Vikings",
                    "NWE": "New England Patriots",
                    "NOR": "New Orleans Saints",
                    "NYG": "New York Giants",
                    "NYJ": "New York Jets",
                    "PHI": "Philadelphia Eagles",
                    "PIT": "Pittsburgh Steelers",
                    "SFO": "San Francisco 49ers",
                    "SEA": "Seattle Seahawks",
                    "TAM": "Tampa Bay Buccaneers",
                    "TEN": "Tennessee Titans",
                    "WAS": "Washington Commanders"
                    }

    def get_player_name(self):
        """Получение имени игрока"""
        self.players = self.df["Player"]
        # Имена содержат звоздочку, от которой хотелось бы избавиться; -> Series
        for index, value in enumerate(self.players):
            if self.players.loc[index][-1] == "*":
                self.players.loc[index] = self.players.loc[index][:-1]
        return self.players

    def get_team_name(self):
        """Функция возвращает объект Series, содержащий полное название команд"""
        self.team = self.df["Tm"]
        # Добавляем в список abbreviation полные названия и возращаем teams -> Series
        self.abbreviation = [] 
        for value in self.team.values:
            self.abbreviation.append(self.teams_abbreviation[value])
        self.teams = pd.Series(self.abbreviation)
        return self.teams