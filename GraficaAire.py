import matplotlib.pyplot as plt
import numpy as np
import base64
from io import BytesIO

horas = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]

Limite =    [35000,	35000,	35000,	35000,	35000, 35000,
            35000,	35000,	35000,	35000,  35000,	35000,
            35000,	35000,	35000,  35000,	35000,	35000,
            35000,	35000,  35000,	35000,	35000,	35000]

concentraciones = [ 378.05,	366.59,	386.07,	579.68,
                    370.03,	289.84,	277.24,	378.05,
                    382.63,	184.44,	286.40,	186.73,
                    93.94,	92.79,	775.57,	1157.06,
                    1065.41,1126.13,375.76, 92.79,
                    91.65,	91.65,	97.38,	91.65]

horas_np=np.array(horas)
concentraciones_np=np.array(concentraciones)
limite_np=np.array(Limite)
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)

major_ticks_x = np.arange(1, 25, 1)

ax.set_xticks(major_ticks_x)

ax.set_xlim(xmax=25, xmin=0)



#ax.grid(which='both')
plt.bar(horas_np,concentraciones_np,label='Concentración CO (μg/m³ std)')
plt.plot(limite_np,color='orange',label='Límite diario res 2254/2017 (μg/m³ std)')
plt.xlabel('Horas')
plt.ylabel('Concentración CO (μg/m³ std)')
plt.title('Concentración de monóxido de carbono')
plt.legend(loc='upper center')
plt.grid()

#plt.show()


# Crear un objeto BytesIO para almacenar la imagen en memoria
buffer = BytesIO()

# Guardar la gráfica en el objeto BytesIO
plt.savefig(buffer, format='png', dpi=100, bbox_inches='tight')

# Convertir la imagen en base64
base64_img = base64.b64encode(buffer.getvalue()).decode("utf-8")

# Guardar la imagen base64 en un archivo de texto

ruta_imagen="E:\ProyectoAire\FormatosAirePdf\imagenes\GraficaMPLb64_2.txt"

with open(ruta_imagen, "w") as f:
    f.write(base64_img)

plt.close()
