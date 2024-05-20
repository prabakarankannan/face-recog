import streamlit as st

def home():
    st.markdown("""

# Face Recognition Application

A web application using face recognition in Python with Streamlit.

## Introduction

This project utilizes the face recognition Python module to build a web app powered by Streamlit. It allows users to perform face recognition tasks interactively.

## Features

- Face detection and recognition
- Streamlit for a user-friendly web interface

## Installation

1. Clone the repository:

```bash
git clone https://github.com/prabakarankannan/face-recog.git
cd face-recog
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the Streamlit app:

```bash
streamlit run app.py
```

Visit `http://localhost:8501` in your browser to access the web app.

## Usage

- Open the web app in your browser.
- You can use register page to register your face in database
- You can use login page to see if user is registered or not
- All the activities like login, register will be stored in log file


        """)
