import io
import asyncio
from pyppeteer import launch
from PyPDF2 import PdfMerger
import time

inicio=time.time()


ruta_pdf='E:/ProyectoAire/FormatosAirePdf/Plantilla'
ruta_nuevo_pdf='E:/ProyectoAire/FormatosAirePdf/Plantilla/NuevoArhivo.pdf'
ruta_html= 'E:/ProyectoAire/FormatosAirePdf/CODIGO_HTML_b64.html'

async def generar_pdf_desde_html(url, page):
    await page.goto(url, {'waitUntil': 'networkidle0', 'timeout': 2500})
    #await page.waitForNavigation({'waitUntil': 'networkidle0', 'timeout': 60})
    return await page.pdf({'format': 'A3','landscape':True,'scale':0.56, 'quality':10})

async def fusionar_pdfs(rutas_pdfs, ruta_pdf_final, nombres_hojas):
    merger = PdfMerger()
    for ruta_pdf, nombre_hoja in zip(rutas_pdfs, nombres_hojas):
        pdf_file=io.BytesIO(ruta_pdf)
        bookmark=nombre_hoja
        merger.append(pdf_file, bookmark)
    with open(ruta_pdf_final, 'wb') as f:
        merger.write(f)

async def crear_pdf_adjuntando_archivos_html(urls_html, ruta_pdf_final, nombres_hojas):
    browser = await launch()
    page = await browser.newPage()
    
    rutas_pdfs = []
    for url in urls_html:
        pdf_data = await generar_pdf_desde_html(url, page)
        rutas_pdfs.append(pdf_data)

    await fusionar_pdfs(rutas_pdfs, ruta_pdf_final, nombres_hojas)
    
    await browser.close()

# Ejemplo de uso
urls_html=[]
nombres_hojas=[]
for i in range(54):
    nombre_hoja="Hoja_"+str(i)
    urls_html.append(ruta_html)
    nombres_hojas.append(nombre_hoja)

ruta_pdf_final = "ruta_nuevo_pdf_v2.pdf"

asyncio.get_event_loop().run_until_complete(crear_pdf_adjuntando_archivos_html(urls_html, ruta_pdf_final, nombres_hojas))

fin=time.time()

tiempo_transcurrido=fin-inicio

print(f"tiempo transcurrido : {tiempo_transcurrido} segundos")