import math

massa = 0.5  
gravidade = 10

def calcular_velocidade_inicial(forca, massa):
    return math.sqrt((2 * forca) / massa)


def calcular_tempo_total_voo(velocidade_inicial, angulo, gravidade):
    return (2 * velocidade_inicial * math.sin(math.radians(angulo))) / gravidade


def calcular_alcance_horizontal(velocidade_inicial, angulo, gravidade):
    return (velocidade_inicial ** 2 * math.sin(2 * math.radians(angulo))) / gravidade


def calcular_velocidades_instantaneas(velocidade_inicial, angulo, tempo, gravidade):
    vx = velocidade_inicial * math.cos(math.radians(angulo))
    vy = velocidade_inicial * math.sin(math.radians(angulo)) - gravidade * tempo
    return vx, vy
''

def main():
    x = float(input("Digite a coordenada x do canhão: "))
    y = float(input("Digite a coordenada y do canhão: "))
    forca = float(input("Digite a força em newtons: "))
    angulo = float(input("Digite o ângulo em graus: "))
 

    velocidade_inicial = calcular_velocidade_inicial(forca, massa)
    tempo_total_voo = calcular_tempo_total_voo(velocidade_inicial, angulo, gravidade)
    alcance_horizontal = calcular_alcance_horizontal(velocidade_inicial, angulo, gravidade)
    local_queda_x = x + alcance_horizontal
    local_queda_y = 0  

    print("Resultados:")
    print(f"1. Velocidade Inicial: {velocidade_inicial:.2f} m/s")
    print(f"2. Tempo Total de Voo: {tempo_total_voo:.2f} segundos")
    print(f"3. Local de Queda do Projétil: ({local_queda_x:.2f}, {local_queda_y:.2f})")
    print("4. Velocidades (Vertical, Horizontal) em cada instante do voo:")

    intervalo_tempo = 0.1  

    for tempo in range(int(tempo_total_voo * 10) + 1):
        tempo_segundos = tempo / 10  
        vx, vy = calcular_velocidades_instantaneas(velocidade_inicial, angulo, tempo_segundos, gravidade)
        print(f"   Tempo: {tempo_segundos:.1f} s - Vertical: {vy:.2f} m/s, Horizontal: {vx:.2f} m/s")

    print(f"5. Distância Horizontal entre o Ponto de Lançamento e o Local da Queda: {alcance_horizontal:.2f} metros")

if __name__ == "__main__":
    main()