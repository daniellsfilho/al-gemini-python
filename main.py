import os
import google.generativeai as ai
from dotenv import  load_dotenv

load_dotenv()

CHAVE_API_GOOGLE = os.getenv("GEMINI_API_KEY")
ai.configure(api_key=CHAVE_API_GOOGLE)
MODELO_ESCOLHIDO = "gemini-2.0-flash"

prompt = "Liste apenas os nomes dos produtos e ofereça uma breve descrição"

config_modelo = {
    "temperature": 2.0,
    "top_p": 0.9,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

llm = ai.GenerativeModel(
    model_name=MODELO_ESCOLHIDO,
    system_instruction=prompt
)

pergunta = "Liste três produtos de moda masculina sustentável para ir em um casamento"

resposta = llm.generate_content(pergunta)

print(resposta.text)