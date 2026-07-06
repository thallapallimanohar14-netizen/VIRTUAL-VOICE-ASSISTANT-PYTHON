{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "067eaabc-adfe-4b46-bd94-0f9c53af1bee",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: SpeechRecognition in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (3.17.0)\n",
      "Requirement already satisfied: typing-extensions in c:\\programdata\\anaconda3\\lib\\site-packages (from SpeechRecognition) (4.12.2)\n",
      "Requirement already satisfied: standard-aifc in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from SpeechRecognition) (3.13.0)\n",
      "Requirement already satisfied: audioop-lts in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from SpeechRecognition) (0.2.2)\n",
      "Requirement already satisfied: standard-chunk in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from standard-aifc->SpeechRecognition) (3.13.0)\n",
      "Note: you may need to restart the kernel to use updated packages.\n",
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pyttsx3 in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (2.99)\n",
      "Requirement already satisfied: comtypes in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pyttsx3) (1.4.16)\n",
      "Requirement already satisfied: pypiwin32 in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pyttsx3) (223)\n",
      "Requirement already satisfied: pywin32 in c:\\programdata\\anaconda3\\lib\\site-packages (from pyttsx3) (308)\n",
      "Note: you may need to restart the kernel to use updated packages.\n",
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: PyAudio in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (0.2.14)\n",
      "Note: you may need to restart the kernel to use updated packages.\n",
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: wikipedia in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (1.4.0)\n",
      "Requirement already satisfied: beautifulsoup4 in c:\\programdata\\anaconda3\\lib\\site-packages (from wikipedia) (4.12.3)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.0.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from wikipedia) (2.32.3)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (2.3.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.0.0->wikipedia) (2025.4.26)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from beautifulsoup4->wikipedia) (2.5)\n",
      "Note: you may need to restart the kernel to use updated packages.\n",
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pyjokes in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (0.8.3)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install SpeechRecognition\n",
    "%pip install pyttsx3\n",
    "%pip install PyAudio\n",
    "%pip install wikipedia\n",
    "%pip install pyjokes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "8a5ddd70-3b23-4038-bb16-aaa301913f0d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "All libraries installed successfully!\n"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "import pyttsx3\n",
    "import wikipedia\n",
    "import pyjokes\n",
    "\n",
    "print(\"All libraries installed successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "756610c5-1a02-4e52-b503-000d822ab63d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Defaulting to user installation because normal site-packages is not writeable\n",
      "Requirement already satisfied: pywhatkit in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (5.4)\n",
      "Requirement already satisfied: Pillow in c:\\programdata\\anaconda3\\lib\\site-packages (from pywhatkit) (11.1.0)\n",
      "Requirement already satisfied: pyautogui in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pywhatkit) (0.9.54)\n",
      "Requirement already satisfied: requests in c:\\programdata\\anaconda3\\lib\\site-packages (from pywhatkit) (2.32.3)\n",
      "Requirement already satisfied: wikipedia in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pywhatkit) (1.4.0)\n",
      "Requirement already satisfied: Flask in c:\\programdata\\anaconda3\\lib\\site-packages (from pywhatkit) (3.1.0)\n",
      "Requirement already satisfied: Werkzeug>=3.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from Flask->pywhatkit) (3.1.3)\n",
      "Requirement already satisfied: Jinja2>=3.1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from Flask->pywhatkit) (3.1.6)\n",
      "Requirement already satisfied: itsdangerous>=2.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from Flask->pywhatkit) (2.2.0)\n",
      "Requirement already satisfied: click>=8.1.3 in c:\\programdata\\anaconda3\\lib\\site-packages (from Flask->pywhatkit) (8.1.8)\n",
      "Requirement already satisfied: blinker>=1.9 in c:\\programdata\\anaconda3\\lib\\site-packages (from Flask->pywhatkit) (1.9.0)\n",
      "Requirement already satisfied: colorama in c:\\programdata\\anaconda3\\lib\\site-packages (from click>=8.1.3->Flask->pywhatkit) (0.4.6)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\programdata\\anaconda3\\lib\\site-packages (from Jinja2>=3.1.2->Flask->pywhatkit) (3.0.2)\n",
      "Requirement already satisfied: pymsgbox in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pyautogui->pywhatkit) (2.0.1)\n",
      "Requirement already satisfied: pytweening>=1.0.4 in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pyautogui->pywhatkit) (1.2.0)\n",
      "Requirement already satisfied: pyscreeze>=0.1.21 in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pyautogui->pywhatkit) (1.0.1)\n",
      "Requirement already satisfied: pygetwindow>=0.0.5 in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pyautogui->pywhatkit) (0.0.9)\n",
      "Requirement already satisfied: mouseinfo in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pyautogui->pywhatkit) (0.1.3)\n",
      "Requirement already satisfied: pyrect in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from pygetwindow>=0.0.5->pyautogui->pywhatkit) (0.2.0)\n",
      "Requirement already satisfied: pyperclip in c:\\users\\manohar thallapalli\\appdata\\roaming\\python\\python313\\site-packages (from mouseinfo->pyautogui->pywhatkit) (1.11.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->pywhatkit) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->pywhatkit) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->pywhatkit) (2.3.0)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\programdata\\anaconda3\\lib\\site-packages (from requests->pywhatkit) (2025.4.26)\n",
      "Requirement already satisfied: beautifulsoup4 in c:\\programdata\\anaconda3\\lib\\site-packages (from wikipedia->pywhatkit) (4.12.3)\n",
      "Requirement already satisfied: soupsieve>1.2 in c:\\programdata\\anaconda3\\lib\\site-packages (from beautifulsoup4->wikipedia->pywhatkit) (2.5)\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "%pip install pywhatkit"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "e22f631f-c6de-4574-9c26-e62a1d14efb6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "pywhatkit installed successfully!\n"
     ]
    }
   ],
   "source": [
    "import pywhatkit\n",
    "print(\"pywhatkit installed successfully!\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "5f77b402-a1e2-40bd-a964-b125ab0a9c33",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Assistant: Hello! I am your Voice Assistant.\n",
      "Listening...\n",
      "No speech detected. Try again.\n",
      "Listening...\n",
      "No speech detected. Try again.\n",
      "Listening...\n",
      "No speech detected. Try again.\n",
      "Listening...\n",
      "You said: hello\n",
      "Assistant: Hello! How can I help you?\n",
      "Listening...\n",
      "You said: what is the time\n",
      "Assistant: The time is 12:46 AM\n",
      "Listening...\n",
      "You said: what is the date\n",
      "Assistant: Today's date is 06 July 2026\n",
      "Listening...\n",
      "No speech detected. Try again.\n",
      "Listening...\n",
      "You said: exit\n",
      "Assistant: Goodbye!\n"
     ]
    }
   ],
   "source": [
    "import speech_recognition as sr\n",
    "import pyttsx3\n",
    "import datetime\n",
    "\n",
    "# Initialize voice engine\n",
    "engine = pyttsx3.init()\n",
    "\n",
    "def speak(text):\n",
    "    print(\"Assistant:\", text)\n",
    "    engine.say(text)\n",
    "    engine.runAndWait()\n",
    "\n",
    "# Welcome message\n",
    "speak(\"Hello! I am your Voice Assistant.\")\n",
    "\n",
    "recognizer = sr.Recognizer()\n",
    "\n",
    "while True:\n",
    "    try:\n",
    "        with sr.Microphone() as source:\n",
    "            print(\"Listening...\")\n",
    "            recognizer.adjust_for_ambient_noise(source, duration=1)\n",
    "            audio = recognizer.listen(source, timeout=5, phrase_time_limit=5)\n",
    "\n",
    "        command = recognizer.recognize_google(audio).lower()\n",
    "        print(\"You said:\", command)\n",
    "\n",
    "        if \"hello\" in command:\n",
    "            speak(\"Hello! How can I help you?\")\n",
    "\n",
    "        elif \"time\" in command:\n",
    "            current_time = datetime.datetime.now().strftime(\"%I:%M %p\")\n",
    "            speak(\"The time is \" + current_time)\n",
    "\n",
    "        elif \"date\" in command:\n",
    "            today = datetime.datetime.now().strftime(\"%d %B %Y\")\n",
    "            speak(\"Today's date is \" + today)\n",
    "\n",
    "        elif \"exit\" in command or \"stop\" in command:\n",
    "            speak(\"Goodbye!\")\n",
    "            break\n",
    "\n",
    "        else:\n",
    "            speak(\"Sorry, I did not understand.\")\n",
    "\n",
    "    except sr.WaitTimeoutError:\n",
    "        print(\"No speech detected. Try again.\")\n",
    "\n",
    "    except Exception as e:\n",
    "        print(\"Error:\", e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a42055d5-524d-4763-ad07-c1ee5d2296ae",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.5"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
