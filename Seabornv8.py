import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df2 = pd.read_csv(r"C:\Users\felip\Downloads\datos_ventas.csv")

print(df2)

# Pie Chart

sns.set_style("darkgrid")
df2.groupby(by="Producto")["Cantidad"].sum().plot(kind="pie", autopct="%1.1f%%")

plt.show()

sns.barplot(
    x="Producto",
    y="Ingresos",
    color="blue",
    palette=[
        "tab:blue",
        "tab:orange",
        "tab:green",
        "tab:red",
        "tab:pink",
        "tab:purple",
    ],
    data=df2,
)

plt.xticks(rotation=45, size=7)
plt.xlabel("Producto de Farmacia", size=12)
plt.ylabel("Ingresos", size=12)

plt.show()


# Grafico de Barra
df2.groupby(["Producto"]).sum().plot(kind="bar")

plt.show()


# Grafico de Dispersion

sns.scatterplot(x="Cantidad", y="Ingresos", data=df2)

plt.show()

# Histograma

sns.histplot(df2.Ingresos)

plt.show()

# Grafico de Lineas

sns.lineplot(data=df2, x="Fecha_Venta", y="Ingresos", color="red")

plt.xticks(rotation=90)

plt.show()
