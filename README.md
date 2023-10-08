# Python Fibonacci

Aplicacion funcionando con Flask, debido a que Flask es un framework de Python que permitirá crear un programa que se ejecutará en el servidor en este caso un servidor Local y con un mínimo número de líneas de código. 

Teoricamente la aplicacion es sencilla y se divide en dos pasos.

# Paso 1

Se implementa la logica del API, la cual calculara Fibonacci recursivamente.

# Paso 2 

Se estipula una ruta para poder ejecutar el API anteriormente desarrollado y que devolvera 200 si es numero entero y un 400 si no es un numero entero.

# Ejecutar el API

Correr comando python app.py

# Mejoras o implementaciones en la nube

Yo desplegaria el API por medio de serveless y unicamente seria la logica del API, la cual calculara Fibonacci recursivamente. Esta API la desplegaria en Lambda dentro de AWS y para las peticiones meteria un API Gateway como puerta de entrada, ya los modelos para ver las devoluciones a estas llamadas las implementaria por JSON. Adicional ¿porque utilizar API Gateway?, de este modo controlariamos las peticiones que atacarian el API y expondriamos unicamente lo que deseamos y se podria colocar capas de seguridad como lo es Cognito como autorizador (o crear una lambda para autorizar), adicional puede colocarse dentro de la etapa implementada WAF como cuestion como implementacion a la seguridad.
