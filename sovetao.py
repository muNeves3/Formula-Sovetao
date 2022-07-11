posicaoInicial = float(input("Digite a posição inicial (m) : "));
velocidadeInicial = float(input("Digite a velocidade inicial (m\s): "));
tempo = int(input("Digite o tempo em segundos: "));
aceleracao = float(input("Digite a aceleração (m\s²): "));

posicaoFinal = posicaoInicial + velocidadeInicial * tempo + ((aceleracao * pow(tempo, 2)) / 2);

print(f'A posição final do objeto será: {posicaoFinal}m');


print("""
    Designed by
    Equipe Então™
""")
