import pandas as pd
import matplotlib.pyplot as plt

colores = ["#94afe6", "#00d3e8", "#4cda0b"]

df2 = pd.read_csv(r"C:\Users\felip\Downloads\dataCGP.csv")

# filtros por producto

dftotales = df2[["Producto", "Total"]]
dftotales2 = dftotales.groupby(by=["Producto"]).sum()
print(dftotales2)

dftotales = df2[["Producto", "Total"]]
dftotales3 = dftotales.groupby(by=["Producto"]).count()
print(dftotales3)

dftotales = df2[["Producto", "Origen"]]
dftotales4 = dftotales.groupby(by="Origen").count()
print(dftotales4)

# Graficos de Barra

labelP = df2["Origen"].unique()
plt.bar(labelP, dftotales4.Producto, color=colores)

plt.xlabel("Origen")
plt.ylabel("Cantidad")
plt.title("Grafico de Barras")
plt.show()

df2.groupby("Origen").size().plot(kind="bar", color=colores)

# Mostrar la gráfica en una nueva ventana
plt.title("Distribución de Origen")
plt.xlabel("Origen")
plt.ylabel("Cantidad")
plt.show()

# grafico horizontal

labelsP = df2["Origen"].unique()

plt.barh(labelsP, dftotales4.Producto, color=colores)
plt.xlabel("Cantidad")
plt.ylabel("Origen")
plt.title("Grafico Barra Horizontal")
plt.show()

# Grafico de Dispersion

dfcantidad = df2[["Cantidad", "Total"]]

plt.scatter(dfcantidad.Cantidad, dfcantidad.Total)
plt.xlabel("Cantidad")
plt.ylabel("Total")
plt.title("Grafico Dispersion")

plt.show()

# Histograma

plt.hist(df2.Cantidad, df2.Total.max())
plt.xlabel("Cantidad")
plt.ylabel("Total")
plt.title("Histograma Cantidad vs Total")

plt.show()

# Grafico de torta

df2.groupby("Origen").size().plot(kind="pie", autopct="%1.1f%%")

plt.show()

labels = df2.Origen.unique()
sizes = dftotales4.Producto

plt.pie(sizes, labels=labels, autopct="%1.1f%%")
plt.title("Grafico de Torta")
plt.show()

# graficos de lineas

x = df2.Fecha
y = df2.Total

plt.plot(x, y)

plt.xlabel("Fecha")
plt.ylabel("Totales")
plt.title("Grafico Lineas")
plt.xticks(rotation=90)
plt.show()


df2.plot(x="Fecha", y="Total", kind="line")

plt.show()
