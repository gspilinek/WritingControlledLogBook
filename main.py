# Gerald Spilinek
# 07/16/22
# This code is designed to automate the handwriting of the controlled substance book at Dandurand's Pharmacy

import csv
from fpdf import FPDF


def main():
    pdf = FPDF('L', 'in', 'Letter')

    with open('Drugs.csv') as csv_file:
        csv_reader = csv.reader(csv_file)

        for row in csv_reader: # for each drug
            if row[0] == "Drug Name":
                continue
            pdf.add_page() # make a new page
            pdf.set_font('Times', 'B', 16)
            pdf.cell(3)  # for aligning in 'middle' of page
            pdf.cell(2, 0.5, row[0], align='c')  # drug name
            pdf.cell(0, 0.5, row[1], ln=2)  # drug strength
            pdf.cell(-5)  # realign to left side with a 1-inch margin

            # label column names
            pdf.cell(3, .25, "Label", border=1, align="c")
            pdf.cell(2, .25, "Qty", border=1)
            pdf.cell(2, .25, "Tech / RPH", border=1)
            pdf.cell(3, .25, "Corrections", border=1, ln=2)

            for x in range(12):
                pdf.cell(-7)
                pdf.cell(3, .5, border=1)
                pdf.cell(2, .5, border=1)
                pdf.cell(2, .5, border=1)
                pdf.cell(3, .5, border=1, ln=2)

    pdf.output('Test.pdf', 'F')

if __name__ == '__main__':
    main()
