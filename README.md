# gpt-quizzer
Quizzer creates a multiple-choice quiz with the inputted PDF with user preferences such as the number of questions and the difficulty of the questions. It is a program for teachers to efficiently prepare for their classes. 

# Getting Started

To get started with this project, you'll need to clone the repository and set up a virtual environment. This will allow you to install the required dependencies without affecting your system-wide Python installation.

### Cloning the Repository

    git clone https://github.com/jkmathilda/gpt-quizzer.git

### Setting up a Virtual Environment

    cd ./gpt-quizzer

    pyenv versions

    pyenv local 3.11.6

    echo '.env'  >> .gitignore
    echo '.venv' >> .gitignore

    ls -la

    python -m venv .venv        # create a new virtual environment

    source .venv/bin/activate   # Activate the virtual environment

    python -V                   # Check a python version

### Install the required dependencies

    pip list

    pip install -r requirements.txt

    pip freeze | tee requirements.txt.detail

### Configure the Application

To configure the application, there are a few properties that can be set the environment

    echo 'OPENAI_API_KEY="sk-...."' >> .env

### Running the Application

    python -m streamlit run main.py

### Deactivate the virtual environment

    deactivate

# Example

<img width="1710" alt="Screenshot 2024-01-22 at 11 29 15 PM" src="https://github.com/jkmathilda/gpt-Chatbot/assets/142202145/d380faa0-687b-4411-9cfe-fc834be25994">

<img width="1710" alt="Screenshot 2024-01-22 at 11 29 19 PM" src="https://github.com/jkmathilda/gpt-Chatbot/assets/142202145/7265926f-2abb-481d-aab0-7369f75f448d">