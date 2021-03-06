from re import I
import pandas as pd
import io
import matplotlib.pyplot as plt
import datetime

global count
count = 0
path = 'test.csv'
df = pd.read_csv(path)
buffer = io.StringIO()
df.info(buf=buffer)
df.describe().to_csv("my_description.csv")
s = buffer.getvalue()
column_names = [*df]
with open("df_info.txt", "w", encoding="utf-8") as f:
    f.write(s)

def plot(col):
    global count
    time = datetime.datetime.now()
    file_name = str(time)
    fig, ax = plt.subplots()
    ax.plot(col)
    plt.savefig(f'plots/{count}.png')
    count+=1

df.apply(plot)

###################################################################################
from fpdf import FPDF

def makepdf(count, fileName, column_names):
    WIDTH = 210
    HEIGHT = 297
    pdf = FPDF()
    pdf.add_page()
    pdf.ln(60)
    pdf.set_font('Arial', 'B', 14)
    pdf.write(25, f'Analysis for {fileName}')
    pdf.ln(20)
    pdf.set_font('Arial', 'B', 12)
    pdf.write(5, '''This report analyzes the following:
              - Column Distribution
              - Column Plots
              ''')
    pdf.ln(40)
    for i in range(count):
        pdf.add_page()
        pdf.write(5, f'Plot for Column {column_names[i]}')
        pdf.image(f'plots/{i}.png',20, 20, WIDTH-10)
    pdf.output(f'Analysis Report for {fileName}' + '.pdf')

makepdf(count, 'test.csv', column_names)