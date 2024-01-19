# Rewards Service (rewards-serv)

El servicio `rewards-serv` es el encargado de manejar las recompensas y penalizaciones que afectan la vida de los barcos en el juego Battleship. Este microservicio calcula y asigna cambios en la vida de los barcos de forma aleatoria.

## Estructura del Proyecto
La estructura de `rewards-serv` siguiendo los principios de Clean Architecture es la siguiente:
- **app.py**: Archivo principal de la aplicación Flask que inicia el servicio y define los endpoints.
- **Dockerfile**: Define cómo se construye la imagen Docker del servicio.
- **README.md**: Documentación del servicio `rewards-serv`.
- **requirements.txt**: Lista de dependencias necesarias para la ejecución del servicio.
- **entities/**: Contiene las entidades del dominio del servicio.
- **use_cases/**: Contiene la lógica de negocio que opera sobre las entidades.

## Construcción y Ejecución

Para construir la imagen Docker de `rewards-serv`:
```bash
docker compose build rewards-serv
```

Para ejecutar `rewards-serv`, utiliza el siguiente comando:
```bash
docker run -p [puerto-local]:[puerto-contenedor] -v $(pwd):/rewards-serv rewards-serv 
```
