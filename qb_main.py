import plotly.graph_objects as go
from plotly import offline
from get_statistics import Stats
from create_figure import Histo

qb = Stats("https://www.pro-football-reference.com/years/2022/passing.htm#passing")
df = qb.df

attempt = qb.turn_to_int64(stats=df["Att"])
completed = qb.turn_to_int64(stats=df["Cmp"])
percent = qb.turn_to_float64(per_game = df["Cmp%"])
yards = qb.turn_to_int64(stats=df["Yds"])
players = qb.get_rid_of(df["Player"])
teams = qb.get_team_name(team = df["Tm"])

#histogram = Histo(players=players, teams=teams, attempt=attempt, completed=completed, percent=percent, yards=yards)
#
#fig = histogram.make_histo(players=players, teams=teams, attempt=attempt, completed=completed)
#fig = histogram.layout(players=players, teams=teams, attempt=attempt, completed=completed)

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


#fig.show()
offline.plot(fig, filename = "qb.html")
# https://www.youtube.com/watch?v=-_VGq9ee0xE&list=PLlaXam44G_k6de8_NtydvuOWuM7Mf8fmC
# https://github.com/tbryan2/NFL-Next-Gen-Stats/blob/main/NFL-Next-Gen-Stats/NFL-Next-Gen-Stats.ipynb
# https://www.codingwithricky.com/2019/08/28/easy-django-plotly/
# https://www.kaggle.com/code/kanncaa1/plotly-tutorial-for-beginners