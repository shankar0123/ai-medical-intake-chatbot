# ai-medical-intake-chatbot

Project Overview
The AI Medical Chatbot is an interactive web application designed to simulate a medical intake process. It uses OpenAI's GPT-3.5 model to understand and process user inputs, asking about symptoms and medical history, and providing potential diagnostic hypotheses. You can update this to use GPT4 or any latest model provided by OpenAI.

Disclaimer
This chatbot is for demonstration and educational purposes only and should not be used for actual medical diagnosis or treatment. Always consult with a professional healthcare provider for medical advice.

Dependencies

Python 3.x
Flask
OpenAI API Key


Installation

1) Clone the Repository

git clone https://github.com/shankar0123/ai-medical-intake-chatbot/tree/main
cd ai-medical-chatbot

2) Install Dependencies

Ensure Python is installed on your system.
Install Flask and other required libraries:

pip install Flask openai

3) OpenAI API Key

Obtain an API key from OpenAI.
Replace 'YOUR_OPENAI_API_KEY' in chatbot.py with your actual API key.

Running the Application

1) Start the Flask Server

Execute the following command in the project's root directory:

python app.py

This starts the Flask server.

2) Access the Web Interface

Open a browser and navigate to http://127.0.0.1:5000/.
Interact with the chatbot through the web interface.

Usage

Input your symptoms and medical history as prompted by the chatbot.
The chatbot will process the information and provide potential diagnostic hypotheses.
Remember, these diagnoses are hypothetical and for educational purposes only.

Contributing
Contributions to the AI Medical Chatbot project are welcome. Please feel free to fork the repository, make changes, and submit pull requests.

License
This project is licensed under the MIT License - see the LICENSE.md file for details.

