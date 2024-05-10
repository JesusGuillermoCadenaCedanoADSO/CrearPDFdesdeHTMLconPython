import asyncio
from pyppeteer import launch
import os
import base64
from PyPDF2 import PdfMerger, PdfReader
import time

inicio=time.time()
ruta_pdf='E:/ProyectoAire/FormatosAirePdf/Plantilla'
ruta_nuevo_pdf='E:/ProyectoAire/FormatosAirePdf/Plantilla/NuevoArhivo.pdf'
ruta_html= 'E:/ProyectoAire/FormatosAirePdf/CODIGO_HTML_b64.html'


async def convertir_html_a_pdf(html_file, pdf_file):
    browser = await launch(headless=True)
    page = await browser.newPage()
    with open(html_file, 'r', encoding='utf-8') as f:
        html_content = f.read()
    await page.setContent(html_content)
    await page.waitForSelector('body')
    await page.pdf({'path': pdf_file, 'format': 'A3','landscape':True,'scale':0.56,})
    await browser.close()


mergeFile = PdfMerger()
for i in range(54):
    ruta_archivo_pdf = ruta_pdf + str(i) + ".pdf"
    asyncio.get_event_loop().run_until_complete(convertir_html_a_pdf(ruta_html, ruta_archivo_pdf))
    bookmark='hoja'+str(i)
    mergeFile.append(PdfReader(ruta_archivo_pdf,'rb'),bookmark)

mergeFile.write("ruta_nuevo_pdf.pdf")
fin=time.time()

tiempo_transcurrido=fin-inicio

print(f"tiempo transcurrido : {tiempo_transcurrido} segundos")
