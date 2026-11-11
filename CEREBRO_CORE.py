
import json
import os
from datetime import datetime


class JarvisCore:

    def __init__(self):
        self.name = "JARVIS"
        self.version = "0.1.0"
        self.memory_file = "memoria_jarvis.json"

        self.memory = self.load_memory()

        print("=" * 45)
        print("       J.A.R.V.I.S. CORE SYSTEM")
        print("       Version:", self.version)
        print("       STATUS: ONLINE")
        print("=" * 45)

    # SISTEMA DE MEMORIA

    def load_memory(self):
        if os.path.exists(self.memory_file):
            try:
                with open(self.memory_file, "r",
                          encoding="utf-8") as file:
                    return json.load(file)
            except (json.JSONDecodeError, OSError):
                return {"recuerdos": []}

        return {"recuerdos": []}

    def save_memory(self):
        with open(self.memory_file, "w",
                  encoding="utf-8") as file:
            json.dump(
                self.memory,
                file,
                ensure_ascii=False,
                indent=4
            )

    def remember(self, information):
        record = {
            "contenido": information,
            "fecha": datetime.now().isoformat()
        }

        self.memory["recuerdos"].append(record)
        self.save_memory()

        return "Información guardada en mi memoria."

    def recall(self):
        records = self.memory.get("recuerdos", [])

        if not records:
            return "Mi memoria todavía está vacía."

        result = "INFORMACIÓN ALMACENADA:\n"

        for index, record in enumerate(records, 1):
            result += (
                f"{index}. {record['contenido']}\n"
            )

        return result

    # MOTOR DE PROCESAMIENTO

    def process(self, instruction):

        command = instruction.strip()
        lower = command.lower()

        if not command:
            return "No recibí ninguna instrucción."

        if lower in ["hola", "hola jarvis"]:
            return "Saludos. Sistemas preparados."

        if lower in ["estado", "diagnostico"]:
            return (
                "Sistema operativo.\n"
                "Núcleo central: activo.\n"
                "Memoria: activa.\n"
                "Versión: " + self.version
            )

        if lower.startswith("recordar:"):
            information = command[9:].strip()

            if information:
                return self.remember(information)

            return "Indica qué información debo recordar."

        if lower in ["memoria", "recuerdos"]:
            return self.recall()

        if lower == "ayuda":
            return (
                "COMANDOS DISPONIBLES:\n"
                "hola\n"
                "estado\n"
                "recordar: información\n"
                "memoria\n"
                "ayuda\n"
                "salir"
            )

        if lower == "salir":
            return "Cerrando sesión."

        return (
            "He recibido tu instrucción: "
            + command
            + "\nMi motor de inteligencia artificial "
              "todavía necesita conectarse."
        )

    # INTERFAZ DE CONSOLA

    def start(self):

        print("\nJARVIS está preparado.")
        print("Escribe 'ayuda' para ver los comandos.\n")

        while True:

            try:
                instruction = input("USUARIO > ")
                response = self.process(instruction)

                print("\nJARVIS >", response, "\n")

                if instruction.strip().lower() == "salir":
                    break

            except KeyboardInterrupt:
                print("\nSesión interrumpida.")
                break

            except Exception as error:
                print("ERROR DEL SISTEMA:", error)


if __name__ == "__main__":
    jarvis = JarvisCore()
    jarvis.start()
