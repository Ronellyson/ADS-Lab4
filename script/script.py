import subprocess
import csv

qtTestes = int(input('Digite a quantidade de testes que serão realizados: '))
ordenador = input('Digite o ordenador desejado(QUICK, MERGE, ou COUNTING): ')
tamanhoEntrada = int(input('Digite o tamanho da entrada: '))
valorMaximo = int(input('Digite o valor maximo: '))

def medirOrdenacao(ordenador, tamanhoEntrada, valorMaximo):
    output = subprocess.run(
    [
        "java",
        "-cp",
        "../bin",
        "MedidorDeOrdenacao",
        ordenador,
        str(tamanhoEntrada),
        str(valorMaximo)
    ], capture_output=True, text=True)
    return output

results = []

for i in range(0, qtTestes):
    results.append(
        medirOrdenacao(
        ordenador, 
        tamanhoEntrada, 
        valorMaximo
        ).stdout
    )

# Salvar resultados em um arquivo CSV
with open(f'resultados{ordenador}.csv', mode='w', newline='', encoding='utf-8') as arquivo_csv:
    writer = csv.writer(arquivo_csv)
    # escrever o cabeçalho
    writer.writerow(['Algoritmo', 'TamanhoDaEntrada', 'ValorMaximo', 'TempoDeOrdenacao'])
    # escrever cada linha de resultados
    for result in results:
        # remover o cabeçalho do resultado antes de escrever no arquivo CSV
        linhas_resultado = result.strip().split('\n')[1:]
        for linha in linhas_resultado:
            colunas = linha.split()
            writer.writerow(colunas)