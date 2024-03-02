# Cafe Rating Flask App

This Flask application allows users to submit information about different cafes, including their name, location, opening and closing times, and ratings for coffee, WiFi, and power availability. The app uses Flask, Flask-WTF for form handling, Flask-Bootstrap for styling, and saves the submitted cafe data to a CSV file. Users can also view a list of all submitted cafes.

## Features

- **Form Submission for New Cafes**: Users can submit details about new cafes through a form, including ratings for coffee quality, WiFi strength, and power outlet availability.
- **Data Persistence**: Submitted data is saved to a CSV file, making it easy to retain and access information about cafes.
- **Validation and Feedback**: The form includes validation for required fields and correct data formats, ensuring that all necessary information is provided correctly.
- **Dynamic List of Cafes**: Users can view a dynamically generated list of all submitted cafes, including their details and ratings.

## Technologies Used

- **Python 3.x**: The primary programming language used.
- **Flask**: A micro web framework written in Python for building web applications.
- **Flask-WTF**: An extension for Flask that integrates with WTForms for form handling, validation, and rendering.
- **Flask-Bootstrap**: An extension for Flask that integrates Bootstrap for styling.
- **WTForms**: A flexible forms validation and rendering library for Python web development.
- **CSV**: To store and retrieve cafe data.

## How to Run the Application

1. **Clone the repository** to your local machine.

2. **Ensure Python is installed** on your computer.

3. **Install required packages** by running:

   ```bash
   pip install Flask Flask-WTF Flask-Bootstrap
# Cafe-Rating-Flask-App
