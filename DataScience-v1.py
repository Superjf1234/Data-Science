import pandas as pd

# Ajustar las opciones de visualización
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df1 = pd.read_excel(r"C:\Users\felip\Downloads\data.xls")
df2 = pd.read_csv(r"C:\Users\felip\Downloads\dataCGP.csv")

print(df1)
print(df2)

print(df2.describe())
print(df1.describe())

print(df1.dtypes)
print(df2.dtypes)

print(df1.head(5))
print(df2.head(10))

print(df1.tail(11))
print(df2.tail(8))

print(df2.info())
print(df1.info())

print("---------")

print(df1.isnull().sum())
print(df2.isnull().sum())


df2.rename(columns={"Precio Unitario": "PRECIO"}, inplace=True)
df1.rename(columns={"Horas": "HR", "Explicación": "EXP"}, inplace=True)
df1.rename(
    columns={"Fecha de registro": "FECHA", "Tipo de aviso": "AVISO"}, inplace=True
)

print("--------RENAME----------------")

print(df1)
print(df2)

print("--------DROP-----------------")

df2 = df2.drop(columns=["PRECIO"])

print(df2)
