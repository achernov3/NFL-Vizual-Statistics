import plotly.graph_objects as go
from passing import Quarterbacks


rb = Quarterbacks("https://www.pro-football-reference.com/years/2022/rushing.htm#rushing")
df = rb.df

rushing_yds = rb.turn_to_int64(stats = df["Rushing"]["Yds"])
rushing_tds = rb.turn_to_int64(stats = df["Rushing"]["TD"])
yds_per_game = rb.turn_to_float64(per_game = df["Rushing"]["Y/G"])
first_downs = rb.turn_to_int64(stats = df["Rushing"]["1D"])
players = rb.get_rid_of(symbol = df["Unnamed: 1_level_0"]["Player"])
teams = rb.get_team_name(team = df["Unnamed: 2_level_0"]["Tm"])

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