import subprocess
import sys
import os
import webbrowser

def main():
    # Path to your quiz.py
    script_path = os.path.join(os.path.dirname(__file__), "quiz.py")

    # Launch Streamlit
    process = subprocess.Popen([sys.executable, "-m", "streamlit", "run", script_path])

    # Open browser automatically
    webbrowser.open("http://localhost:8501")

    # Keep the process alive
    process.wait()

if __name__ == "__main__":
    main()