from fpdf import FPDF



class Shirt():


    @classmethod
    def create_pdf(cls, name):
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()
        pdf.set_font("helvetica", size=50)
        pdf.text(x=45, y=40, txt="CS50 Shirtificate")
        pdf.image("shirtificate.png", x=30, y=100, w=150, h=180)
        pdf.set_font("helvetica", size=25)
        pdf.set_text_color(255)
        pdf.text(x=65, y=180, txt=name + " took CS50")
        pdf.output("shirtificate.pdf")



def main():
    shirt = Shirt()
    shirt.create_pdf(input("Name: "))

if __name__ == "__main__":
    main()