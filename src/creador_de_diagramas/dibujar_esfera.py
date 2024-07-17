import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

"""

ARCHIVO FUNCIONA EN GOOGLE COLAB, AQUÍ NO 
https://colab.research.google.com/drive/1vIw8aq05-YAi_HinW2kKWvTbDx6fVSFz?authuser=1#scrollTo=Z9H3lrXAlnL_
"""

# Función para generar una semiesfera
def generate_hemisphere(radius, resolution=300):
    phi = np.linspace(0, np.pi / 2, resolution // 2)  # Ángulo phi va de 0 a pi/2 para la mitad de la esfera
    theta = np.linspace(0, 2 * np.pi, resolution)     # Ángulo theta va de 0 a 2*pi completo

    phi, theta = np.meshgrid(phi, theta)

    x = radius * np.sin(phi) * np.cos(theta)
    y = radius * np.sin(phi) * np.sin(theta)
    z = radius * np.cos(phi)

    return x, y, z

# Función para convertir coordenadas esféricas a cartesianas
def spherical_to_cartesian(radius, azimuth, elevation):
    azimuth_rad = np.deg2rad(azimuth)
    elevation_rad = np.deg2rad(elevation)
    
    x = radius * np.cos(azimuth_rad) * np.cos(elevation_rad)
    y = radius * np.sin(azimuth_rad) * np.cos(elevation_rad)
    z = radius * np.sin(elevation_rad)
    
    return x, y, z

# Coordenadas de ejemplo (elevación y azimut en grados)
coordinates = [
(0.341777,	57.525432),
(1.902168,	59.206483),
(3.489891,	60.863255),
(5.103246,	62.497814),
(6.740599,	64.112292),
(8.400377,	65.708889),
(10.081062,	67.289872),
(11.781191,	68.857583),
(13.499345,	70.414442),
(15.234149,	71.962961),
(16.984262,	73.505751),
(18.748372,	75.04554),
(20.525192,	76.585191),
(22.313446,	78.12772),
(24.111871,	79.676328),
(25.919198,	81.234422),
(27.734149,	82.805658),
(29.555426,	84.393974),
(31.381695,	86.003645),
(33.211576,	87.639332),
(35.043627,	89.30615),
(36.876323,	91.009746),
(38.708039,	92.756382),
(40.53702,	94.553049),
(42.361355,	96.407579),
(44.178938,	98.328795),
(45.987426,	100.326679),
(47.784189,	102.41256),
(49.566245,	104.59934),
(51.330181,	106.901744),
(53.072066,	109.336596),
(54.78733,	111.923113),
(56.470636,	114.683196),
(58.115713,	117.641683),
(59.715166,	120.826494),
(61.260261,	124.268574),
(62.740693,	128.001453),
(64.144344,	132.060205),
(65.457099,	136.47945),
(66.662744,	141.290069),
(67.743079,	146.514263),
(68.678353,	152.158979),
(69.448157,	158.208272),
(70.032865,	164.616282),
(70.415533,	171.303494),
(70.583981,	178.159189),
(70.532547,	185.051587),
(70.262981,	191.844091),
(69.78416,	198.413024),
(69.110739,	204.661437),
(68.261171,	210.525655),
(67.255661,	215.974518),
(66.114455,	221.003727),
(64.85666,	225.628258),
(63.499581,	229.875088),
(62.058452,	233.777351),
(60.546434,	237.370201),
(58.974773,	240.688173),
(57.35301,	243.763677),
(55.689226,	246.626274),
(53.990265,	249.302437),
(52.261941,	251.815605),
(50.509215,	254.186393),
(48.736343,	256.432864),
(46.94725,	258.570827),
(45.144389,	260.614123),
(43.331319,	262.57489),
(41.510278,	264.463802),
(39.683493,	266.290278),
(37.852974,	268.06266),
(36.020554,	269.788371),
(34.187925,	271.474047),
(32.356663,	273.125651),
(30.52825,	274.748571),
(28.704099,	276.347703),
(26.885565,	277.92752),
(25.073964,	279.492132),
(23.270584,	281.045341),
(21.476696,	282.590683),
(19.693566,	284.131463),
(17.922463,	285.670793),
(16.164664,	287.211616),
(14.42147,	288.756728),
(12.694204,	290.308802),
(10.984222,	291.8704),
(9.29292,	293.44399),
(7.621736,	295.031956),
(5.972157,	296.636603),
(4.345728,	298.260167),
(2.744049,	299.904817),
(1.168784,	301.572654),

]

# Función para generar el plano horizontal orientado al norte
def generate_north_plane(radius, resolution=300):
    u = np.linspace(0, 2 * np.pi, resolution)
    v = np.linspace(0, np.pi / 2, resolution // 2)  # Mitad de la esfera

    u, v = np.meshgrid(u, v)
    x = radius * np.sin(u) * np.cos(v)
    y = radius * np.cos(u) * np.cos(v)
    z = radius * np.sin(v)
    
    return x, y, z

# Crear una figura y configurar el tamaño de la ventana
fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111, projection='3d')

# Generar semiesfera
radius = 20
x, y, z = generate_hemisphere(radius)

# Dibujar la semiesfera
ax.plot_surface(x, y, z, color='b', alpha=0.3)

# Plotear los puntos en la semiesfera
for elevation, azimuth in coordinates:
    # Convertir a coordenadas cartesianas
    point_x, point_y, point_z = spherical_to_cartesian(radius, azimuth, elevation)

    # Dibujar el punto
    ax.scatter(point_x, point_y, point_z, color='r', s=20)  # s es el tamaño del punto


# Agregar etiquetas a los ejes
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

# Ajustar límites para asegurar una correcta visualización
ax.set_xlim(-radius, radius)
ax.set_ylim(-radius, radius)
ax.set_zlim(0, radius)

# Ajustar la vista para una perspectiva axonométrica
ax.view_init(elev=30, azim=45)  # Elevación y azimut para una vista axonométrica

# Mostrar la gráfica
plt.show()
