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

pdf = FPDF()
pdf.add_page()
pdf.set_font('Arial', 'B', 16)
pdf.cell(40, 10, 'Hello World!')
pdf.output('tuto1.pdf', 'F')
def makepdf(count, fileName):
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
    # pdf.add_page()
    # pdf.image(f'site_stats_{state_code}_{district_code}.png',5, 10, WIDTH-10)
    # pdf.image(f'genderwise_district_{district_code}_{state_code}.png',5, 120, WIDTH-10)
    # pdf.add_page()
    # pdf.image(f'dosewise_district_{state_code}_{district_code}.png',5, 10, WIDTH-10)
    # pdf.image(f'diff_vaccine_stats_{state_code}_{district_code}.png',5, 120, WIDTH-10)
    # pdf.add_page()
    # pdf.image(f'agewise_district_{district_code}_{state_code}.png',5, 10, WIDTH-10)
    # pdf.image(f'session_site_changes_{district_code}_{state_code}_{session_site_id}.png',5, 120, WIDTH-10)
    # pdf.add_page()
    # pdf.image(f'datatable_{state_code}_{district_code}_{session_site_id}.png',5,10, 200)
    # pdf.output(f'State_{state_code}_district_{district_code}_session_site_{session_site_id}' + '.pdf')
    for i in range(count):
        pdf.add_page()
        pdf.image(f'plots/{i}.png',5, 120, WIDTH-10)
    pdf.output(f'Analysis Report for {fileName}' + '.pdf')

makepdf(count, 'test.csv')