import plotly.graph_objects as go
from get_statistics import Stats

wr = Stats(position = "https://www.pro-football-reference.com/years/2022/receiving.htm")
df = wr.df

# Информация об игроке и команде
players = wr.get_rid_of(symbol = df["Player"])
teams = wr.get_team_name(team = df["Tm"])

# Собираем статистику
yards = wr.turn_to_int64(df["Yds"])
yards_per_reception = wr.turn_to_float64(per_game = df["Y/R"])
yards_per_game = wr.turn_to_float64(per_game = df["Y/G"])
receiving_tds = wr.turn_to_int64(stats = df["TD"])

fig = go.Figure(data=[
    go.Bar(name = "Количество ярдов за сезон", x = players, y = yards, marker_color = yards, hovertext = teams, hovertemplate='<br>Имя игрока: %{x}<br>Статистика: %{y}<br>z: %{}<br>Команда: %{hovertext}', customdata=["google.com"]),
    go.Bar(name = "Среднее количество ярдов за прием", x = players, y = yards_per_reception, marker_color = yards_per_reception),
    go.Bar(name = "Среднее количество ярдов за игру", x = players, y = yards_per_game, marker_color = yards_per_game),
    go.Bar(name = "Количество тачдаунов на приеме", x = players, y = receiving_tds, marker_color = receiving_tds)
])

fig.update_layout(
    title_text = "Статистика 10 лучших уайд ресиверов 2022",
    barmode = "group", 
    xaxis = {"categoryorder": "total ascending"},
    xaxis_title = "Имя игрока", 
    yaxis_title = "Общая статистика игры уайд ресиверов",
    hovermode = "closest"
    )


fig.show()