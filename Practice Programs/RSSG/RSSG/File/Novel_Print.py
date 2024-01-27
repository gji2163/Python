from fpdf import FPDF
import io

pdf=FPDF(format='letter', unit='in')


for i in range(2918):
    a = str(i+1)
    
    with io.open('New Folder/'+'0'*(4-len(a))+a+'.txt', 'r') as f:

        pdf.add_page()
        x = f.read()
        x[:x.find('\n')]

        pdf.set_font('Times','B',10.0)
        pdf.cell(1.0,0.0, x[:x.find('\n')].encode('latin-1', 'replace').decode('latin-1'))
        pdf.ln(0.25)
        
        pdf.set_font('Times','',10.0)
        pdf.multi_cell(pdf.w - 2*pdf.l_margin, 0.2, x[x.find('\n')+1:].encode('latin-1', 'replace').decode('latin-1'))
        pdf.ln(0.5)

        f.close()

pdf.output("mygfg.pdf","F")



