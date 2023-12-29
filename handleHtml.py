from bs4 import BeautifulSoup
import glob

files = glob.glob('./dataHtmlMarginAtm/*/*/*')

for file in files:
    with open(file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    soup = BeautifulSoup(html_content, 'html.parser')
    soup.select_one('#postContent > div.style_postInfoAmber__Il5uZ > div.style_infoWrapper__ku1GI.d-flex.align-items-center.style_ph50__VHpPr.style_infoWrapperMargin__assZ3 > div.style_leftCol__HP0Dc.d-flex.caption-normal.justify-content-between > div.style_authorWrapper__G5xMC.style_authorMarginWrapper__G4bvr').decompose()
    soup.select_one('#postContent > div.style_postInfoAmber__Il5uZ > div.style_infoWrapper__ku1GI.d-flex.align-items-center.style_ph50__VHpPr.style_infoWrapperMargin__assZ3 > div.d-flex.align-items-center.caption-normal.style_rightCol__GoKL8.style_hide-mobile__SYD0Y').decompose()
    soup.select_one(
        '#post-content-colCenter > div.style_authorPostWrapper__O3iK_.style_authorInfoMarginATM__q_nrO').decompose()
    with open(file, 'w', encoding='utf-8') as f1:
        f1.write(soup.prettify())
