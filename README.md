## Función Lambda en Python

Esta es una función Lambda escrita en Python que realiza una conversión de SOAP a REST.

### Ejecutar el script después de cambios

Después de realizar cambios en el proyecto, es importante ejecutar el script **_script.sh_** para crear el archivo **_deployment.zip_**, que será el archivo a subir a AWS Lambda.

### Instrucciones

1. Abre una terminal.
2. Navega al directorio raíz del proyecto.
3. Ejecuta el siguiente comando: ```./script.sh ```
Esto ejecutará el script script.sh y realizará:

   1. Instala las dependencias especificadas en el archivo requirements.txt en una carpeta de destino utilizando pip3 install.
   2. Comprime el contenido de la carpeta de destino en un archivo ZIP utilizando el comando zip -r.
   3. Agrega archivos adicionales desde la carpeta schemas al archivo ZIP utilizando zip -g.
   4. Agrega el archivo lambda_function.py al archivo ZIP utilizando zip -g.