import google.generativeai as genai

MODELO_FLASH = "gemini-1.5-flash"
MODELO_PRO = "gemini-1.5-pro"

CUSTO_ENTRADA_FLASH = 0.075
CUSTO_ENTRADA_PRO = 0.30

CUSRTO_ENTRADA_PRO = 3.5
CUSTO_SAIDA_PRO = 10.50

model_pro = genai.get_model(f"models/{MODELO_PRO}")
limites_modelo_pro = {
    "tonkens_entrada": model_pro.input_token_limit,
    "tonkens_saida": model_pro.output_token_limit,
}

print(f"Limite do modelo pro: {limites_modelo_pro}")

llm_flashe = genai.GenerativeModel(
    f"models/{MODELO_FLASH}",
)

quantidade_tonkens = llm_flashe.count_tokens("Olá, tudo bem?")
print(f"Quantidade de tonkens: {quantidade_tonkens}")

resposta = llm_flashe.generate_content("Olá, tudo bem?")
tonkens_prompt = resposta.usage_metadata.prompt_token_count
tonkens_resposta = resposta.usage_metadata.candidates_token_count
custo_total = (tonkens_prompt * CUSTO_ENTRADA_FLASH) / 1000000 + (tonkens_resposta * CUSTO_SAIDA_PRO) / 1000000
print(f"Custo total $ Flash: {custo_total}")

custo_total = (tonkens_prompt * CUSTO_ENTRADA_PRO) / 1000000 + (tonkens_resposta * CUSTO_SAIDA_PRO) / 1000000
print(f"Custo total $ Pro: {custo_total}")