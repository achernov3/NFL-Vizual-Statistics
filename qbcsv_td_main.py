import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("quoterback.csv")
df = df[:10]

touchdowns = df["TD"]
player = df["Player"]
percent_of_tds = df["TD%"]

fig = go.Figure(data=[
    go.Bar(name = "Количество тачдаунов", x = player, y = touchdowns, marker_color = touchdowns),
    go.Bar(name = "Процент тачдаунов", x = player, y = percent_of_tds, marker_color = percent_of_tds)
])

fig.update_layout(
    title_text = "Статистика 10 лучших квотербэков 2022",
    barmode = "group", 
    xaxis = {"categoryorder": "total ascending"},
    xaxis_title = "Имя игрока", 
    yaxis_title = "Статистика тачдаунов")

fig.show()