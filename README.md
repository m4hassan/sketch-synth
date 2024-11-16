# Sketch-Synth: Hyper Realistic Portrait Generation

## Overview

**Sketch-Synth** is a web application that allows users to generate hyper-realistic portraits from hand-drawn sketches. Utilizing a StableDiffusion model through the ModelsLab API, Sketch-Synth provides a seamless and effective solution for creating high-quality images from simple sketches.

## Features

- **User Registration and Authentication:** Users can register, log in, and manage their profiles.
- **Sketch Upload:** Users can upload their hand-drawn sketches to the platform.
- **Realistic Portrait Generation:** The application uses the ModelsLab API to convert sketches into hyper-realistic portraits.
- **Gallery:** Users can view all their generated images in a personal gallery.
- **User Profile:** Users can view and update their profile information.

## Tech Stack

- **Backend:** Django
- **Frontend:** HTML, Tailwind CSS, JavaScript
- **Storage:** Firebase Storage
- **API:** ModelsLab API for image generation

## Installation

### Prerequisites

- Python 3.8+
- Firebase account
- ModelsLab API access

### Steps

1. **Clone the repository:**
    ```sh
    git clone https://github.com/yourusername/sketch-synth.git
    cd sketch-synth
    ```

2. **Create a virtual environment:**
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the dependencies:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Configure Firebase:**
    - Create a Firebase project and enable Firebase Storage.
    - Add your Firebase credentials to `firebase.py` file.

    ```python
    # firebase.py
    import pyrebase

    FIREBASE_CONFIG = {
        "apiKey": "your_api_key",
        "authDomain": "your_project_id.firebaseapp.com",
        "projectId": "your_project_id",
        "storageBucket": "your_project_id.appspot.com",
        "messagingSenderId": "your_messaging_sender_id",
        "appId": "your_app_id",
        "measurementId": "your_measurement_id",
        "databaseURL": ""
    }
    ```

5. **Run database migrations:**
    ```sh
    python manage.py migrate
    ```

6. **Create a superuser:**
    ```sh
    python manage.py createsuperuser
    ```

7. **Run the development server:**
    ```sh
    python manage.py runserver
    ```

## Usage

1. **Register/Login:**
   - Register for an account or log in if you already have one.

2. **Upload a Sketch:**
   - Navigate to the sketch upload page.
   - Upload your hand-drawn sketch and provide the necessary prompts.
   - Submit the form to generate a hyper-realistic portrait.

3. **View Gallery:**
   - View all your generated images in your personal gallery.

