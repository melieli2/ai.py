# ai.py
Virtual Assistant - AI Assistant Project
This project is a voice-based virtual assistant powered by speech recognition and text-to-speech technology. It can process voice commands and respond with voice feedback, providing functionalities like basic commands, assistance, and more.

Features
Voice Commands: The assistant can listen to your voice commands and interpret them using SpeechRecognition.
Text-to-Speech: It responds back with a voice, utilizing pyttsx3.
Multilingual Support: It can understand commands in various languages (like Albanian in this case).
Customizable Commands: You can extend the assistant’s functionality by adding more voice commands.
Interactive: The assistant can engage in basic conversation and handle commands like "help", "stop", etc.
Requirements
To run this project locally, ensure you have the following installed:

Python 3.7+

pip (Python package manager)

The following Python libraries:

SpeechRecognition - for recognizing and interpreting voice commands
pyttsx3 - for text-to-speech functionality
pyaudio - for microphone input (may need to install additional dependencies on Windows/macOS)
Installation
Clone the repository: If you haven't cloned the repository yet, do so by running:

bash
Copy code
git clone https://github.com/yourusername/ai-assistant.git
cd ai-assistant
Install the required packages: You can install all required dependencies by running:

bash
Copy code
pip install -r requirements.txt
If you don't have a requirements.txt file, you can manually install the dependencies:

bash
Copy code
pip install SpeechRecognition pyttsx3 pyaudio
Note: On Windows, you may need to install additional dependencies for pyaudio. You can refer to PyAudio installation guide.

Usage
Running the Assistant
Run the assistant: You can start the assistant by executing the Python script:

bash
Copy code
python myapp.py
Voice Commands: The assistant will listen for voice commands. Some predefined commands include:

ndihmë: Asks for help (responses with help instructions).
shumë mirë: Acknowledges a positive response.
stop: Stops the assistant and exits the program.
Example Command Flow
When you say "ndihmë", it will respond: "Përshëndetje! Unë mund të të ndihmoj me komandat..."
Saying "stop" will make the assistant say "Po ndalem tani. Mirupafshim!" and exit.
