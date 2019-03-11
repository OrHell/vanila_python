from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        # Logo
        self.image('болт.png', 10, 8, 33)
        # Arial bold 15
        self.set_font('Arial', 'B', 15)
        # Move to the right
        self.cell(80)
        # Title
        self.cell(30, 10, 'Деталь:', 1, 0, 'C')
        # Line break
        self.ln(20)


   
pdf = PDF()
pdf.alias_nb_pages()
pdf.add_page()
pdf.set_font('Times', '', 12)

pdf.cell(0, 10, 'Printing line number ' )
pdf.output('tuto2.pdf', 'F')