from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format = 'A4')
pdf.set_auto_page_break(auto = False, margin = 0)

df = pd.read_csv("topics.csv")

for index,row in df.iterrows():
    pdf.add_page()
    
    #Set the Header for the Master page
    pdf.set_font(family='Times', style='B', size=24)
    # setting text color using RGB color method
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row["Topic"], align = 'L', ln=1)
    # Adding a separating line
    for y in range(20, 285, 10):
        pdf.line(10,y,200,y)   
    # Set the Footer for the Master page
    pdf.ln(265)
    pdf.set_font(family='Times', style='I', size=8)
    pdf.set_text_color(180,180,180)
    pdf.cell(w = 0, h = 10, txt=row["Topic"], align = "R")
    
    for i in range(row["Pages"] - 1):
        pdf.add_page()
        pdf.ln(275)
        # Set the Footer for the Subpages
        pdf.set_font(family='Times', style='I', size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w = 0, h = 10, txt=row["Topic"], align = "R")
        for y in range(20, 285, 10):
            pdf.line(10,y,200,y)
       
    

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