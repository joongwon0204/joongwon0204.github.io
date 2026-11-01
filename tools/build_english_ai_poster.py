#!/usr/bin/env python3
"""Rebuild the English poster from the Korean PDF, preserving its data and plots.

Dependencies: reportlab, pypdf, Pillow.
Run from the repository root with python3 tools/build_english_ai_poster.py.
The six distribution plots are extracted, not estimated from their images.
The six survey charts use the counts and final labels in the original poster.
"""
from __future__ import annotations

import io
import logging
from pathlib import Path
from xml.sax.saxutils import escape

from PIL import Image
from pypdf import PdfReader
import reportlab
from reportlab.lib import colors
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.utils import ImageReader
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'assets/신중원_생성형 AI 시대의 불평등 가속화_경제적 상황, AI 접근성, 성과의 관계.pdf'
OUTPUT = ROOT / 'assets/generative-ai-inequality-poster-en.pdf'
W, H = 2384, 3370
MARGIN, GAP = 68, 48
COL = (W - 2 * MARGIN - GAP) / 2
LEFT, RIGHT = MARGIN, MARGIN + COL + GAP
NAVY = colors.HexColor('#173c55')
BLUE = colors.HexColor('#267daf')
INK = colors.HexColor('#17232b')
LIGHT = colors.HexColor('#eaf3f8')
PALETTE = ['#4285f4', '#ea4335', '#fbbc04', '#34a853', '#ff7600', '#46bdc6', '#7ba7f3', '#ed726b', '#ffd653', '#72bf8c', '#ff9a52']

# Embed fonts so the poster renders consistently without system-font fallback.
font_dir = Path(reportlab.__file__).parent / 'fonts'
for name, file in [('PosterSans', 'Vera.ttf'), ('PosterSans-Bold', 'VeraBd.ttf'),
                   ('PosterSans-Italic', 'VeraIt.ttf'), ('PosterSans-BoldItalic', 'VeraBI.ttf')]:
    pdfmetrics.registerFont(TTFont(name, str(font_dir / file)))
pdfmetrics.registerFontFamily('PosterSans', normal='PosterSans', bold='PosterSans-Bold',
                              italic='PosterSans-Italic', boldItalic='PosterSans-BoldItalic')

logging.getLogger('pypdf').setLevel(logging.ERROR)
images = {item.name: item.data for item in PdfReader(SOURCE).pages[0].images}
c = canvas.Canvas(str(OUTPUT), pagesize=(W, H), pageCompression=1, initialFontName='PosterSans')
c.setTitle('Accelerating Inequality in the Era of Generative AI')
c.setAuthor('JoongWon Shin')
c.setSubject('English translation of the May 2025 Korean research poster')

styles = {
    'body': ParagraphStyle('body', fontName='PosterSans', fontSize=30, leading=39, textColor=INK, spaceAfter=13),
    'small': ParagraphStyle('small', fontName='PosterSans', fontSize=26, leading=34, textColor=INK, spaceAfter=10),
    'ref': ParagraphStyle('ref', fontName='PosterSans', fontSize=22, leading=29, textColor=INK, spaceAfter=10),
    'caption': ParagraphStyle('caption', fontName='PosterSans-Bold', fontSize=22, leading=27, textColor=NAVY),
    'legend': ParagraphStyle('legend', fontName='PosterSans', fontSize=18, leading=22, textColor=INK),
}


def para(text: str, x: float, y: float, width: float = COL, style: str = 'body') -> float:
    p = Paragraph(text, styles[style])
    _, height = p.wrap(width, H)
    if y - height < 66:
        raise ValueError(f'Poster text overflows: {text[:60]} (bottom={y-height:.1f})')
    p.drawOn(c, x, y - height)
    return y - height - styles[style].spaceAfter


def section(title: str, x: float, y: float) -> float:
    c.setFillColor(LIGHT)
    c.rect(x, y - 53, COL, 53, fill=1, stroke=0)
    c.setFillColor(NAVY)
    c.setFont('PosterSans-Bold', 34)
    c.drawString(x + 15, y - 38, title)
    return y - 72


def caption(text: str, x: float, y: float, width: float) -> float:
    return para(text, x, y, width, 'caption') - 7


def pie_panel(title: str, labels: list[str], counts: list[int], x: float, y: float,
              width: float, height: float, palette: list[str] | None = None) -> None:
    caption(title, x, y, width)
    palette = palette or PALETTE
    top = y - 64
    chart_height = height - 80
    r = min(width * .205, chart_height * .43)
    cx, cy = x + r + 6, top - chart_height / 2
    total = sum(counts)
    angle = 90
    for i, count in enumerate(counts):
        extent = -360 * count / total
        c.setFillColor(colors.HexColor(palette[i % len(palette)]))
        c.wedge(cx-r, cy-r, cx+r, cy+r, startAng=angle, extent=extent, fill=1, stroke=0)
        angle += extent
    legend_x = x + 2 * r + 32
    legend_w = width - (legend_x-x) - 12
    # Size wrapped legend entries by their measured height, not by item count.
    legend_font = 18
    while True:
        legend_style = ParagraphStyle('pie-legend', parent=styles['legend'],
                                      fontSize=legend_font, leading=legend_font * 1.2)
        entries = []
        for label, count in zip(labels, counts):
            p = Paragraph(f'{escape(label)}: {count} ({count/total:.1%})', legend_style)
            _, ph = p.wrap(legend_w - 25, chart_height)
            entries.append((p, ph))
        gap = 5
        total_height = sum(ph for _, ph in entries) + gap * (len(entries)-1)
        if total_height <= chart_height:
            break
        legend_font -= .5
        if legend_font < 14:
            raise ValueError(f'Legend does not fit: {title}')
    legend_y = top - (chart_height - total_height) / 2
    for i, (p, ph) in enumerate(entries):
        c.setFillColor(colors.HexColor(palette[i % len(palette)]))
        c.rect(legend_x, legend_y - 17, 14, 14, fill=1, stroke=0)
        p.drawOn(c, legend_x + 24, legend_y - ph)
        legend_y -= ph + gap


def reasons_panel(title: str, counts: list[int], x: float, y: float, width: float,
                  height: float, pro: bool = False) -> None:
    caption(title, x, y, width)
    labels = ['Cost', 'Cost + no need', 'No need']
    if pro:
        labels = ['Cost', 'Cost + Free/Plus sufficient', 'Free/Plus sufficient']
    graph_x = x + width * .47
    graph_w = width * .45
    graph_top = y - 88
    row_height = (height - 130) / 3
    limit = 10 if pro else 4
    for tick in range(0, limit + 1, 2 if pro else 1):
        tx = graph_x + graph_w * tick / limit
        c.setStrokeColor(colors.HexColor('#dbe3e8'))
        c.setLineWidth(1)
        c.line(tx, graph_top + 6, tx, graph_top - 3*row_height + 6)
        c.setFillColor(INK)
        c.setFont('PosterSans', 18)
        c.drawCentredString(tx, graph_top - 3*row_height - 20, str(tick))
    for i, (label, count, color) in enumerate(zip(labels, counts, ['#4285f4', '#d968cc', '#fc6a7d'])):
        yy = graph_top - i * row_height
        p = Paragraph(label, styles['legend'])
        _, ph = p.wrap(width * .43, row_height)
        p.drawOn(c, x, yy - ph - 4)
        c.setFillColor(colors.HexColor(color))
        c.rect(graph_x, yy - row_height * .65, graph_w * count / limit, row_height * .55, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('PosterSans-Bold', 18)
        c.drawString(graph_x + graph_w * count / limit + 8, yy - row_height * .45, str(count))
    c.setFillColor(INK)
    c.setFont('PosterSans', 18)
    c.drawCentredString(graph_x + graph_w/2, graph_top - 3*row_height - 48, 'Number of respondents')


def plot_panel(title: str, name: str, x: float, y: float, width: float, height: float,
               spending_axis: bool = False) -> None:
    caption(title, x, y, width)
    data = images[name]
    image = Image.open(io.BytesIO(data))
    scale = min(width / image.width, (height - 62) / image.height)
    iw, ih = image.width * scale, image.height * scale
    ix, iy = x + (width - iw)/2, y - 64 - ih
    c.drawImage(ImageReader(image), ix, iy, iw, ih)
    if spending_axis:
        # The final Korean poster overlays this same correction on its R plot.
        c.setFillColor(colors.white)
        c.rect(ix, iy + ih*.30, iw*.047, ih*.41, fill=1, stroke=0)
        c.saveState()
        c.translate(ix + iw*.023, iy + ih*.505)
        c.rotate(90)
        c.setFillColor(colors.black)
        c.setFont('PosterSans', 8)
        c.drawCentredString(0, 0, 'Monthly spending')
        c.restoreState()


# Header: the title, author, and affiliation preserve the original attribution.
c.setFillColor(NAVY)
c.rect(0, H-26, W, 26, fill=1, stroke=0)
c.setFont('PosterSans-Bold', 64)
c.drawCentredString(W/2, H-116, 'Accelerating Inequality in the Era of Generative AI')
c.setFont('PosterSans', 36)
c.drawCentredString(W/2, H-178, 'Economic circumstances, AI access, and academic performance')
c.setFont('PosterSans-Bold', 30)
c.drawCentredString(W/2, H-238, 'JoongWon Shin')
c.setFont('PosterSans', 27)
c.drawCentredString(W/2, H-280, 'Department of Computer Science and Engineering, Seoul National University')
c.setStrokeColor(BLUE)
c.setLineWidth(3)
c.line(MARGIN, H-320, W-MARGIN, H-320)
TOP = H-354

# Left column.
y = section('Introduction', LEFT, TOP)
intro = [
    'The arrival of ChatGPT in November 2022 brought generative AI into widespread use. OpenAI subsequently introduced Plus ($20/month) and Pro ($200/month), differentiating GPT performance and access by price. If AI access depends on financial resources, this may deepen information gaps and disparities in learning outcomes.',
    'Prior research has found a significant association between income and experience using generative AI (Lee and Lee, 2023, pp. 377-394). Socioeconomic status also affects AI literacy - understanding AI principles and limitations and using AI effectively - which is related to ChatGPT activities and academic outcomes (Zhang, Rice, and Wang, 2024). These studies show differences in AI use and awareness by economic circumstances, but do not account for economic differences in access to paid models and outcomes related to model performance.',
    'This study examines whether economic circumstances are associated with AI use and paid subscriptions, and how subscription-related differences in model performance relate to academic performance. It focuses on economic circumstances, AI access (paid GPT subscriptions), and academic achievement to examine the implications of price-based access.'
]
for text in intro:
    y = para(text, LEFT, y)
y = section('Methods', LEFT, y-10)
methods = [
    'A Google Forms survey of SNU undergraduates was conducted from <b>May 4 to May 15, 2025</b>, collecting information on economic circumstances, GPT subscriptions, and GPA.',
    '<b>Survey items.</b> College affiliation was recorded because GPA distributions and GPT purposes and usage patterns differ across colleges. Monthly average spending was used as an indicator of economic circumstances. Other items covered GPT use, Plus/Pro subscriptions, reasons for not subscribing, and GPA for the preceding semester (4.3 scale).',
    '<b>Analysis sample.</b> Of <b>43 respondents</b>, <b>18 were from the College of Engineering</b>. Every other college had five or fewer respondents. To improve comparability and consistency, subsequent analysis focused on the 18 engineering respondents.',
    'Survey items and the distributions of spending and GPA by subscription status were visualized using Excel and RStudio. Variance tests and independent two-sample tests were conducted (SNU Department of Statistics, 2025). Given the small, exploratory sample, the significance level was set at <b>alpha = 0.15</b>, rather than the conventional 0.05.'
]
for text in methods:
    y = para(text, LEFT, y)
y = section('Results | Survey profile', LEFT, y-10)
half = (COL-28)/2
row_h = 363
pie_panel('Fig. 1 | Respondents by college (n=43)',
          ['Business', 'Engineering', 'Agriculture & Life Sciences', 'Education', 'Social Sciences',
           'Veterinary Medicine', 'Pharmacy', 'Music', 'Humanities', 'Natural Sciences', 'Undergraduate Studies / Liberal Studies'],
          [1,18,5,2,6,1,3,1,2,2,2], LEFT, y, half, row_h)
pie_panel('Fig. 2 | GPT usage frequency (n=18)',
          ['4-5 times/week', 'Almost daily', 'Rarely', '3-4 times/week', '1-2 times/week'],
          [5,10,1,1,1], LEFT+half+28, y, half, row_h)
y -= row_h + 16
y = para('Except for Fig. 1, all results concern the 18 engineering respondents.', LEFT, y, COL, 'small')
pie_panel('Fig. 3 | GPT Plus subscription (n=18)',
          ['No', 'Account sharing', 'Yes'], [10,1,7], LEFT, y, half, 330,
          ['#4285f4','#ea4335','#fbbc04'])
reasons_panel('Fig. 4 | Reasons for not subscribing to Plus (n=10)',
              [4,4,2], LEFT+half+28, y, half, 330)
y -= 346
y = para('"Yes" and "Account sharing" form the GPT Plus group; "No" forms GPT Free.', LEFT, y, COL, 'small')
left_bottom = y

# Right column, continuing the results.
y = section('Results | Access and outcomes', RIGHT, TOP)
pie_panel('Fig. 5 | GPT Pro subscription (n=18)', ['No'], [18], RIGHT, y, half, 305, ['#4285f4'])
reasons_panel('Fig. 6 | Reasons for not subscribing to Pro (n=18)',
              [9,4,5], RIGHT+half+28, y, half, 305, pro=True)
y -= 323
y = para('No respondents subscribed to Pro, so the spending and GPA analyses compare Plus and Free only.', RIGHT, y, COL, 'small')
pw = (COL-28)/3
ph = 370
for j, (label, name) in enumerate([
    ('Fig. 7 | Spending: box plot', 'Im9.png'),
    ('Fig. 8 | Spending: histogram', 'Im12.png'),
    ('Fig. 9 | Spending: kernel density', 'Im10.png')
]):
    plot_panel(label, name, RIGHT+j*(pw+14), y, pw, ph, spending_axis=(j==0))
y -= ph + 7
y = para('Monthly spending is expressed in KRW 10,000. Welch\'s one-sided t-test for higher mean spending among Plus users: <b>t = 1.2149, df = 11.779, p = 0.1241</b>. Variance test: <b>F = 2.2126, df1 = 7, df2 = 9, p = 0.2652</b>.', RIGHT, y, COL, 'small')
for j, (label, name) in enumerate([
    ('Fig. 10 | GPA: box plot', 'Im6.png'),
    ('Fig. 11 | GPA: histogram', 'Im8.png'),
    ('Fig. 12 | GPA: kernel density', 'Im7.png')
]):
    plot_panel(label, name, RIGHT+j*(pw+14), y, pw, ph)
y -= ph + 7
y = para('GPA is on a 4.3 scale. Welch\'s two-sided t-test for different mean GPAs: <b>t = -0.5178, df = 10.845, p = 0.615</b>. Variance test: <b>F = 2.8283, df1 = 7, df2 = 9, p = 0.1488</b>.', RIGHT, y, COL, 'small')
y = section('Discussion', RIGHT, y-4)
discussion = [
    'The following discussion concerns engineering respondents. All respondents used GPT, and about 88.8% reported using it at least three to four times a week, indicating widespread use.',
    'About <b>44.4%</b> subscribed to Plus, including account sharing. Among non-subscribers, cost (80%) was cited more often than lack of perceived need (60%). No one subscribed to Pro; cost (72.2%) was again more common than lack of perceived need (50%). Economic circumstances may therefore be a barrier to generative AI access.',
    'For monthly spending, the Plus group\'s interquartile range (about 60-120) was visibly wider than the Free group\'s (about 30-70). The mean comparison (p = 0.1241) was not significant at 5%, but was significant at the exploratory 15% level used here, suggesting an association between economic circumstances and paid AI subscriptions.',
    'Mean GPAs were not clearly different in Figs. 10-12; the mean comparison (p = 0.615) was not significant even at 15%. The Plus group showed a bimodal and more dispersed grade distribution. GPT usage patterns, dependence on AI, and other factors may be related to these differences. The variance test (p = 0.1488) was not significant at 5%, but suggested a possible difference at 15%. A paid subscription alone does not directly translate into higher grades; appropriate usage patterns and levels of dependence may be relevant to positive outcomes.',
    'Generative AI pricing may deepen economic disparities in information access and outcomes. AI-based education and related policy should consider measures to address these inequalities.',
    '<b>Limitations.</b> Analysis was restricted to 18 engineering students because sufficient samples were not obtained from other colleges. Larger samples spanning diverse colleges are needed for more generalizable findings.'
]
for text in discussion:
    y = para(text, RIGHT, y, COL, 'small')
y = section('References', RIGHT, y-4)
references = [
    'Department of Statistics, College of Natural Sciences, Seoul National University. 2025. <i>General Statistics</i>. Seoul: Hanbit Academy. [Korean; title translated.]',
    'Lee, Hae-su, and Lee, Mo-ran. 2023. "Who Uses Generative AI? Focusing on Sociodemographic Variables, Digital Literacy, and Perceptions of Digital Transformation." <i>Information Systems Review</i> 25(3): 377-394. [Korean; title translated.]',
    'Zhang, C. (Xinyi), Rice, R. E., and Wang, L. H. 2024. "College students\' literacy, ChatGPT activities, educational outcomes, and trust from a digital divide perspective." <i>New Media &amp; Society</i>. doi:10.1177/14614448241301741. Accessed March 30, 2025.'
]
for text in references:
    y = para(text, RIGHT, y, COL, 'ref')
right_bottom = y
c.setStrokeColor(colors.HexColor('#bacbd6'))
c.setLineWidth(1)
c.line(MARGIN, 57, W-MARGIN, 57)
c.setFillColor(NAVY)
c.setFont('PosterSans', 20)
c.drawString(MARGIN, 28, 'Research poster | May 2025 | English version')
c.drawRightString(W-MARGIN, 28, 'Survey figures and statistical results retained from the Korean original')
c.showPage()
c.save()
print(f'Created {OUTPUT} (A0 portrait, one page); column bottoms: {left_bottom:.1f}, {right_bottom:.1f} pt')
