import plotly.graph_objects as go
import pandas as pd

df = pd.read_csv("quoterback.csv")
df = df[:10]

yards = df["Yds"]
player = df["Player"]
longest_pass = df["Lng"]

fig = go.Figure(data=[
    go.Bar(name = "Общее количество ярдов на пасе", x = player, y = yards, marker_color = yards),
    go.Bar(name = "Самый длинный успешный розыгрыш", x = player, y = longest_pass, marker_color = longest_pass)
])

fig.update_layout(
    title_text = "Статистика 10 лучших квотербэков 2022",
    barmode = "group", 
    xaxis = {"categoryorder": "total ascending"},
    xaxis_title = "Имя игрока", 
    yaxis_title = "Статистика по ярдам")

fig.show()