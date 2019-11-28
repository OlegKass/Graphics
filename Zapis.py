import plotly as pl
import plotly.graph_objects as go
def y(x):
    return (x**2 - 4)/(2*x**2 - 1)
def GG():
    x= -5
    for i in range(1000):
        yield (x+0.01*i, y(x + 0.01 * i))
with open("input.txt", mode="w") as f:
    f.write("x;y\n")
    f.write('\n'.join(';'.join(str(j) for j in i) for i in GG()))

trace = go.Scatter(x = list(i[0] for i in GG()),
                   y = list(i[1] for i in GG()),
                   mode="lines"
                   )
fig = go.Figure(data=[trace])

fig.update_xaxes(title_text='X')
fig.update_yaxes(title_text='Y')

pl.offline.plot(fig,filename='line-mode.html',)