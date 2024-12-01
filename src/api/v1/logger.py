

def terminalcolor(estilo, cor):
    definicao_estilo = {0: "0", 1: "1", 2: "4", 3: "7"}
    definicao_cor = {0: "37", 1: "30", 2: "31", 3: "32", 4: "33", 5: "34", 6: "35", 7: "36"}

    base = "\033[0;0m"
    padrao = f"\033[{definicao_estilo[estilo]};{definicao_cor[cor]}m"
    return padrao,  base


def errormessage(message):
    red,  base = terminalcolor(1,  2)
    print(f"{red}{message}{base}\n")


def successmessage(message):
    green, base = terminalcolor(0,  3)
    print(f"✅{green}{message}{base}")


def awaitmessage(message):
    blue, base = terminalcolor(0,  7)
    print(f"🚀 {blue}{message}{base}")


def alertmessage(message):
    yellow, base = terminalcolor(0,  4)
    print(f"{yellow}{message}{base}")
    