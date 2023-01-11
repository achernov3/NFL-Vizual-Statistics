import plotly.graph_objects as go
from rushing import RunningBacks


rb = RunningBacks()
df = rb.df

rushing_yds = rb.object_to_int(stats=df["Rushing"]["Yds"])
rushing_tds = rb.object_to_int(stats=df["Rushing"]["TD"])
yds_per_game = rb.object_to_float()
first_downs = rb.object_to_int(stats=df["Rushing"]["1D"])
players = rb.get_player_name()
teams = rb.get_team_name()

fig = go.Figure(data=[
    go.Bar(name = "Среднее количество ярдов за игру", x = players, y = yds_per_game, hovertext = teams, hovertemplate='<br>Имя игрока: %{x}<br>Статистика: %{y}<br>z: %{}<br>Команда: %{hovertext}', customdata=["google.com"]),
    go.Bar(name = "Количество первых даунов", x = players, y = first_downs),
    go.Bar(name = "Количество выносных тачдаунов", x = players, y = rushing_tds),
    go.Bar(name = "Общее количество выносных ярдов", x = players, y = rushing_yds)
])
#
fig.update_layout(
    title_text = "Статистика 10 лучших раннин бэков 2022",
    barmode = "group", 
    xaxis = {"categoryorder": "total ascending"},
    xaxis_title = "Имя игрока", 
    yaxis_title = "Общая статистика выносной игры",
    hovermode = "closest"
    )


fig.show()