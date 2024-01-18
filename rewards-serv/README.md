# Rewards Service (rewards-serv)

El servicio `rewards-serv` es el encargado de manejar las recompensas y penalizaciones que afectan la vida de los barcos en el juego. Este microservicio calcula y asigna cambios en la vida de los barcos de forma aleatoria al inicio del juego.

## Estructura del Proyecto
La estructura de `rewards-serv` es la siguiente:
- **app.py**: Archivo principal de la aplicación Flask.
- **Dockerfile**: Define cómo se construye la imagen Docker del servicio.
- **README.md**: Documentación del servicio `rewards-serv`.
- **requirements.txt**: Lista de dependencias necesarias para la ejecución del servicio.
- **views.py**: Define los endpoints.

## Construcción y Ejecución

### Construir la Imagen Docker
Para construir la imagen Docker de `rewards-serv`:
```bash
docker compose build rewards-serv
```
### Ejecutar el Servicio
Para ejecutar `rewards-serv`, utiliza el siguiente comando:
```bash
docker run -p [puerto-local]:[puerto-contenedor] -v $(pwd):/rewards-serv rewards-serv 
```