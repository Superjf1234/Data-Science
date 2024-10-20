import pandas as pd
import sweetviz as sv
from autoviz.AutoViz_Class import AutoViz_Class
import webbrowser
import os

# from dataprep.eda import create_report

pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

df1 = pd.read_excel(r"C:\Users\felip\Downloads\data.xls")
df2 = pd.read_csv(r"C:\Users\felip\Downloads\dataCGP.csv")

reporte = sv.analyze(df2, target_feat="Total")

reporte.show_html("sweetviz_report.html")

# Para visualizar en el navegador
import webbrowser

webbrowser.open("sweetviz_report.html")

# dataprep

# create_report(df2).show_browser()

# autoviz

# Crear instancia de AutoViz

# AV = AutoViz_Class()

# Visualizar el archivo CSV y guardar en HTML
# df_av = AV.AutoViz(
#     "dataCGP.csv",
#     chart_format="html",
#     save_plot_dir="AutoViz_Plots",
# )

# Abre el archivo HTML generado
# webbrowser.open("AutoViz_Plots/AutoViz_Visualization.html")

# AV = AutoViz_Class()

# df_av = AV.AutoViz(df2)

# Crear instancia de AutoViz
# AV = AutoViz_Class()

# Visualizar el DataFrame y guardar en HTML con un nombre personalizado
# df_av = AV.AutoViz(df2)

# Abre el archivo HTML generado en el navegador
# webbrowser.open("AutoViz_Plots/mi_grafico_autoviz.html")

"-----------------"

from autoviz.AutoViz_Class import AutoViz_Class
import pandas as pd
import webbrowser
import os

# Crear instancia de AutoViz
AV = AutoViz_Class()

# Visualizar el DataFrame y guardar en HTML
df_av = AV.AutoViz(
    r"C:Users\felip\OneDrive\Documentos\curso-py\.venv\DataScience\dataCGP.csv",
    chart_format="html",
    save_plot_dir=r"C:\Users\felip\OneDrive\Documentos\curso-py\AutoViz_Plots\AutoViz",
)

# Mover y renombrar el archivo generado
os.rename(
    r"C:\Users\felip\OneDrive\Documentos\curso-py\AutoViz_Plots\AutoViz\AutoViz_Visualization.html",
    r"C:\Users\felip\OneDrive\Documentos\curso-py\AutoViz_Plots\AutoViz\mi_reporte_autoviz.html",
)

# Abrir el archivo HTML generado en el navegador
webbrowser.open(
    r"C:\Users\felip\OneDrive\Documentos\curso-py\AutoViz_Plots\AutoViz\mi_reporte_autoviz.html"
)
