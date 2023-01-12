import plotly.graph_objects as go

class Histo():
    """Класс построения гистограмм, отображающих статистику"""
    def __init__(self, players, teams, attempt, completed, percent, yards) -> None:
        self.qb_description =  {
            "stats_desc": ["Количество попыток паса", "Успешных пасов", "Отношение количества к успешным попыткам", "Общее количество ярдов за сезон"],
            "title": "Статистика 10 лучших квотербэков 2022",
            "yaxis": "Общая статистика пасовой игры квотербеков"
            }
        self.players = players
        self.teams = teams
        self.attempt = attempt
        self.completed = completed
        self.percent = percent
        self.yards = yards

    def make_histo(self, players, teams, attempt, completed):
        fig = go.Figure(data=[
    go.Bar(name = "Количество попыток паса", x = players, y = attempt, marker_color = attempt, hovertext = teams, hovertemplate='<br>Имя игрока: %{x}<br>Статистика: %{y}<br>z: %{}<br>Команда: %{hovertext}', customdata=["google.com"]),
    go.Bar(name = "Успешных пасов", x = players, y = completed, marker_color = completed)
    ])
        return fig

    def layout(self, players, teams, attempt, completed):
        fig = self.make_histo(players, teams, attempt, completed)
        fig.update_layout(
            title_text = "Статистика 10 лучших квотербэков 2022",
            barmode = "group", 
            xaxis = {"categoryorder": "total ascending"},
            xaxis_title = "Имя игрока", 
            yaxis_title = "Общая статистика пасовой игры квотербеков",
            hovermode = "closest"
            )
        return fig