import os
import google.generativeai as ai
from dotenv import  load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
ai.configure(api_key=CHAVE_API_GOOGLE)

MODELO_FLASH = "gemini-2.0-flash"
MODELO_PRO = "gemini-1.5-pro"

def montar_llm(modelo):

    prompt_sistema = """
        Identifique o perfil de compra para cada cliente a seguir.

        O formato de saída deve ser:

        cliente - descreva o perfil do cliente em 3 palavras
    """

    return ai.GenerativeModel(
        model_name=modelo,
        system_instruction=prompt_sistema
    )

conteudo = ''
#file = open("./dados/dados.csv") #flash
file = open("./dados/dados_extenso.csv")
lines = file.readlines()
for line in lines:
    conteudo += line

llm_escolhido = montar_llm(MODELO_FLASH)

tokens = llm_escolhido.count_tokens(conteudo)

if tokens.total_tokens > 1000:
    llm_escolhido = montar_llm(MODELO_PRO)

print(f"total de tokens: {tokens.total_tokens}")
print(f"modelo escolhido: {llm_escolhido.model_name}")

resposta = llm_escolhido.generate_content(conteudo)

print(resposta.text)