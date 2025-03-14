import os
import google.generativeai as ai
from dotenv import  load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
ai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO = "gemini-2.0-flash"



def categorizar_produtos(produto, lista_categorias_possiveis):
    prompt = f"""
                Você é um categorizador de produtos.
                Você deve assumir as categorias presentes na lista abaixo.
                # Lista de Categorias Válidas
                {lista_categorias_possiveis.split(",")}
                # Formato da Saída
                Produto: Nome do Produto
                Categoria: apresente a categoria do produto
                # Exemplo de Saída
                Produto: Escova elétrica com recarga solar
                Categoria: Eletrônicos Verdes
            """

    llm = ai.GenerativeModel(
        model_name=MODELO_ESCOLHIDO,
        system_instruction=prompt
    )

    resposta = llm.generate_content(produto)
    return resposta.text

def main():
    lista_categorias_possiveis = "Mangá,HQ,Ficção,Livro,Fantasia,Romance,Drama,Histórico"
    produto = input("Insira o produto que deseja classificar: ")

    while produto != "":
        print(categorizar_produtos(produto, lista_categorias_possiveis))
        produto = input("Insira o produto que deseja classificar: ")

if __name__ == "__main__":
    main()


