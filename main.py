from chatbot import chat_with_patient
from data_processing import summarize_notes
from diagnostic import generate_diagnostic_hypotheses

def main():
    patient_query = "Describe your symptoms and medical history."  # This can be dynamic based on user input
    chat_response = chat_with_patient(patient_query)
    print("Chatbot Response:", chat_response)

    notes = summarize_notes(chat_response)
    print("Summarized Notes:", notes)

    hypotheses = generate_diagnostic_hypotheses(notes)
    print("Diagnostic Hypotheses:", hypotheses)

if __name__ == "__main__":
    main()
