import pandas as pd

class Information():
    """Информационный класс"""
    def __init__(self) -> None:
        self.URL = "https://www.pro-football-reference.com/years/2022/rushing.htm#rushing"
        self.TOP_TEN = 10
        self.df = pd.read_html(self.URL)[0][:self.TOP_TEN]
        self.yds_per_game = self.df["Rushing"]["Y/G"]
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


class RunningBacks(Information):
    """Класс для работы со статистикой раннин бэков"""
    def __init__(self) -> None:
        super().__init__()


    def get_player_name(self):
        """Получение имени игрока"""
        self.players = self.df["Unnamed: 1_level_0"]["Player"]
        # Имена содержат звоздочку, от которой хотелось бы избавиться; -> Series
        for index, value in enumerate(self.players):
            if self.players.loc[index][-1] == "*":
                self.players.loc[index] = self.players.loc[index][:-1]
        return self.players

    def get_team_name(self):
        """Функция возвращает объект Series, содержащий полное название команд"""
        self.team = self.df["Unnamed: 2_level_0"]["Tm"]
        # Добавляем в список abbreviation полные названия и возращаем teams -> Series
        self.abbreviation = [] 
        for value in self.team.values:
            self.abbreviation.append(self.teams_abbreviation.get(value, "San Francisco 49ers"))
        self.teams = pd.Series(self.abbreviation)
        return self.teams
    
    def object_to_int(self, stats):
        """Изменить значения из Series в int64; исходный тип - object"""
        self.ry = stats
        self.rushing_yds = [int(yard) for yard in self.ry]
        self.rushing_yards = pd.Series(self.rushing_yds)
        return self.rushing_yards
    
    def object_to_float(self):
        """Изменить значения из Series в float64; исходный тип - object"""
        self.per_game = self.df["Rushing"]["Y/G"]
        self.ypg = [float(yard) for yard in self.per_game]
        self.yds_per_game = pd.Series(self.ypg)
        return self.yds_per_game