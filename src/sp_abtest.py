import pandas as pd

def exploracion_df_abtest (df, col_control):
    for categoria in df[col_control].unique():
        df_filtrado = df[df[col_control]== categoria]
        print(f'Los principales estadísticos de las categorias para el grupo {categoria} son;')
        display(df_filtrado.describe(include=['O','category']).T)
        print(f'Los principales estadísticos de las numércia para el grupo {categoria} son;')
        display(df_filtrado.describe().T)