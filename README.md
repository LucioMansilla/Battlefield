# Battleship Project

El proyecto Battleship es una implementación dinámica del clásico juego de estrategia naval. Este proyecto utiliza una arquitectura de microservicios para manejar diferentes aspectos del juego.

Este proyecto es una continuación del viejo battlefield: https://github.com/LucioMansilla/old-Battlefield/ en donde para explorar el uso de los microservicios la caracteristica de CI/CD no esta actualmente migrada acá.

## Descripción
El proyecto se compone de tres componentes principales:
- **`battlefield-serv`**: Servicio backend principal que gestiona la lógica del juego, las interacciones del usuario y el estado del juego.
- **`rewards-serv`**: Servicio encargado de manejar sistemas de recompensas y logros dentro del juego.
- **`client`**: Interfaz de usuario construida con React.

## Datos
- La comunicación bidireccional es soportada con WebSockets, por eso co-existen con endpoints REST 

## Estructura del Proyecto

La estructura de directorios del proyecto Battleship es la siguiente:

- **battleship/**
  - **battlefield-serv/**: Servicio principal del backend del juego.
    - **api/**: Contiene los endpoints de la API.
    - **app/**: Lógica principal de la aplicación y modelos de datos. (se usa una arquitectura de capas)
    - **battlefield.py**: Punto de entrada para el servicio de battlefield.
    - **config.py**: Configuración de la aplicación.
    - **Dockerfile**: Definición de Docker para el servicio de battlefield.
    - **features/**: Características adicionales y pruebas BDD.
    - **migrations/**: Migraciones de base de datos.
    - **README.md**: Documentación específica del servicio battlefield.
    - **requirements.txt**: Dependencias del servicio battlefield.
    - **tests/**: Pruebas unitarias y de integración.
  - **client/**: Interfaz de usuario del juego, desarrollada en React.
    - **node_modules/**: Dependencias de Node.js (ignorar).
    - **package.json**: Metadatos y dependencias del cliente.
    - **package-lock.json**: Estado exacto del árbol de dependencias (ignorar).
    - **public/**: Archivos públicos del cliente, como HTML base.
    - **README.md**: Documentación específica del cliente.
    - **src/**: Código fuente del cliente React.
  - **docker-compose.yml**: Configuración de Docker Compose para levantar todo el proyecto.
  - **rewards-serv/**: Microservicio para manejo de recompensas y logros.
    - **Dockerfile**: Definición de Docker para el servicio de rewards.
    - **README.md**: Documentación específica del servicio de rewards.
    - **requirements.txt**: Dependencias del servicio de rewards.
    - **views.py**: 

## Despliegue

Para desplegar el proyecto, se debe tener instalado Docker y Docker Compose. Luego, ejecutar el siguiente comando en la raíz del proyecto:

```bash
docker-compose up
```

Para ejecuciones particulares de cada servicio, se puede utilizar el siguiente comando:

```bash
docker build -t <nombre-imagen> <directorio-dockerfile>
docker run -p <puerto-externo>:<puerto-interno> <nombre-imagen>
```
 
## Información

La documentación completa del proyecto se encuentra en el archivo `README.md` de cada servicio.
