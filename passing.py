import pandas as pd
from teams_abb import TEAMS_ABBREVIATION

class Quarterbacks():
    """Класс для работы со статистикой квотербэков
    @position - ссылка на статистику по позициям"""

    def __init__(self, position: str) -> None:
        self.position = position
        self.TOP_TEN = 10
        self.df = pd.read_html(position)[0][:self.TOP_TEN]


    def get_rid_of(self, symbol):
        """Удаление ненужного символа;
        для разных позиций symbol принимает разный параметр:
        @qb_players - symbol = df["Player"] # удаляем * из имен
        @wr_players - symbol = df["Player"] # удаляем * из имен
        @rb_players - symbol = df["Unnamed: 1_level_0"]["Player"] # удаляем * из имен
        @wr_catches_percent - symbol = df["Ctch%"]
        @return -> Series
        """
        self.symbol = symbol
        for index, value in enumerate(self.symbol):
            if self.symbol.loc[index][-1] == "*" or self.symbol.loc[index][-1] == "%":
                self.symbol.loc[index] = self.symbol.loc[index][:-1]
        return self.symbol

    def get_team_name(self, team):
        """Функция возвращает объект Series, содержащий полное название команд
        @qb_teams - team = df["Tm"]
        @wr_teams - team = df["Tm"]
        @rb_teams - team = df["Unnamed: 2_level_0"]["Tm"]
        """
        self.team = team
        # Добавляем в список abbreviation полные названия и возращаем teams -> Series
        self.abbreviation = [] 
        for value in self.team.values:
            self.abbreviation.append(TEAMS_ABBREVIATION.get(value))
        self.teams = pd.Series(self.abbreviation)
        return self.teams

    def turn_to_int64(self, stats):
        """Изменить значения из Series в int64; исходный тип - object"""
        self.convert = [int(yard) for yard in stats]
        self.statistics = pd.Series(self.convert)
        return self.statistics

    def turn_to_float64(self, per_game):
        """Изменить значения из Series в float64; исходный тип - object
        @qb_yds_per_game - per_game = df["Cmp%"]
        @wr_yds_per_game - per_game = df["Y/R"]
        @rb_yds_per_game - per_game = df["Rushing"]["Y/G"]
        """
        self.pg = per_game
        self.convert = [float(yard) for yard in self.pg]
        self.per_game = pd.Series(self.convert)
        return self.per_game