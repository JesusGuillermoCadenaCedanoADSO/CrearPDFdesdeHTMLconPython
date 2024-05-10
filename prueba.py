from pyppeteer import executablePath

if executablePath():
    print("Chromium encontrado en:", executablePath())
else:
    print("Chromium no encontrado. Asegúrate de tener Pyppeteer y Chromium instalados correctamente.")