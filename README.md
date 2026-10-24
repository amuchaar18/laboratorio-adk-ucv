# Laboratorio UCV – Google ADK + Poetry + GitHub + SonarQube

## Descripción
Proyecto de mono-agente básico utilizando Google ADK y Python, gestionando dependencias con Poetry, versionando en GitHub e integrando análisis de calidad estático con SonarQube mediante GitHub Actions.

## Requisitos Previos
- Python 3.10 o superior
- Poetry instalado (`pip install poetry`)
- Cuenta en GitHub y SonarCloud

## Instalación y Configuración
1. Clonar el repositorio.
2. Instalar dependencias con Poetry:
   ```bash
   poetry install
   ```
3. Configurar tu clave de API de Google en un archivo `.env`:
   ```env
   GOOGLE_API_KEY="TU_API_KEY"
   ```

## Ejecución del Agente
Para ejecutar el agente en la terminal:
```bash
poetry run adk run agente_ucv
```
Para ejecutar la interfaz web:
```bash
poetry run adk web --port 8000
```
Luego, abre el navegador en: `http://localhost:8000`

## Ejecución de Pruebas Unitarias
```bash
poetry run pytest
```
