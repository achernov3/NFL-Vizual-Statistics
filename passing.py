import pandas as pd
from teams_abb import TEAMS_ABBREVIATION

class Quarterbacks():
    """Класс для работы со статистикой квотербэков"""

    def __init__(self) -> None:
        self.QB = "quoterback.csv"
        self.TOP_TEN = 10
        #self.df = pd.read_csv(self.QB)[:self.TOP_TEN] # создаю объект DataFrame 10 лучших игроков, с которым будем работать
        self.df = pd.read_html("https://www.pro-football-reference.com/years/2022/passing.htm#passing")[0][:self.TOP_TEN]


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
            self.abbreviation.append(TEAMS_ABBREVIATION.get(value))
        self.teams = pd.Series(self.abbreviation)
        return self.teams

    def object_to_int(self, stats):
        """Изменить значения из Series в int64; исходный тип - object"""
        self.stat = [int(yard) for yard in stats]
        self.statistics = pd.Series(self.stat)
        return self.statistics

    def object_to_float(self):
        """Изменить значения из Series в float64; исходный тип - object"""
        self.cmp = self.df["Cmp%"]
        self.cmp_per = [float(yard) for yard in self.cmp]
        self.completed_percent = pd.Series(self.cmp_per)
        return self.completed_percent