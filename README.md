# Speech Recognizer using Vosk and PyAudio

## Overview

This project implements a speech recognition system using the **Vosk API** and **PyAudio** library. The program continuously listens to audio input from the microphone, processes it using the Vosk speech recognition model, and prints the recognized text in real-time. The program stops when the user says "exit" or interrupts the program manually.

---

## Features

1. **Continuous Listening:**

   - The program listens to audio input continuously and processes speech in real-time.

2. **Real-Time Speech Recognition:**

   - Converts spoken words into text instantly.

3. **Customizable Model:**

   - Uses a Vosk speech recognition model that can be replaced with models for other languages or improved accuracy.

4. **Graceful Termination:**

   - Allows the user to exit by saying "exit" or pressing `Ctrl+C`.

5. **Error Handling:**

   - Handles initialization errors and audio processing issues gracefully.

---

## Requirements

### Dependencies

1. **Python (>= 3.7)**
2. **Vosk API**
   - Install using: `pip install vosk`
3. **PyAudio**
   - Install using: `pip install pyaudio`
   - On some systems (e.g., Linux), additional dependencies might be required to install PyAudio. Use your package manager to install them (e.g., `sudo apt install portaudio19-dev` on Ubuntu).

### Hardware Requirements

- A working microphone to capture audio input.

---

## Installation and Setup

1. **Clone the Repository:**

   ```bash
   git clone <repository_url>
   cd <repository_name>
   ```

2. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Download Vosk Model:**

   - Download a pre-trained Vosk model from the [Vosk models repository](https://alphacephei.com/vosk/models).
   - Example: For English (Indian accent), download `vosk-model-en-in-0.5`.
   - Extract the model into the project directory and note the path (e.g., `models/vosk-model-en-in-0.5`).

4. **Run the Program:**

   ```bash
   python src/speech_recognition.py
   ```

---

## Usage

1. Start the program by running the script.
2. Speak into the microphone. The program will recognize and display your speech as text in real-time.
3. Say "exit" to terminate the program or press `Ctrl+C` to stop manually.

---

## Code Structure

### Main Components

1. **SpeechRecognizer Class:**

   - Handles model initialization, audio stream setup, continuous listening, and resource cleanup.

2. **listen\_continuous Method:**

   - Processes microphone input in real-time and yields recognized text.

3. **Graceful Resource Management:**

   - Ensures proper release of audio resources upon termination.

### Code Highlights

- **Initialization:**

  ```python
  self.stream = self.audio.open(
      rate=16000,
      channels=1,
      format=pyaudio.paInt16,
      input=True,
      frames_per_buffer=4000
  )
  ```

  Sets up the PyAudio stream for real-time audio capture.

- **Continuous Listening:**

  ```python
  while True:
      data = self.stream.read(4000, exception_on_overflow=False)
      if self.recognizer.AcceptWaveform(data):
          result = json.loads(self.recognizer.Result())
          yield result.get("text", "")
  ```

  Captures audio continuously, processes it using Vosk, and yields the recognized text.

- **Termination:**

  ```python
  if "exit" in text.lower():
      break
  ```

  Stops the program when "exit" is spoken.

---

## Example Output

### Running the Program:

```bash
Start speaking! (Say 'exit' to quit)
You said: hello
You said: how are you
You said: exit
Exiting...
```

---

## Troubleshooting

### Common Issues:

1. **PyAudio Installation Errors:**

   - On Linux, install development headers for PortAudio:
     ```bash
     sudo apt install portaudio19-dev
     ```
   - On macOS, use Homebrew:
     ```bash
     brew install portaudio
     ```
   - Then, reinstall PyAudio using `pip install pyaudio`.

2. **Microphone Not Working:**

   - Ensure your microphone is properly configured and recognized by your system.

3. **Low Recognition Accuracy:**

   - Use a more accurate Vosk model for your language or accent.

---

## Customization

1. **Change the Model:**
   - Replace `model_path` with the path to a different Vosk model.
2. **Adjust Audio Settings:**
   - Modify `rate`, `channels`, or `frames_per_buffer` in the `self.audio.open()` method for better compatibility with your microphone.

---

## License

This project is licensed under the MIT License. Feel free to use, modify, and distribute it as needed.

---

## Acknowledgments

1. [Vosk API](https://alphacephei.com/vosk) - Speech recognition toolkit.
2. [PyAudio](https://people.csail.mit.edu/hubert/pyaudio/) - Library for audio stream handling.
3. Open-source contributors for making these tools available to the community.

