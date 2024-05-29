import os

def speak_text(text):
    powershell_command = f"powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{text}')"
    os.system(powershell_command)

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 created by Komal")
    while True:
      x = input("Enter what you want to say: ")
      if x=="q":
          powershell_command = f"powershell Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak('{'bye bye friend'}')"
          os.system(powershell_command)
          break
      speak_text(x)

# speak_text("hello patrika")



