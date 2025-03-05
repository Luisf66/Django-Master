import openai

client = openai.OpenAI(api_key='sk-proj-9f_bHwDp-3b4eFTz_kTU21V-wCpMej0SH7Y0oQ43GwMmkvtn4DzdNZJLmOMmvcibJRCS9fI9xBT3BlbkFJZYiFlMcyMQmLFePB-HkJvZBTUEUiO06nHcsD0k3MC9r8f1g-MfYa2AjqWKQE-CD0DkvKXTd0A')  # Crie um cliente OpenAI

def get_car_ai_bio(model, brand, year):
    prompt = f"Me descreva um {brand} {model} {year} com detalhes específicos em até 100 caracteres."

    response = client.chat.completions.create(  # Novo formato da API OpenAI 1.0+
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content  # Novo acesso ao conteúdo da resposta

