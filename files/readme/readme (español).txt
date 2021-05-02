----------------------------------------------------------

Requisitos:

1) Python >= 3.2: 
	Descargar e instalar. En la última pantalla del instalador, tildar "Add to PATH" y "Disable path length limit"
	Link: python.org/downloads

2) G-Python & PyQt5:
	Ejecutar "install_components.bat" desde la carpeta "readme" y seguir las instrucciones

----------------------------------------------------------

Uso: 

1) Conectar G-Earth 
2) Correr "Wallfurnix77.bat" y aceptar la ventanita que saldrá

Para seleccionar un poster, moverlo a cualquier parte
-/+ modifican las coordenadas en 1 unidad 
--/++ modifican las coordenadas en 10 unidades
---/+++ modifican las coordenadas en 100 unidades
Para ingresar un valor manualmente, escribirlo en la caja de texto y darle a "Set"
"Reset" devuelve el poster a su posición original
"Move to last" mueve el poster actual a la posición del anterior poster seteado con la extensión

----------------------------------------------------------

Actualización: 

Cuando Habbo actualice headers, la extensión se romperá :(
Para arreglarla, sobreescribir la nueva ID del packet de mover posters (MoveWallItem) en el archivo "header.txt"

----------------------------------------------------------

Créditos a kSlideHH, Laande y Sirjonasxx
