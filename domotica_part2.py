import time
import random

salon = False
dormitori = False
cuina = False
co2_actual = 0

def menu_principal():
    while True:           
        print("\033[36mMENU DE CONFIGURACIÓ\033[0m")
        print("\033[33m1. Control de llums\033[0m")
        print("\033[32m2. Control de temperatura\033[0m")
        print("\033[35m3. Alarma de CO₂\033[0m")
        print("\033[31m4. Tornar al menú anterior\033[0m")

        llista = [1, 2, 3, 4]
        
        while True:
            try:
                opcio = int(input("Tria una opció (1-4): "))
                if opcio not in llista:
                    print("Opció fora de rang. Torna-ho a provar.")
                    continue
                break
            except ValueError:
                print("Entrada no vàlida, introdueix un número (1-4).")

        match opcio:
            case 1:
                llums()
            case 2:
                control_temperatura()
            case 3:
                alarma()
            case 4:
                print("Fins aviat!")
                break


def missatge_llums(habitacio: str, estat: bool):
    print(f"room {habitacio} : LLums {'ON' if estat else 'OFF'} correctly")


def opcionsllums():
    print(" CONTROL LLUMS")
    print("1 Selecciona la habitació")
    print("2 Selecciona totes les habitacions")
    print("3 Mostrar estat real de les llums")
    print("4 Tornar al menú anterior")


def llums():
    global salon, dormitori, cuina
    while True:
        opcionsllums()

        llista2 = [1, 2, 3, 4]
        while True:
            try:
                opcio = int(input("Selecciona quina opcio vols (1-4): "))
                if opcio not in llista2:
                    print("Opció fora de rang. Torna-ho a provar.")
                    continue
                break
            except ValueError:
                print("Entrada no vàlida.")
        
        match opcio:
            case 1:
                habitacio = input("Introdueix la habitació (salon/dormitori/cuina): ")
                manual = input("turn on or turn off (on/off): ")
                if habitacio == "salon":
                    salon = True if manual == "on" else False
                    missatge_llums("salon", salon)
                elif habitacio == "dormitori":
                    dormitori = True if manual == "on" else False
                    missatge_llums("dormitori", dormitori)
                elif habitacio == "cuina":
                    cuina = True if manual == "on" else False
                    missatge_llums("cuina", cuina)
                else:
                    print("Habitació no reconeguda.")

            case 2:
                manual = input("turn on or turn off all (on/off): ")
                if manual == "on":
                    salon = dormitori = cuina = True
                    print("Totes les habitacions enceses.")
                elif manual == "off":
                    salon = dormitori = cuina = False
                    print("Totes les habitacions apagades.")
                else:
                    print("Comanda desconeguda.")
                missatge_llums("salon", salon)
                missatge_llums("dormitori", dormitori)
                missatge_llums("cuina", cuina)

            case 3:
                print("Estat actual de totes les llums:")
                missatge_llums("salon", salon)
                missatge_llums("dormitori", dormitori)
                missatge_llums("cuina", cuina)

            case 4:
                print("Tornant al menú principal")
                return


def mostrar_menu_temp():
    print(" CONTROL TEMPERATURA ")
    print("1 Configurar límits de temperatura")
    print("2 Veure estat actual")
    print("3 Sortir")


def control_temperatura():
    minim = None
    maxim = None
    while True:
        mostrar_menu_temp()

        llista2 = [1, 2, 3]
        while True:
            try:
                opcio = int(input("Selecciona una opció (1-3): "))
                if opcio not in llista2:
                    print("Opció fora de rang. Torna-ho a provar.")
                    continue
                break
            except ValueError:
                print("Entrada no vàlida.")
        
        match opcio:
            case 1:
                try:
                    minim = float(input("Introdueix Temperatura MÍNIMA (°C): "))
                    maxim = float(input("Introdueix Temperatura MÀXIMA (°C): "))
                    if minim >= maxim:
                        print("El mínim ha de ser menor que el màxim. Torna a intentar-ho.")
                        minim = maxim = None
                except ValueError:
                    print("Entrada no vàlida. Introdueix nombres vàlids.")
                    minim = maxim = None

            case 2:
                if minim is None or maxim is None:
                    print("Primer has de configurar els límits (opció 1).")
                    continue
                try:
                    temps_actual = float(input("Introdueix temperatura ACTUAL (°C): "))
                except ValueError:
                    print("Entrada no vàlida.")
                    continue

                calefactor = temps_actual < minim
                if temps_actual >= maxim:
                    calefactor = False

                print("-" * 40)
                print(f"Límit mínim: {minim} °C  |  Límit màxim: {maxim} °C")
                print(f"Temperatura actual: {temps_actual} °C")
                print(f"Calefactor: {'ACTIVAT' if calefactor else 'APAGAT'}")
                print("-" * 40)

            case 3:
                print("Tornant al menú principal")
                return


def menu_alarma():
    print(" ALARMA CO₂ ")
    print("1 Configurar límit de CO₂")
    print("2 Veure estat actual")
    print("3 Sortir")


def alarma():
    limit = None 
    while True:
        menu_alarma()

        llista2 = [1, 2, 3]
        while True:
            try:
                opcio = int(input("Selecciona una opció (1-3): "))
                if opcio not in llista2:
                    print("Opció fora de rang. Torna-ho a provar.")
                    continue
                break
            except ValueError:
                print("Entrada no vàlida.")
        
        match opcio:
            case 1:
                try:
                    limit = float(input("Introdueix el límit MÀXIM de CO₂ (ppm): "))
                except ValueError:
                    print("Entrada no vàlida.")
                    limit = None

            case "2":
                print("Simulació de CO₂ iniciada. Prem Ctrl+C per aturar.")

                try:
                    for hora in range(0,24):
                        for minut in range(0, 60):
                            print(f"Hora actual: {hora}:{minut}")  
                            increment = random.randint(10, 25)
                            co2_actual += increment
                            print(f" Nivell actual de CO₂: {co2_actual} ppm")
                            if co2_actual > limit:
                                print("Alarma! Nivell de CO₂ massa alt!")
                            time.sleep(1)
                except KeyboardInterrupt:
                    print("Simulació aturada per l'usuari.")
            case 3:
                print("Tornant al menú principal")
                return


if __name__ == "__main__":
    opcio = "0"
    while opcio != "4":
        opcio = input("Introdueix opció (1: menú / 2: simulació CO₂ / 3: simulació llums / 4: sortir): ")
        match opcio:
            case "1":
                menu_principal()
            case "2":
                print("Simulació de CO₂ iniciada. Prem Ctrl+C per aturar.")
                try:
                    for hora in range(0, 24):
                        for minut in range(0, 60):
                            print(f"Hora actual: {hora}:{minut}")  
                            increment = random.randint(10, 25)
                            co2_actual += increment
                            print(f" Nivell actual de CO₂: {co2_actual} ppm")
                            if co2_actual > limit:
                                print("Alarma! Nivell de CO₂ massa alt!")
                            time.sleep(1)
                except KeyboardInterrupt:
                    print("Simulació aturada per l'usuari.")
            case "3":
                print("Simulació de llums iniciada. Prem Ctrl+C per aturar.")
                try:
                    while True:
                        salon = random.choice([True, False])
                        dormitori = random.choice([True, False])
                        cuina = random.choice([True, False])
                        print("-" * 40)
                        print(f"Saló: {'ON' if salon else 'OFF'}")
                        print(f"Dormitori: {'ON' if dormitori else 'OFF'}")
                        print(f"Cuina: {'ON' if cuina else 'OFF'}")
                        print("-" * 40)
                        time.sleep(2)
                except KeyboardInterrupt:
                    print("Simulació aturada per l'usuari.")
            case "4":
                print("Sortint del programa")
            case _:
                print("Opció no vàlida.")
