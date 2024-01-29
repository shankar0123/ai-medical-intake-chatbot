def generate_diagnostic_hypotheses(summarized_notes):
    diagnostic_output = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"Based on the following patient notes, what are the possible diagnoses?\n\n{summarized_notes}",
        max_tokens=150
    )
    return diagnostic_output.choices[0].text.strip()
