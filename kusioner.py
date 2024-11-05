import pandas as pd
import numpy as np

def diagnosa(data):
    xl_file = pd.ExcelFile("D:\Salsya's Punya\deployment\tabelkategori.xlsx")

    #daftar jenis kategori
    df_indikator = xl_file.parse("tabelkategori")
    #metadata gejala vs kategori
    df_kategori = xl_file.parse("tabelindikatorvskategori")


    df_responibu = pd.DataFrame([data])

df_indikator.drop("indikator", axis = 1, inplace = True)
df_indikator.drop("Kode indikator", axis = 1, inplace = True)
arr_indikator = np.array(df_indikator)
