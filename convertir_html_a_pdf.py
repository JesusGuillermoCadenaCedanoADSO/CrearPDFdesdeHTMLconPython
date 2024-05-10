import pdfkit
import base64

def imagen_a_base64(ruta_imagen):
    with open(ruta_imagen, "rb") as img_file:
        # Lee los bytes de la imagen
        bytes_imagen = img_file.read()
        # Codifica los bytes en base64
        base64_encoded = base64.b64encode(bytes_imagen)
        # Decodifica los bytes base64 a una cadena (str) en Python 3
        imagen_base64 = base64_encoded.decode("utf-8")
        # Construye la URI de datos
        uri_datos = f"data:image/png;base64,{imagen_base64}"
        return uri_datos

# Ejemplo de uso
ruta_imagen = "E:\ProyectoAire\FormatosAirePdf\img\Logo.png"
uri_datos_imagen = imagen_a_base64(ruta_imagen)
# print(uri_datos_imagen)





ruta_pdf='E:/ProyectoAire/FormatosAirePdf/PlantillaPdfCreada.PDF'

texto_html_head=[
'<!DOCTYPE html>'+
'<html lang="en">'+
'<head>'+
'<meta charset="UTF-8">'+
'<meta http-equiv="X-UA-Compatible" content="IE=edge">'+
'<meta name="viewport" content="width=device-width, initial-scale=1.0">'+
'<title>Document</title>'+
'<style>'+
'.contenedorencabezado {'+
'display: flex;'+
'align-items: center;'+
'border: solid black;'+
'padding:1%;'+
'}'+
'h1 {'+
'text-align: center;'+
'flex:1;'+
'border:solid;'+
'}'+
'.contenedor_listaencabezado{'+
'display:flex;'+
'align-items: center;'+
'}'+
'.listaencabezadotitulos {'+
'list-style: none;'+
'text-align: left;'+
'flex:1;'+
'font-weight: bold;'+
'}'+
'.listaencabezadovalores {'+
'list-style: none;'+
'text-align: center;'+
'flex:1/3;'+
'}'+
'img {'+
'margin-right: 20px;'+
'}'+
'.contenedorproyecto {'+
'display: flex;'+
'align-items: center;'+
'}'+
'.contenedor_listadatosproyecto{'+
'display: flex;'+
'align-items: center;'+
'flex:1;'+
'text-align: left;'+
'}'+
'.listadatosproyectotitulos {'+
'list-style: none;'+
'text-align: left;'+
'flex:1;'+
'font-weight: bold;'+
'}'+
'.listadatosproyectovalores {'+
'list-style: none;'+
'text-align: left;'+
'flex:1;'+
'}'+
'.contenedor_listaplanmuestreo{'+
'display:flex;'+
'align-items: center;'+
'flex:1;'+
'text-align:left;'+
'}'+
'.listadatosmuestreotitulos {'+
'list-style: none;'+
'text-align: left;'+
'flex:1;'+
'font-weight: bold;'+
'}'+
'.listadatosmuestreovalores {'+
'list-style: none;'+
'text-align: left;'+
'flex:1;'+
'}'+
'.contenedor_coordenadasaltura {'+
'display: flex;'+
'align-items: center;'+
'}'+
'.listacoordenadastitulos{'+
'list-style: none;'+
'text-align: left;'+
'flex:1;'+
'font-weight: bold;'+
'}'+
'.listacoordenadasvalores{'+
'list-style: none;'+
'text-align: left;'+
'flex:1;'+
'}'+
'.Altura{'+
'flex:10;'+
'text-align: left;'+
'}'+
'table {'+
'table-layout: fixed;'+
'width: 100%;'+
'border-collapse: collapse;'+
'border: 1px solid black;'+
'}'+
'tbody,th, td{'+
'border-collapse:collapse;'+
'border: 1px solid black;'+
'font-size: small;'+
'}'+
'thead th:nth-child(1) {'+
'width: 10%;'+
'}'+
'thead th:nth-child(2) {'+
'width: 10%;'+
'}'+
'thead th:nth-child(3) {'+
'width: 10%;'+
'}'+
'thead th:nth-child(4) {'+
'width: 10%;'+
'}'+
'thead th:nth-child(5) {'+
'width: 10%;'+
'}'+
'thead th:nth-child(6) {'+
'width: 15%;'+
'}'+
'thead th:nth-child(7) {'+
'width: 15%;'+
'}'+
'thead th:nth-child(8) {'+
'width: 20%;'+
'}'+
'th,'+
'td {'+
'padding: 10px;'+
'}'+
'tbody td {'+
'text-align: center;'+
'}'+
'tfoot{'+
'text-align: left;'+
'}'+
'.contenedor_tablagrafica{'+
'display:flex;'+
'gap: 100px;'+
'}'+
'.contenedor_tablaresultados{'+
'flex:1;'+
'}'+
'.contenedor_grafica{'+
'display: flex;'+
'align-items: top;'+
'justify-content: center;'+
'gap: 200px;'+
'flex:1;'+
'}'+
'.contenedor_profesionales{'+
'display: flex;'+
'flex-wrap: wrap;'+
'height: auto;'+
'}'+
'.flex-item{'+
'width: 25%;'+
'box-sizing: border-box;'+
'border: 1px solid black;'+
'padding: 10px;'+
'}'+
'</style>'+
'</head>'
]

texto_html_body_1=[
'<body>'+
'<div class="contenedorencabezado">'+
'<img src="{uri_datos_imagen}" alt="Logo">'+
'<h1>TRATAMIENTO DE DATOS DE ANALIZADORES AUTOMÁTICOS - CO</h1>'+
'<div class="contenedor_listaencabezado">'+
'<ul class="listaencabezadotitulos">'+
'<li>Fecha</li>'+
'<li>Página</li>'+
'<li>Versión</li>'+
'<li>Código</li>'+
'</ul>'+
'<ul class="listaencabezadovalores">'+
'<li>2021-07-23</li>'+
'<li>1/1</li>'+
'<li>V2</li>'+
'<li>FO-GI-010</li>'+
'</ul>'+
'</div>'+
'</div>'+
'<div class="contenedorproyecto">'+
'<div class="contenedor_listadatosproyecto">'+
'<ul class="listadatosproyectotitulos">'+
'<li>Cliente:</li>'+
'<li>Proyecto:</li>'+
'<li>Ciudad:</li>'+
'</ul>'+
'<ul class="listadatosproyectovalores">'+
'<li>Petróleos Sudamericanos Energy</li>'+
'<li>Campo el difícil</li>'+
'<li>Ariguaní</li>'+
'</ul>'+
'</div>'+
'<div class="contenedor_listaplanmuestreo">'+
'<ul class="listadatosmuestreotitulos">'+
'<li>Plan de muestreo:</li>'+
'<li>Muestreado por:</li>'+
'<li>Punto de muestreo:</li>'+
'<li>Serial:</li>'+
'</ul>'+
'<ul class="listadatosmuestreovalores">'+
'<li>PM-23-0136-V1</li>'+
'<li>Luisa Cruz</li>'+
'<li>Pozo ED32</li>'+
'<li>ND</li>'+
'</ul>'+
'</div>'+
'</div>'+
'<div class="contenedor_coordenadasaltura">'+
'<ul class="listacoordenadastitulos">'+
'<li>Coordenadas (N):</li>'+
'<li>Coordenadas (E):</li>'+
'</ul>'+
'<ul class="listacoordenadasvalores">'+
'<li>2653845</li>'+
'<li>4880928</li>'+
'</ul>'+
'<div class="Altura">'+
'<p><b>Altura (m):</b> 97</p>'+
'</div>'+
'</div>'+
'<div class="contenedor_tablagrafica">'+
'<div class="contenedor_tablaresultados">'
]

texto_html_body_2=[
    '<table>'+
'<thead>'+
'<tr>'+
'<th scope="col">Dato</th>'+
'<th scope="col">Código</th>'+
'<th scope="col">Fecha</th>'+
'<th scope="col">Hora</th>'+
'<th scope="col">Temperatura</th>'+
'<th scope="col">Concentración CO (ppm)</th>'+
'<th scope="col">Concentración CO (&microg/m&sup3 std)</th>'+
'<th scope="col">Límite diario res 2254/2017 (&microg/m&sup3 std)</th>'+
'</tr>'+
'</thead>'+
'<tbody>'+
'<tr>'+
'<td>1</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>00:00:00</td>'+
'<td>ND</td>'+
'<td>0,331</td>'+
'<td>378,05</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>2</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>01:00:00</td>'+
'<td>ND</td>'+
'<td>0,321</td>'+
'<td>366,59</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>3</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>02:00:00</td>'+
'<td>ND</td>'+
'<td>0,338</td>'+
'<td>386,07</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>4</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>03:00:00</td>'+
'<td>ND</td>'+
'<td>0,507</td>'+
'<td>579,68</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>5</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>04:00:00</td>'+
'<td>ND</td>'+
'<td>0,324</td>'+
'<td>370,03</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>6</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>05:00:00</td>'+
'<td>ND</td>'+
'<td>0,254</td>'+
'<td>289,84</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>7</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>06:00:00</td>'+
'<td>ND</td>'+
'<td>0,242</td>'+
'<td>277,24</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>8</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>07:00:00</td>'+
'<td>ND</td>'+
'<td>0,331</td>'+
'<td>378,05</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>9</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>08:00:00</td>'+
'<td>ND</td>'+
'<td>0,335</td>'+
'<td>382,63</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>10</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>09:00:00</td>'+
'<td>ND</td>'+
'<td>0,161</td>'+
'<td>184,44</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>11</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>10:00:00</td>'+
'<td>ND</td>'+
'<td>0,251</td>'+
'<td>286,40</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>12</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>11:00:00</td>'+
'<td>ND</td>'+
'<td>0,163</td>'+
'<td>186,73</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'
]

texto_html_body_3=[
    '<td>13</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>12:00:00</td>'+
'<td>ND</td>'+
'<td>0,082</td>'+
'<td>93,94</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>14</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>13:00:00</td>'+
'<td>ND</td>'+
'<td>0,081</td>'+
'<td>92,79</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>15</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>14:00:00</td>'+
'<td>ND</td>'+
'<td>0,678</td>'+
'<td>775,57</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>16</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>15:00:00</td>'+
'<td>ND</td>'+
'<td>1,012</td>'+
'<td>1157,06</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>17</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>16:00:00</td>'+
'<td>ND</td>'+
'<td>0,932</td>'+
'<td>1065,41</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>18</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>17:00:00</td>'+
'<td>ND</td>'+
'<td>0,985</td>'+
'<td>1126,13</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>19</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>18:00:00</td>'+
'<td>ND</td>'+
'<td>0,329</td>'+
'<td>375,76</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>20</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>19:00:00</td>'+
'<td>ND</td>'+
'<td>0,081</td>'+
'<td>92,79</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>21</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>20:00:00</td>'+
'<td>ND</td>'+
'<td>0,080</td>'+
'<td>91,65</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>22</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>21:00:00</td>'+
'<td>ND</td>'+
'<td>0,080</td>'+
'<td>91,65</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>23</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>22:00:00</td>'+
'<td>ND</td>'+
'<td>0,085</td>'+
'<td>97,38</td>'+
'<td>35000</td>'+
'</tr>'+
'<tr>'+
'<td>24</td>'+
'<td>R23-03073</td>'+
'<td>20/04/2023</td>'+
'<td>23:00:00</td>'+
'<td>ND</td>'+
'<td>0,080</td>'+
'<td>91,65</td>'+
'<td>35000</td>'+
'</tr>'+
'<tfoot>'+
'<tr>'+
'<th scope="row" colspan="6">Mínimo:</th>'+
'<td colspan="2">91,65</td>'+
'</tr>'+
'<tr>'+
'<th scope="row" colspan="6">Máximo:</th>'+
'<td colspan="2">1157,06</td>'+
'</tr>'+
'<tr>'+
'<th scope="row" colspan="6">Promedio:</th>'+
'<td colspan="2">384,06</td>'+
'</tr>'+
'</tfoot>'+
'</tbody>'+
'</table>'
]

texto_html_body_4=[
    '</div>'+
'<div class="contenedor_grafica">'+
'<canvas id="myChart" width="400px" height="400px"></canvas>'+
'</div>'+
'</div>'+
'<div>'+
'<h3>observaciones:</h3>'+
'<p>ND: No determinado</p>'+
'</div>'+
'<div class="contenedor_profesionales">'+
'<div class="flex-item"></div>'+
'<div class="flex-item"><p>NOMBRE</p></div>'+
'<div class="flex-item"><p>CARGO</p></div>'+
'<div class="flex-item"><p>FIRMA</p></div>'+
'<div class="flex-item"><p>ELABORÓ</p></div>'+
'<div class="flex-item"><p>CAROLINA MURCIA</p></div>'+
'<div class="flex-item"><p>PROFESIONAL DE PROYECTOS</p></div>'+
'<div class="flex-item">'+
'<img src="img/FirmaCoordinador.png" alt="firma_coordinador">'+
'</div>'+
'<div class="flex-item"><p>APROBÓ</p></div>'+
'<div class="flex-item"><p>MICHEL RODRIGUEZ</p></div>'+
'<div class="flex-item"><p>DIRECTOR DE PROYECTOS</p></div>'+
'<div class="flex-item">'+
'<img src="img/FirmaDirector.png" alt="firma_director">'+
'</div>'+
'</div>'+
'<script type="text/javascript" src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/2.7.2/Chart.js"></script>'+
'<script src="grafica.js"></script>'+
'</body>'+
'</html>'
]

contenido_html= texto_html_head[0]+ \
                texto_html_body_1[0]+ \
                texto_html_body_2[0]+ \
                texto_html_body_3[0]+ \
                texto_html_body_4[0]

# print(contenido_html)

# def crear_archivo_pdf(descripcion, contenido_html, ruta_pdf,wkhtmltopdf_path=None):
#     options = {
#         'page-size': 'A4',
#         'margin-top': '0.75in',
#         'margin-right': '0.75in',
#         'margin-bottom': '0.75in',
#         'margin-left': '0.75in',
#         'encoding': "UTF-8",
#         'no-outline': None
#     }

#     if wkhtmltopdf_path:
#         options['path'] = wkhtmltopdf_path

#     try:
#         pdfkit.from_string(contenido_html, ruta_pdf, options=options)
#         print(f"Archivo PDF '{descripcion}' creado exitosamente en la ruta '{ruta_pdf}'")
#     except Exception as e:
#         print(f"Error al crear el archivo PDF '{descripcion}': {e}")


options = {
        'page-size': 'A2',
        'orientation':'Landscape',
        'zoom':0.86,
        'margin-top': '0.25in',
        'margin-right': '0.25in',
        'margin-bottom': '0.25in',
        'margin-left': '0.25in',
        'no-outline': None
    }
config = pdfkit.configuration(wkhtmltopdf='C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe')
pdfkit.from_string(contenido_html, ruta_pdf, options=options, configuration=config)

# crear_archivo_pdf("PlantillaPdfCreada", contenido_html, ruta_pdf,)