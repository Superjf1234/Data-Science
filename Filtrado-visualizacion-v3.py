import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import sweetviz as sv

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df1 = pd.read_excel(r"C:\Users\felip\Downloads\data.xls")
df2 = pd.read_csv(r"C:\Users\felip\Downloads\dataCGP.csv")

print(df2)

# 1er ventas onlines y luego ventas físicas
Total_Online = df2[df2.Origen.isin(["Online"])]
VO = sum(Total_Online["Total"])
print("Ventas Online --->", VO)

Total_Fisica = df2[df2.Origen.isin(["Tienda Física"])]
VF = sum(Total_Fisica["Total"])
print("Ventas Fisicas--->", VF)


print("Grafico de Barras - Matplotlib")

x = ["Oline", "Fisica"]
y = [VO, VF]

fig, ax = plt.subplots()

ax.bar(x, y, linewidth=5)

# Añadir título y etiquetas
ax.set_title("Grafico de Barras - Matplotlib")
ax.set_xlabel("Tipo de Venta")
ax.set_ylabel("Ventas")

# Mostrar el gráfico
plt.show()


TotalesOrigen = df2[["Origen", "Total"]]
TotalesOrigen2 = TotalesOrigen.groupby(by=["Origen"]).sum()
print(TotalesOrigen2)

fig, ax = plt.subplots()
valores = TotalesOrigen2.Total
titulosm = df2["Origen"].unique()
colores = ["#3466AF", "#FFCB05"]
ax.bar(x=titulosm, height=valores, color=colores)

ax.set_title("Grafico de Barras - Matplotlib")
ax.set_xlabel("Tipo de Venta")
ax.set_ylabel("Ventas")

plt.show()


# df2.info()

A = cantidad = df2[df2["Origen"] == "Online"]
print(cantidad["Origen"].count())

B = cantidad2 = df2[df2["Origen"] == "Tienda Física"]
print(cantidad2["Origen"].count())

print(f"Total de ventas Online {A}")
print(f"Total de venta Tienda Física {B}")

cantidadO = df2[df2.Origen.isin(["Online"])]
TO = cantidadO["Total"].count()

print("Ventas Onlines --->", TO)

cantidadT = df2[df2.Origen.isin(["Tienda Física"])]
TF = cantidadT["Total"].count()

print("Ventas Tiendas Física --->", TF)

# Valores a utilizar de los Calculos

Titulos = df2["Origen"].unique()
Datos = [TO, TF]
fig, ax = plt.subplots()
explode = [0.1, 0]
ax.pie(Datos, labels=Titulos, explode=explode, autopct="%1.1f%%")

plt.show()

"Productos mas vendidos"

dftotales = df2[["Producto", "Total"]]
dftotales2 = dftotales.groupby(by=["Producto"]).sum()
print(dftotales2)

# Crear el gráfico de tortas con partes separadas y colores personalizados
fig, ax = plt.subplots()

# Define una lista de colores
colors = ["#ff9999", "#66b3ff", "#99ff99", "#ffcc99"]

# El parámetro explode separa las partes del gráfico de tortas
explode = [0.1 for _ in range(len(dftotales2))]
ax.pie(
    dftotales2["Total"],
    labels=dftotales2.index,
    autopct="%1.1f%%",
    startangle=90,
    explode=explode,
    colors=colors,
)
ax.axis("equal")  # Para asegurar que el gráfico sea un círculo

ax.set_title("Distribución de Ventas por Producto")
plt.show()

df22 = df2.groupby(["Producto"])["Total"].transform("sum").unique()

fig, ax = plt.subplots()

labelsP = df2["Producto"].unique()

ax.pie(df22, labels=labelsP, autopct="%1.1f%%")

plt.show()

" SEABORN otra graficas"

# Configuración de la gráfica
sns.relplot(data=df2, x="Cantidad", y="Total", hue="Origen", style="Origen")

# Mostrar la gráfica
plt.show()

# grafico de barra
sns.displot(df2, x="Total")

plt.show()


# grafico de regresion

sns.regplot(x="Total", y="Cantidad", data=df2)

plt.show()


sns.scatterplot(x=df2.Cantidad, y=df2.Total)

plt.show()

print("sweetviz - Report")

# report = sv.analyze(df2)
# report.show_notebook()

# # Generar el reporte de Sweetviz
# # report = sv.analyze(df2)

# # Guardar el reporte en un archivo HTML
# # report.show_html

# # Generar el reporte de Sweetviz
# report = sv.analyze(df2)

# # Guardar el reporte en un archivo HTML
# report.show_html("sweetviz_report.html")

# # Para visualizar en el navegador
# import webbrowser

# webbrowser.open("sweetviz_report.html")


# sweetviz - Report
report = sv.analyze(df2)
report.show_html("sweetviz_report.html")

# Para visualizar en el navegador
import webbrowser

webbrowser.open("sweetviz_report.html")
