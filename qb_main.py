import plotly.graph_objects as go
from passing import Quarterbacks

qb = Quarterbacks()
df = qb.df

attempt = qb.object_to_int(stats=df["Att"])
completed = qb.object_to_int(stats=df["Cmp"])
percent = qb.object_to_float()
yards = qb.object_to_int(stats=df["Yds"])
players = qb.get_player_name()
teams = qb.get_team_name()

fig = go.Figure(data=[
    go.Bar(name = "Количество попыток паса", x = players, y = attempt, marker_color = attempt, hovertext = teams, hovertemplate='<br>Имя игрока: %{x}<br>Статистика: %{y}<br>z: %{}<br>Команда: %{hovertext}', customdata=["google.com"]),
    go.Bar(name = "Успешных пасов", x = players, y = completed, marker_color = completed),
    go.Bar(name = "Отношение количества к успешным попыткам", x = players, y = percent, marker_color = percent),
    go.Bar(name = "Общее количество ярдов за сезон", x = players, y = yards, marker_color = yards)
])

fig.update_layout(
    title_text = "Статистика 10 лучших квотербэков 2022",
    barmode = "group", 
    xaxis = {"categoryorder": "total ascending"},
    xaxis_title = "Имя игрока", 
    yaxis_title = "Общая статистика пасовой игры квотербеков",
    hovermode = "closest"
    )


fig.show()

# https://www.youtube.com/watch?v=-_VGq9ee0xE&list=PLlaXam44G_k6de8_NtydvuOWuM7Mf8fmC
# https://github.com/tbryan2/NFL-Next-Gen-Stats/blob/main/NFL-Next-Gen-Stats/NFL-Next-Gen-Stats.ipynb