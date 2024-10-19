print("------Selecion de columnas----------")

import pandas as pd
from IPython.display import display

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df1 = pd.read_excel(r"C:\Users\felip\Downloads\data.xls")
df2 = pd.read_csv(r"C:\Users\felip\Downloads\dataCGP.csv")

# 1ra opcion
# print(df1["Solicita"])

# 2da opcion
print(df1.Solicita)


print("----------SELECCION DE MULTIPLES COLUMNAS--------------")


# se asigna la seleccion de columnas a una nueva variable sin varios la tabla original
df3 = df2[["Cliente", "Total", "Origen"]]

print(df3)


print("-------------------SELECION POR POSICION-----------------------")

print(df3.iloc[0:5])

print("-------------------SELECION POR ETIQUETA-----------------------")

print(df3.loc[0:5])

print("-------------------SELECION POR CONDICION-----------------------")

# print(df3[df3["Total"] > 40])

# Filtrar y mostrar
filtered_df = df3[df3["Total"] > 40]
display(filtered_df)

display(filtered_df.count())
