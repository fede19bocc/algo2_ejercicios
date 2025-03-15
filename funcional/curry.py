from functools import partial

def log(tipo: str, msj: str) -> str:
    return f"{tipo}: {msj}"

msj_error = partial(log, "error")
msj_alerta = partial(log, "alerta")
msj_info = partial(log, "info")

print(msj_alerta("hola alarma"))
print(msj_error("esto es un mega error"))
print(msj_info("te informo algo"))

def log_curry(tipo:str) -> str:
    def msj(texto:str) -> str:
        return f"{tipo}: {texto}"
    return msj

print(log_curry("error")("hola horroroso"))