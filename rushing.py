import pandas as pd
from teams_abb import TEAMS_ABBREVIATION

class RunningBacks():
    """Класс для работы со статистикой раннин бэков"""
    def __init__(self) -> None:
        self.URL = "https://www.pro-football-reference.com/years/2022/rushing.htm#rushing"
        self.TOP_TEN = 10
        self.df = pd.read_html(self.URL)[0][:self.TOP_TEN]
        self.yds_per_game = self.df["Rushing"]["Y/G"]

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
            self.abbreviation.append(TEAMS_ABBREVIATION.get(value, "San Francisco 49ers"))
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