import sys
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

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Erro: Nenhuma pergunta fornecida.")
        sys.exit(1)
    
    pergunta_usuario = sys.argv[1]
    perguntas_respostas = carregar_perguntas("perguntas.txt")
    pergunta_similar = encontrar_pergunta_similar(perguntas_respostas, pergunta_usuario)

    if pergunta_similar:
        resposta = perguntas_respostas[pergunta_similar]
        print(f"Pergunta: {pergunta_usuario}")
        print(f"Resposta: {resposta}")
    else:
        print(f"Pergunta: {pergunta_usuario}")
        print("Desculpe, não encontrei uma resposta para sua pergunta.")
