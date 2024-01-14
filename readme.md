# Jarvis Virtual Assistant

## Introduction

Jarvis is a basic virtual assistant written in Python using the pyttsx3 text-to-speech library, speech_recognition for audio recognition, and smtplib for sending emails. It performs various tasks based on voice commands.

## Features

- **Voice Recognition:** Utilizes speech_recognition to understand voice commands.
- **Wikipedia Search:** Provides brief information based on user queries using Wikipedia.
- **Web Browsing:** Opens YouTube, Google, or GeeksforGeeks in the default web browser.
- **Music Player:** Plays the first song from the specified music directory.
- **Current Time:** Tells the current time.
- **Code Editor:** Opens Visual Studio Code.
- **Email Sender:** Sends an email to a predefined recipient.

## Prerequisites

- Python 3.x
- pyttsx3
- speech_recognition
- smtplib
- [Additional libraries mentioned in your code]

## Setup

1. Clone the repository:

   ```bash
   git clone [repository_url]

2. Install required Python libraries:

    ```bash
    pip install pyttsx3 speech_recognition


3. Create a text file named __password.txt__ and add your email password.

4. Run the script:

    ```bash
    python jarvis.py

## Usage

1. Upon running the script, Jarvis will greet you and listen for commands.
 
2. Speak a command, such as:

- "Search Wikipedia for [query]."
- "Open YouTube."
- "Play music."
- "What's the time?"
- "Send an email to Kajal."

3. Jarvis will respond accordingly, executing the requested action.

## Notes

1. Make sure to set up the password.txt file with your email password securely.
2. Adjust the music directory path in the code to match your system.
