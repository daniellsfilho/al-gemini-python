import os
import google.generativeai as ai
from dotenv import  load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
ai.configure(api_key=CHAVE_API_GOOGLE)

MODELO_FLASH = "gemini-2.0-flash"
MODELO_PRO = "gemini-1.5-pro"

CUSTO_ENTRADA_FLASH = 0.075
CUSTO_SAIDA_FLASH = 0.30

CUSTO_ENTRADA_PRO = 3.5
CUSTO_SAIDA_PRO = 10.50

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