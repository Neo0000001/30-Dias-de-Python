
""" * Crea un programa que calcule quien gana más partidas al piedra,
 * papel, tijera, lagarto, spock.
 * - El resultado puede ser: "Player 1", "Player 2", "Tie" (empate)
 * - La función recibe un listado que contiene pares, representando cada jugada.
 * - El par puede contener combinaciones de "🗿" (piedra), "📄" (papel),
 *   "✂️" (tijera), "🦎" (lagarto) o "🖖" (spock).
 * - Ejemplo. Entrada: [("🗿","✂️"), ("✂️","🗿"), ("📄","✂️")]. Resultado: "Player 2".
 * - Debes buscar información sobre cómo se juega con estas 5 posibilidades.
<NORMAS>
    Las tijeras cortan el papel - Gana: ✂️
    El papel cubre a la piedra - Gana: 📄
    La piedra aplasta las tijeras - Gana: 🗿
    La piedra aplasta al lagarto - Gana: 🗿
    El lagarto envenena a Spock - Gana: 🦎
    Spock destroza las tijeras - Gana: 🖖
    Las tijeras decapitan al lagarto - Gana: ✂️
    El lagarto se come el papel - Gana: 🦎
    El papel desautoriza a Spock - Gana: 📄
    Spock vaporiza la piedra - Gana: 🖖
"""

def quien_gana(partidas):
    jugador_1 = 0
    jugador_2 = 0

    for jugada in partidas:
        if jugada[0] == jugada[1]:
            continue
        elif jugada[0] == "🗿":
            if jugada[1] == "✂️" or jugada[1] == "🦎":
                jugador_1 += 1
            else:
                jugador_2 += 1
        elif jugada[0] == "📄":
            if jugada[1] == "🗿" or jugada[1] == "🖖":
                jugador_1 += 1
            else:
                jugador_2 += 1
        elif jugada[0] == "✂️":
            if jugada[1] == "📄" or jugada[1] == "🖖":
                jugador_1 += 1
            else:
                jugador_2 += 1
        elif jugada[0] == "🦎":
            if jugada[1] == "📄" or jugada[1] == "🖖":
                jugador_1 += 1
            else:
                jugador_2 += 1
        elif jugada[0] == "🖖":
            if jugada[1] == "🗿" or jugada[1] == "✂️":
                jugador_1 += 1
            else:
                jugador_2 += 1
    
    if jugador_1 > jugador_2:
        return "Player 1"
    elif jugador_2 > jugador_1:
        return "Player 2"
    else:
        return "Tie"

print(quien_gana([("🗿","✂️"),("🖖","🦎"),("🖖","🗿")]))