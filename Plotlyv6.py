import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go

colores = ["#94afe6", "#00d3e8", "#4cda0b"]

df2 = pd.read_csv(r"C:\Users\felip\Downloads\dataCGP.csv")

dftotales = df2[["Producto", "Total"]]
dftotales2 = dftotales.groupby(by=["Producto"]).sum()

print(dftotales2)

dftotales22 = dftotales.groupby(by=["Producto"]).count()
print(dftotales22)

dforigen = df2[["Producto", "Origen"]]
dftotales33 = dforigen.groupby(by=["Origen"]).count()
print(dftotales33)

# Grafico de Barra

x = df2.Producto.unique
y = dftotales.Total

fig = px.bar(df2, x="Producto", y="Total", color=df2.Origen, title="Grafico de Barras")

fig.show()

"Graph objects"

# Crear la gráfica de barras usando plotly.graph_objects
x = df2["Producto"].unique()
y = df2.groupby("Producto")["Total"].sum()

fig_graph_objects = go.Figure(data=go.Bar(x=x, y=y))
fig_graph_objects.update_layout(
    title="Grafico de Barras con Plotly Graph Objects",
    xaxis_title="Categoria de Producto",
    yaxis_title="Total",
)
fig_graph_objects.show()

# Grafico horarizontal - plotply express

x = df2.Producto.unique()
y = dftotales.Total

fig = px.bar(
    df2,
    y="Producto",
    x="Total",
    color=df2.Origen,
    orientation="h",
    title="Grafico Barra Horizontal",
)
fig.show()

# graph objects

x = df2.Producto.unique()
y = dftotales.Total

fig = go.Figure(data=go.Bar(x=y, y=x, orientation="h"))
fig.update_layout(
    title="Grafico de Barras",
    xaxis_title="Valores",
    yaxis_title="Categoria de Producto",
)
fig.show()

"Grafico de Torta o Pie Chart"

labels = df2.Producto.unique()

valores = dftotales2.Total

fig = px.pie(dftotales2, values=valores, names=labels, title="Pie Chart")
fig.show()

# pie chart - graph objects

fig = go.Figure(data=go.Pie(labels=labels, values=valores))
fig.update_layout(title="Pie Chart")
fig.show()

# Histograma

fig = px.histogram(df2, x="Cantidad", color="Origen")
fig.show()

# Histograma - Graph Objetcs

fig = go.Figure(data=go.Histogram(x=df2.Cantidad))
fig.update_layout(title="Histograma", xaxis_title="Valores", yaxis_title="Producto")
fig.show()

# Grafico de Lineas -express

fig = px.line(df2, x="Fecha", y="Total", color="Origen")
fig.show()

# Grafico lineas - Graph Objetcs

fig = go.Figure(data=go.Scatter(x=df2.Fecha, y=df2.Total))
fig.update_layout(title="Grafico de Lineas", xaxis_title="Fecha", yaxis_title="Totales")
fig.show()

# Grafico de Regresion o Dispersion

fig = px.scatter(df2, x="Fecha", y="Total", color="Origen")
fig.show()

# Grafico de Regresion - Graph Objetcs

fig = go.Figure(data=go.Scatter(x=df2.Fecha, y=df2.Total, mode="markers"))
fig.update_layout(
    title="Grafico de Dispersion G", xaxis_title="Fecha", yaxis_title="Producto"
)
fig.show()
