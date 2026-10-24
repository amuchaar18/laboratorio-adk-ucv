from agente_ucv.agent import explicar_concepto, calcular_promedio

def test_explicar_concepto_valido():
    res = explicar_concepto("api")
    assert res["status"] == "success"

def test_explicar_concepto_invalido():
    res = explicar_concepto("desconocido")
    assert res["status"] == "not_found"

def test_calcular_promedio_valido():
    res = calcular_promedio([10, 15, 20])
    assert res["promedio"] == 15.0
