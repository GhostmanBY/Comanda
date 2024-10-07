import os
import json
import datetime

base_dir = os.path.dirname(os.path.abspath(__file__))
ruta_mesa = os.path.join(base_dir, "../Docs/Mesa.json")

def mesa_tmp(cantidad: int):
    with open(ruta_mesa, "r", encoding="utf-8") as file:
        content = json.load(file)

    for i in range(cantidad):
        content["Mesa"] = i+1
        with open(os.path.join(base_dir ,f"../tmp/Mesa {i+1}.json"),"w") as file:
            json.dump(content, file, indent= 4, ensure_ascii=False)

def abrir_mesa(mesa: int, mozo: str):
    # Captura de la hora de cierre de la mesa y el día
    fecha_origin = datetime.datetime.now()
    fecha = fecha_origin.strftime("%H:%M")

    with open(os.path.join(base_dir, f"../tmp/Mesa {mesa}.json"), "r", encoding="utf-8") as file:
        mesa_tem = json.load(file)

    if mesa_tem["Disponibilidad"] == False:
        return f"La mesa numero {mesa} ya esta abierta"
    
    mesa_tem["Disponibilidad"] = False
    mesa_tem["Mozo"] = mozo

    mesa_tem.update({"Hora Apertura": str(fecha)})

    with open(os.path.join(base_dir, f"../tmp/Mesa {mesa}.json"), "w", encoding="utf-8") as file:
        json.dump(mesa_tem, file, indent= 4, ensure_ascii=False)

#funcion para editar la mesa
def editar_mesa(categoria: str, valor, mesa: int):
    with open(os.path.join(base_dir, f"../tmp/Mesa {mesa}.json"), "r", encoding="utf-8") as file:
        mesa_tem = json.load(file)

    if categoria == "Productos":
        for i in range(len(valor)):
            lista = []
            lista.append(valor)
        mesa_tem[categoria] = lista
    elif categoria == "Comensales infatiles":
        mesa_tem[categoria] = [True, valor]
    else:
        mesa_tem[categoria] = valor

    with open(os.path.join(base_dir, f"../tmp/Mesa {mesa}.json"), "w", encoding="utf-8") as file:
        json.dump(mesa_tem, file, indent= 4, ensure_ascii=False)
        
if __name__ == "__main__":
    #mesa_tmp(10)
    abrir_mesa(1, "Nahuel")
    editar_mesa("Comensales", 2, 1)
    editar_mesa("Comensales infatiles", 2, 1)
    editar_mesa("Productos", ["Café expreso"])
    pass
