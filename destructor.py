import os, random, textwrap, time
import tkinter as tk
from stringcolor import *
import tkinter.filedialog as fd
from tkinter import filedialog


#CODIGO DESASTRE, ME DA PAJA EXPLICARLO
def triturar(archivito):
    cuenta = 0
    while cuenta <= 36:
        cuenta += 1
        with open(archivito, 'w'):
            pass
        with open(archivito, 'w') as archivo:
            cuenta2 = 0
            numero_random = random.randrange(180, 900)
            while cuenta2 <= numero_random:
                cuenta2 += 1
                mensaje = "WAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAJAWAJWJAAJAJA"
                archivo.write(f"{mensaje}\n")
        archivo.close()
        os.remove(archivito)
    
def main():
    def clear():
        if os.name == "nt":
            os.system("cls")
        else:
            os.system("clear")

    clear()
    def center_wrap(text, cwidth=80, **kw):
        lines = textwrap.wrap(text, **kw)
        return "\n".join(line.center(cwidth) for line in lines)
    def banner(menu):

        japo = """
        く__,.ヘヽ.　　　　/　,ー､ 〉
    　　　　　＼ ', !-─‐-i　/　/´
    　　　 　 ／｀ｰ'　　　 L/／｀ヽ､
    　　 　 /　 ／,　 /|　 ,　 ,　　　 ',
    　　　ｲ 　/ /-‐/　ｉ　L_ ﾊ ヽ!　 
    　　　 ﾚ ﾍ 7ｲ｀ﾄ　 ﾚ'ｧ-ﾄ､!ハ|　 |
    　　　　 !,/7 '0'　　 ´0iソ| 　      |　　　
    　　　　 |.从"　　_　　 ,,,, / |./ 　 |
    　　　　 ﾚ'| i＞.､,,__　_,.イ / 　.i 　|
    　　　　　 ﾚ'| | / k_７_/ﾚ'ヽ,　ﾊ.　|
    　　　　　　 | |/i 〈|/　 i　,.ﾍ |　i　|
    　　　　　　.|/ /　ｉ： 　 ﾍ!　　＼　|
    　　　 　 　 kヽ>､ﾊ 　 _,.ﾍ､ 　 /､!
    　　　　　　 !'〈//｀Ｔ´', ＼ ｀'7'ｰr'
    　　　　　　 ﾚ'ヽL__|___i,___,ンﾚ|ノ
    　　　　　 　　　ﾄ-,/　|___./
    　　　　　 　　　'ｰ'　　!_,.: \n""".center(40)
        texto = "INFO-DESTRUCTOR"
        linea = "=======================".center(40)
        banner = f"""
        {cs(japo, "#00ffae")}
        {cs(linea, "#03fc77")}
        {texto.center(40)}
        {cs(menu, "#00ffae")}
        {cs(linea, "#03fc77")}
        """
        return banner
    print(banner("more#6123".center(40)))
    options = f'                 {cs("[1]", "#00ffae")} multi   {cs("[2]", "#00ffae")} one'
    print(options.center(40))
    def opciones(opcion, modo):
        def cli(modo):
            if modo == "multi":
                clear()
                print(banner("COMMANDLINE".center(40)))
                u = input("  ubicacion: ")
                if os.path.exists(u) == False:
                    clear()
                    print(banner("COMMANDLINE".center(40)))
                    print(f"  {cs('LA CARPETA NO EXISTE VUELVE A INTENTARLO CON EL COMANDO RETRY', '#f20000')} \n")
                    time.sleep(0.5)
                    opcion = input("  : ")
                    if opcion == "retry":
                            cli(modo)
                    opciones(opcion)
                else:
                    a = input("  archivos: ")
                    a = a.replace(" ", "")
                    a = a.split(",")
                    def archivos(archivo):
                        for archivos in archivo:
                            if archivos not in os.listdir(u):
                                return False
                            else:
                                return True
                    if archivos(a) == True:
                        try:
                            for archivos in a: 
                                triturar(f"{u}/{archivos}")
                            print(f"  {cs('ARCHIVOS E INFORMACION  DESTRUIDO/AS', '#03fc77')}\n")
                        except:
                            print(f"  {cs('ERROR', '#f20000')}\n")
                        opcion = input("  : ")
                        if opcion == "retry":
                            cli(modo)
                        opciones(opcion)
                    else:
                        print(f"  {cs('VERIFICA EL NOMBRE DE LOS ARCHIVOS Y INTENTALO NUEVAMENTE CON EL COMANDO RETRY', '#f20000')}\n")
                        time.sleep(0.2)
                        if opcion == "retry":
                            cli(modo)
                        opciones(opcion)

            else:
                clear()
                print(banner("COMMANDLINE".center(40)))
                u = input("  archivo: ")
                if os.path.exists(u) == False:
                    clear()
                    print(banner("COMMANDLINE".center(40)))
                    print(f" {cs('LA CARPETA NO EXISTE', '#f20000')}\n")
                    opcion = input("  : ")
                    opciones(opcion)
                else:
                    a = input("  archivos: ")
                    a = a.split(",")
                    try:
                        for archivos in a: 
                            triturar(archivos)
                        print(f"  {cs('ARCHIVOS E INFORMACION DESTRUIDO/AS', '#03fc77')}\n")
                    except:
                        print(f"  {cs('ERROR', '#f20000')}\n")
                opcion = input("  : ")
                if opcion == "retry":
                    cli()
                opciones(opcion)

        
        def gui(modo):
            clear()
            if modo == "multi":
                try:
                    clear()
                    print(banner("SEMI-GUI".center(40)))
                    a = filez = filedialog.askopenfilenames(title='Choose a file')
                    for archivos in a:
                        triturar(archivos)
                    print(f"\n  {cs('ARCHIVOS E INFORMACION DESTRUIDO/AS', '#03fc77')}\n")
                    opcion = input("  : ")
                    if opcion == "retry":
                        gui(modo)
                    opciones(opcion, None)
                except:
                    clear()
                    print(banner("SEMI-GUI".center(40)))
                    print(f"  {cs(' ERROR', '#f20000')}\n")
                    if opcion == "retry":
                        gui(modo)
                    opciones(opcion)
            else:
                print(banner("SEMI-GUI".center(40)))
                a = filedialog.askopenfilename()
                try:
                    triturar(a)
                    print(f"\n  {cs('ARCHIVO E INFORMACION DESTRUIDO/A', '#03fc77')}\n")
                except:
                    print(f"  {cs(' ERROR', '#f20000')}\n")
                opcion = input("  : ")
                if opcion == "retry":
                    gui(modo)
                opciones(opcion, None)

        if opcion == "ayuda":
            clear()
            print(banner("AYUDA".center(40)))
            print(" COMANDOS")
            print("  SEMI-GUI MODE: gui")
            print("  TERMINAL MODE: cli")
            print("  BACK: volver")
            print("  RETRY: retry")
            print("  EXIT: salir")
            opcion = input("  : ")
            opciones(opcion)
        modos = ["multi"]
        if opcion == "gui" and modo == "multi":
            gui("multi")
        if opcion == "gui" and modo not in modos:
            gui(None)
        if opcion == "cli" and modo == "multi":
            cli("multi")
        if opcion == "cli" and modo not in modos:
            cli(None)
        if opcion == "volver":
            main()
        if opcion == "salir":
            clear()
            exit()
    opcion = input("  : ")
    if opcion == "1":
        clear()
        print(banner("MULTIPLE_FILES".center(40)))
        print(f"\n  {cs('MULTI: ON', '#03fc77')}\n")
        opcion = input("  : ")
        opciones(opcion, "multi")
    if opcion == "2":
        clear()
        print(banner("ONE_FILE".center(40)))
        print(f"\n  {cs('ONE: ON', '#03fc77')}\n")
        opcion = input("  : ")
        opciones(opcion, "one")
        
        
main()
