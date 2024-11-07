import pyttsx3
from datetime import datetime
import random
import webbrowser
import os

try:
    from speech_recognition import Recognizer, Microphone, UnknownValueError, RequestError
except ImportError:
    print("Module 'speech_recognition' is missing. Install it with 'pip install SpeechRecognition'.")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def fol_tekstin(tekst):
    """Speak the given text out loud."""
    engine.say(tekst)
    engine.runAndWait()

def njoh_komanden():
    """Listen and recognize spoken commands."""
    recognizer = Recognizer()
    with Microphone() as source:
        print("Të lutem, thuaj diçka...")
        audio = recognizer.listen(source)

    try:
        komanda = recognizer.recognize_google(audio, language='sq-AL')
        print(f"Ke thënë: {komanda}")
        return komanda.lower()
    except UnknownValueError:
        print("Nuk mund të kuptoj komandën. Mund të provosh përsëri?")
        fol_tekstin("Nuk mund të kuptoj komandën. Mund të provosh përsëri?")
        return None
    except RequestError:
        print("Ka ndodhur një gabim me shërbimin.")
        fol_tekstin("Ka ndodhur një gabim me shërbimin.")
        return None

def reagimi_ne_komanden(komanda, monthtime=None):
    """Respond based on the recognized command."""
    if komanda is None:
        return True

    if 'përshëndetje' in komanda:
        fol_tekstin("Përshëndetje! Si mund të ndihmoj?")
    elif 'ora' in komanda:
        fol_tekstin(f"Ora është {datetime.now().strftime('%H:%M')}.")
    elif 'data' in komanda:
        fol_tekstin(f"Sot është {datetime.now().strftime('%d-%m-%Y')}.")
    elif 'fakt' in komanda:
        facts = [
            "Delfinët flenë vetëm me një sy të hapur.",
            "Bletët mund të dallojnë fytyrat njerëzore.",
            "Zemra e një breshke rrah vetëm 6 herë në minutë.",
        ]
        fol_tekstin(random.choice(facts))
    elif 'shaka' in komanda:
        jokes = [
            "Pse nuk mund të hajnë akullore pinguinët? Sepse gjithmonë e hedhin në det!",
            "Çfarë bëri kompjuteri kur u mërzit? U bë me humor byte!",
        ]
        fol_tekstin(random.choice(jokes))
    elif 'motivim' in komanda:
        quotes = [
            "Mos ndaloni së ëndërruari, ëndrrat janë fillimi i suksesit.",
            "Nëse sot nuk është dita jote, mos u shqetëso. Nesër mund të jetë.",
        ]
        fol_tekstin(random.choice(quotes))
    elif 'hap shfletuesin' in komanda:
        fol_tekstin("Po hap shfletuesin.")
        webbrowser.open("https://www.google.com")
    elif 'kalkulo' in komanda:
        fol_tekstin("Çfarë dëshiron të kalkulosh? Thuaj një problem, si 'sa bën 5 plus 3'")
        try:
            calc_command = njoh_komanden()
            if calc_command:
                answer = eval(calc_command.replace('plus', '+').replace('minus', '-').replace('herë', '*').replace('pjesëtuar', '/'))
                fol_tekstin(f"Rezultati është {answer}")
        except Exception as e:
            fol_tekstin("Më vjen keq, nuk mund të kalkuloj atë.")
    elif 'hap dokumentin' in komanda:
        file_path = "C:/Users/Admin/Documents/example.txt"  # Path to a file you want to open
        try:
            os.startfile(file_path)
            fol_tekstin("Po hap dokumentin.")
        except FileNotFoundError:
            fol_tekstin("Më vjen keq, nuk gjeta dokumentin.")
    elif 'stop' in komanda:
        fol_tekstin("Po ndalem tani. Mirupafshim!")
        return False
    else:
        fol_tekstin("Nuk e kuptova komandën. Mund të provosh përsëri?")
    return True

def start_app():
    """Run the voice assistant application."""
    fol_tekstin("Mirësevini! Thjesht flisni dhe unë do të përgjigjem.")
    while True:
        komanda = njoh_komanden()
        if not reagimi_ne_komanden(komanda):
            break

start_app()