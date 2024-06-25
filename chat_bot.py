import difflib

def carregar_perguntas(nome_arquivo):
    perguntas_respostas = {}
    with open(nome_arquivo, encoding="utf-8") as f:
        for linha in f:
            pergunta, resposta = linha.strip().split("?")
            perguntas_respostas[pergunta.strip()] = resposta.strip()
    return perguntas_respostas

def encontrar_pergunta_similar(perguntas, pergunta_usuario, limiar=0.6):
    pergunta_usuario = pergunta_usuario.lower()
    perguntas_similares = difflib.get_close_matches(pergunta_usuario, perguntas.keys(), n=1, cutoff=limiar)
    if perguntas_similares:
        return perguntas_similares[0]
    return None

perguntas_respostas = carregar_perguntas("perguntas.txt")
print("Perguntas carregadas:")
for pergunta in perguntas_respostas:
    print(f"- {pergunta}")

while True:
    pergunta_usuario = input("\nDigite sua pergunta (ou 'sair' para encerrar): ").strip()
    if pergunta_usuario.lower() == 'sair':
        break

    pergunta_similar = encontrar_pergunta_similar(perguntas_respostas, pergunta_usuario)

    if pergunta_similar:
        resposta = perguntas_respostas[pergunta_similar]
        print(f"Resposta: {resposta}")
    else:
        print("Desculpe, não encontrei uma resposta para sua pergunta.")
