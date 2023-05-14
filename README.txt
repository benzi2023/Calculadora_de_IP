README
# README

Este repositorio contiene un código en Python para calcular la dirección de red, la dirección de broadcast y el rango de direcciones a partir de una dirección IP y una máscara de subred.

## Cómo utilizar

Para utilizar este código, sigue los siguientes pasos:

1. Clona el repositorio o descarga los archivos en tu máquina local.

2. Asegúrate de tener Python instalado en tu sistema. Este código está escrito en Python 3.

3. Abre el archivo `calcular_direccion.py` en tu editor de código preferido.

4. En la sección `ip` y `mascara`, establece los valores correspondientes a la dirección IP y la máscara de subred que deseas utilizar. Puedes modificar estos valores según tus necesidades.

5. Ejecuta el script. Puedes hacerlo ejecutando el comando `python calcular_direccion.py` en la terminal.

6. El script validará la entrada y calculará la dirección de red, la dirección de broadcast y el rango de direcciones correspondientes a la dirección IP y la máscara de subred proporcionadas.

7. Los resultados se mostrarán en la terminal, incluyendo la dirección de red, la dirección de broadcast y el rango de direcciones.

## Validación de la entrada

El código también incluye una función `validar_entrada` para verificar si la entrada proporcionada es válida. La función asegura que la dirección IP y la máscara de subred tengan el formato correcto y estén dentro del rango válido.

## Excepciones

El código utiliza una excepción personalizada llamada `InvalidInputError` para manejar errores de entrada inválida. Si se produce un error de entrada, se lanzará esta excepción junto con un mensaje de error específico.

## Notas adicionales

- Este código está diseñado para funcionar con direcciones IPv4.

- Asegúrate de tener los permisos necesarios para ejecutar el script y acceder a la información de red en tu sistema.

- Ten en cuenta que este código no realiza validaciones exhaustivas de todas las posibles combinaciones de direcciones IP y máscaras de subred. Se recomienda utilizarlo como una herramienta básica y realizar pruebas adicionales según tus requisitos específicos.

¡Disfruta utilizando este código para calcular la dirección de red, la dirección de broadcast y el rango de direcciones en Python! Si tienes alguna pregunta o sugerencia, no dudes en abrir un "issue" en este repositorio.