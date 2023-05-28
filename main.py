from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("topics.csv")

pdf.set_auto_page_break(auto=False)


for index, row in df.iterrows():

    if row["Pages"] > 0:
        pdf.add_page()
        pdf.set_font(family="Times", style="B", size=20)
        pdf.set_text_color(69, 69, 69)
        pdf.cell(w=60, h=12, txt="Pdf generation:", align="R", ln=0, border=0)
        pdf.cell(w=70, h=12, txt=f"{row['Order']}: {row['Topic']}", align="R", ln=0, border=0)
        pdf.cell(w=65, h=12, txt="- study materials", align="L", ln=1, border=0)

        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(120, 120, 120)
        pdf.cell(w=0, h=12, txt=row["Topic"], align="R")

        for i in range(2, 29):
            pdf.line(x1=10, y1=5+i*10, x2=200, y2=5+i*10)  # 25 35 45..

        for i in range(row["Pages"] - 1):
            pdf.add_page()
            pdf.ln(272)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(120, 120, 120)
            pdf.cell(w=0, h=12, txt=row["Topic"], align="R")
            for j in range(1, 29):
                pdf.line(x1=10, y1=5+j*10, x2=200, y2=5+j*10)

pdf.output("output.pdf")
