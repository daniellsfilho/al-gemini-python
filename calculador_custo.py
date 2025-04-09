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

llm_flash = ai.GenerativeModel(
    model_name=MODELO_FLASH
)

llm_pro = ai.GenerativeModel(
    model_name=MODELO_PRO
)

res_flash = llm_flash.generate_content("Me recomende 3 hqs da image comics")
res_pro = llm_pro.generate_content("Me recomende 3 hqs da image comics")

tokens_flash = {
    "tokens_entrada": res_flash.usage_metadata.prompt_token_count,
    "tokens_saida": res_flash.usage_metadata.candidates_token_count
}

tokens_pro = {
    "tokens_entrada": res_pro.usage_metadata.prompt_token_count,
    "tokens_saida": res_pro.usage_metadata.candidates_token_count
}

custo_total_flash = (tokens_flash["tokens_entrada"] * CUSTO_ENTRADA_FLASH) / 1000000 + (tokens_flash["tokens_saida"] * CUSTO_SAIDA_FLASH) / 1000000
custo_total_pro = (tokens_pro["tokens_entrada"] * CUSTO_ENTRADA_PRO) / 1000000 + (tokens_pro["tokens_saida"] * CUSTO_SAIDA_PRO) / 1000000

custo_total_flash = "{:.5f}".format(custo_total_flash)
custo_total_pro = "{:.5f}".format(custo_total_pro)

print(f"Custo total llm flash em dólar: {custo_total_flash}")
print(f"Custo total llm pro em dólar: {custo_total_pro}")