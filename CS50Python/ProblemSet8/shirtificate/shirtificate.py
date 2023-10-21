from fpdf import FPDF

pdf = FPDF()

def main():
    #Prompt user for thier name
    name = input("Name: ")
    make_pdf(name)

def make_pdf(name):
    #Create PDF: A4(210x297), Portrait Orientation
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()
    pdf.set_margin(0)
    pdf.set_font("helvetica", "B", 40)

    #Add Header
    pdf.cell(0, 50, "CS50 Shirtificate", align="C")
    pdf.ln(20)

    #Add Image
    pdf.image("shirtificate.png", x=0, y=60)

    #Add Users Name to shirt in white text
    pdf.set_font("helvetica", size=25)
    pdf.set_text_color(255,255,255)
    pdf.text(x=75, y=150, txt=f"{name} took CS50")

    #Output fpdf2
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()