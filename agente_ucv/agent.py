from google.adk.agents.llm_agent import Agent

def explicar_concepto(concepto: str) -> dict:
    if not isinstance(concepto, str) or not concepto.strip():
        return {"status": "error", "explicacion": "Entrada inválida."}
        
    conceptos = {
        "api": "Una API permite comunicación entre sistemas.",
        "algoritmo": "Un algoritmo es una secuencia de pasos.",
        "base de datos": "Una base de datos almacena información.",
        "python": "Lenguaje de programación principal del proyecto.",
        "github": "Plataforma de versionamiento de proyectos.",
        "poetry": "Gestor de dependencias de Python.",
        "sonarqube": "Herramienta de análisis estático de código.",
        "docker": "Plataforma de contenedores."
    }
    concepto = concepto.lower().strip()
    if concepto in conceptos:
        return {"status": "success", "explicacion": conceptos[concepto]}
    return {"status": "not_found", "explicacion": "Concepto no registrado."}

def calcular_promedio(notas: list[float]) -> dict:
    if not notas or not all(isinstance(n, (int, float)) for n in notas):
        return {"status": "error", "resultado": "Entrada inválida, se requiere lista de números."}
    return {"status": "success", "promedio": sum(notas) / len(notas)}

root_agent = Agent(
    model="gemini-flash-latest",
    name="agente_ucv",
    description="Agente académico UCV",
    instruction="Eres un asistente académico. Responde en español. Usa lenguaje simple.",
    tools=[explicar_concepto, calcular_promedio],
)
