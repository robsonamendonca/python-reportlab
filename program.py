from reportlab.pdfgen   import canvas

def drawMyRuler(pdf):
    pdf.drawString(100,810, 'x100')
    pdf.drawString(200,810, 'x200')
    pdf.drawString(300,810, 'x300')
    pdf.drawString(400,810, 'x400')
    pdf.drawString(500,810, 'x500')

    pdf.drawString(10,100, 'y100')
    pdf.drawString(10,200, 'y200')
    pdf.drawString(10,300, 'y300')
    pdf.drawString(10,400, 'y400')
    pdf.drawString(10,500, 'y500')
    pdf.drawString(10,600, 'y600')
    pdf.drawString(10,700, 'y700')
    pdf.drawString(10,800, 'y800') 

pdf = canvas.Canvas('olamundo.pdf')
#drawMyRuler(pdf)

# 1) adicionar título ao ficheiro/arquivo
pdf.setTitle('Ayrton Senna')

# 2) adicionar título
# for font in pdf.getAvailableFonts():
#     print(font)

from reportlab.pdfbase.ttfonts  import TTFont
from reportlab.pdfbase          import pdfmetrics

pdfmetrics.registerFont(TTFont('aminhafonte', 'Formula 1.ttf'))

pdf.setFont('aminhafonte', 54)

pdf.setFillColor('black')
pdf.drawCentredString(300, 770, 'Ayrton Senna')
pdf.setFillColor('red')
pdf.drawCentredString(298, 772, 'Ayrton Senna')

# 3) adicionar sub título
from reportlab.lib      import colors

pdf.setFont('Helvetica-Bold', 24)
pdf.setFillColor(colors.black)
pdf.drawCentredString(300, 740, 'Piloto de Fórmula 1')

# 4) adicionar linha horizontal

pdf.setStrokeColor(colors.green)
pdf.setLineWidth(5)
pdf.line(30, 730, 550, 730)

# 5) adicionar parágrafo
from reportlab.platypus import Paragraph

p = Paragraph('Ayrton Senna da Silva ONM • ComRB • CvMA • OME (São Paulo, 21 de março de 1960 — Bolonha, 1 de maio de 1994) foi um piloto brasileiro de Fórmula 1, campeão da categoria três vezes, em 1988, 1990 e 1991. Ele começou sua carreira competindo no kart em 1973 e em "carros de fórmula" em 1981, quando venceu as Fórmulas Ford 1600 e 2000. Em 1983 alcançou o título de campeão do Campeonato Britânico de Fórmula 3 batendo vários recordes.')

p.wrapOn(pdf, 400, 100)
p.drawOn(pdf, 100, 625)

# 6) adicionar imagem

pdf.drawInlineImage(
    'imagem.jpg',
    180, 400,
    250, 250,
    preserveAspectRatio= True
    )

# 7) adicionar hiperlink

pdf.linkURL(
    'https://pt.wikipedia.org/wiki/Ayrton_Senna',  
    (180, 450, 180 + 250, 450 + 150),
    relative=1
)

#pdf.rect(180, 450, 250, 150)

pdf.save()

