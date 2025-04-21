import os
import google.generativeai as ai
from google.api_core.exceptions import NotFound
from dotenv import  load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
ai.configure(api_key=CHAVE_API_GOOGLE)

MODELO = "gemini-2.0-flash"

def carregarArquivo(caminho):
    try:
        with open(caminho, "r") as arquivo:
            return arquivo.read()
    except IOError as ioError:
        print(f"Erro ao abrir arquivo: {ioError}")

def escreverArquivo(caminho, conteudo):
    try:
        with open(caminho, "w", encoding="utf-8") as arquivo:
            arquivo.write(conteudo)
    except IOError as ioError:
        print(f"Erro ao escrever arquivo: {ioError}")

def analisarSentimento(produto):

    prompt_sistema = f"""
        Você é um analisador de sentimentos de avaliações de produtos.
        Escreva um parágrafo com até 50 palavras resumindo as avaliações e
        depois atribua qual o sentimento geral para o produto.
        Identifique também 3 pontos fortes e 3 pontos fracos identificados a partir das avaliações.

        # Formato de Saída

        Nome do Produto:
        Resumo das Avaliações:
        Sentimento Geral: [utilize aqui apenas Positivo, Negativo ou Neutro]
        Ponto fortes: lista com três bullets
        Pontos fracos: lista com três bullets
    """

    try:
        llm_flash = ai.GenerativeModel(
            model_name=MODELO,
            system_instruction=prompt_sistema
        )

        caminho_arquivo = f"./dados/avaliacoes-{produto}.txt"

        prompt_usuario = carregarArquivo(caminho_arquivo)

        resposta = llm_flash.generate_content(prompt_usuario)
        print(f"Salvando arquivo resposta-{produto}")

        caminho_arquivo_resposta = f"./dados/resposta-{produto}"
        escreverArquivo(caminho_arquivo_resposta, resposta.text)
    except NotFound as e:
        print(f"Erro ao carregar modelo: {e}")

def main():
    produtos = ["Camisetas de algodão orgânico", "Jeans feitos com materiais reciclados", "Maquiagem mineral"]

    for produto in produtos:
        analisarSentimento(produto)

if __name__ == "__main__":
    main()