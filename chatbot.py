import openai

openai.api_key = 'YOUR_OPENAI_API_KEY'

def chat_with_patient(patient_query):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=patient_query,
        max_tokens=150
    )
    return response.choices[0].text.strip()
