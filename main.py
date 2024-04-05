from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format = 'A4')

df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    pdf.set_font(family='Times', style='B', size=24)
    # setting text color using RGB color method
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align = 'L', ln=1)
    # Adding a separating line
    pdf.line(10,21,200,21)
    

pdf.output('output.pdf')

















# # Creating first page
# pdf.add_page()

# # setting font for the first text
# pdf.set_font(family='Times', style='B', size=12)
# # inserting the first text cell
# pdf.cell(w=0, h=12, txt='That is the first PDF page', align = 'L', ln=1, border = 1)
# #setting font for the second text
# pdf.set_font(family='Times', style='B', size=10)
# #inserting the first text cell
# pdf.cell(w=0, h=12, txt='Hello There!', align = 'L', ln=1, border = 1)


# # Creating Second Page 
# pdf.add_page()

# pdf.set_font(family='Times', style='B', size=12)
# pdf.cell(w=0, h=12, txt='That is the first PDF page', align = 'L', ln=1, border = 1)
# pdf.set_font(family='Times', style='B', size=10)
# pdf.cell(w=0, h=12, txt='Hello There!', align = 'L', ln=1, border = 1)

# pdf.output('output.pdf')