import os
import google.generativeai as ai
from dotenv import  load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
ai.configure(api_key=CHAVE_API_GOOGLE)

MODELO_FLASH = "gemini-2.0-flash"
MODELO_PRO = "gemini-1.5-pro"

ai_flash = ai.get_model(f"models/{MODELO_FLASH}")
ai_pro = ai.get_model(f"models/{MODELO_PRO}")

limites_token_flash = {
    "limite_entrada": ai_flash.input_token_limit,
    "limite_saida": ai_flash.output_token_limit
}

limites_token_pro = {
    "limite_entrada": ai_pro.input_token_limit,
    "limite_saida": ai_pro.output_token_limit
}

print(f"limites de tokens flash: {limites_token_flash}")
print(f"limites de tokens pro: {limites_token_pro}")
print("")

llm_flash = ai.GenerativeModel(
    model_name=MODELO_FLASH
)

llm_pro = ai.GenerativeModel(
    model_name=MODELO_PRO
)

qtd_tokens_flash = llm_flash.count_tokens("O que é uma hq de capa dura?")
print(f"A quantidade de tokens para flash é: {qtd_tokens_flash}")

qtd_tokens_pro = llm_pro.count_tokens("O que é uma hq de capa dura?")
print(f"A quantidade de tokens para pro é: {qtd_tokens_flash}")