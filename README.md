# Formula Automatizada - Semana de la Ingeniería 24/25 - Escuela de Ingeniería y Arquitectura (Universidad de Zaragoza)
**Proyecto en Standby sin acabar**

## Resumen
En la [Escuela de Ingenieria y Arquitectura](https://eina.unizar.es/) de la [Universidad de Zaragoza](https://www.unizar.es/), los alumnos de la asociación IEEE/EINA decidimos realizar, para la Semana de la Ingeniería y Arquitectura 2024-2025, exponer un stand donde los interesados podían realizar carreras automatizadas de coches.

Para ello, un coche con un módulo para seguir lineas de un circuito, realizaria vueltas mientras los interesados podían pulsar un botón en sus móviles para ajustar la velocidad del coche. Cuanto más rápido pulsasen en conjunto, mas rápido iría el coche.

## Tecnologías utilizadas
- Front End: HTML, CSS y JS junto con BootStrap
- Back End: Python Con FastAPI

## Requerimientos Previos
Para el servidor backend se dispone del archivo "requirements.txt" donde se indican todas las librerias usadas.
Para instalar las librerias, estando en el directorio "back", ejecutar el comando `pip install -r requirements.txt`
Recomendamos que uses un [entorno virtual](#usar-entorno-virtual) para ello usando la libreria `virtualenv`

## Instalación del servidor localmente
1. Clone el repositorio `git clone https://github.com/Chechere/SIA-FA-2025.git`
2. Muevase a la carpeta "back" dentro del repositorio
3. [Opcional] instale y use un [entorno virtual](#usar-entorno-virtual) **llamado ".venv"**
4. Use el comando `pip install -r requirements.txt` para instalar las dependencias del servidor

## Uso y Contribución del servidor
Para ejecutar el servidor, ejecutar el comando `uvicorn main:app --host 0.0.0.0 --port 8000 --reload`

Para contribuir al proyecto:
1. Crea un fork en tu cuenta
2. Crea una rama nueva para la contribución `git checkout -b mi_rama`
3. Realiza tu contribución y haz commit al repositorio local `git add .` -> `git commit -m <Mensaje explicando tu increible contribución>`
4. Realiza un push a tu fork `git push origin mi_rama`
5. Realiza una pull request para incluir tu contribución al repositorio principal

¡Muchas Gracias por la ayuda! Toda ayuda, por pequeña que sea, ayuda ¡Muchas gracias! 😄

## Usar Entorno Virtual

