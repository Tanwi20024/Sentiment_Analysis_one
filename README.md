# Sentiment_Analysis_one
To Analyse sentences and its emotion

SentimentAI — Emotion Analyzer
This is a simple Django web application that uses TextBlob to perform sentiment analysis on user-provided text. It provides a user-friendly interface to analyze text, determine its polarity (positive, negative, neutral) and subjectivity, and keeps a history of recent analyses.
Features
Real-time sentiment analysis using TextBlob.
Displays polarity, subjectivity, word count, and sentence count.
Visually represents sentiment (emoji, color-coded).
Stores and displays recent analysis history.
Responsive web interface.
Setup and Run
Prerequisites
Python 3.8+
Django
TextBlob
pyngrok (for local development/exposure)
Installation
Clone this repository:
git clone <repository_url>
cd sentiment_project
Install the required Python packages:
pip install -r requirements.txt # (assuming a requirements.txt is generated or packages installed as in notebook)
# or manually: pip install django textblob pyngrok
Download TextBlob corpora (if not already done):
python -m textblob.download_corpora
Run Django migrations:
python manage.py migrate
Start the Django development server:
python manage.py runserver
Accessing the Application
If running locally, navigate to http://127.0.0.1:8000 in your web browser.
If using pyngrok (as in a Colab environment), a public URL will be provided upon successful tunnel creation.
Usage
Enter text into the provided text area.
Click 'Analyze Sentiment' to get the analysis results.
The results will show the sentiment (Positive, Negative, Neutral), polarity score, subjectivity score, and other text statistics.
Recent analyses will be stored and displayed in the 'Recent Analyses' section.
Project Structure
sentiment_project/: Main Django project configuration.
analyzer/: Django app containing views, templates, and static files for the sentiment analysis functionality.
views.py: Contains the logic for sentiment analysis and rendering.
urls.py: Defines URL patterns for the analyzer app.
templates/analyzer/index.html: The main HTML template for the web interface.
static/analyzer/: Static assets like CSS/JS (though in this example, CSS/JS is embedded in HTML).
Technologies Used
Backend: Django (Python web framework)
Sentiment Analysis: TextBlob
Frontend: HTML, CSS, JavaScript
Tunneling: ngrok (for exposing local server)
License
This project is open-source and available under the MIT License.
SentimentAI — Emotion Analyzer
This is a simple Django web application that uses TextBlob to perform sentiment analysis on user-provided text. It provides a user-friendly interface to analyze text, determine its polarity (positive, negative, neutral) and subjectivity, and keeps a history of recent analyses.
Features
Real-time sentiment analysis using TextBlob.
Displays polarity, subjectivity, word count, and sentence count.
Visually represents sentiment (emoji, color-coded).
Stores and displays recent analysis history.
Responsive web interface.
Setup and Run
Prerequisites
Python 3.8+
Django
TextBlob
pyngrok (for local development/exposure)
Installation
Clone this repository:
git clone <repository_url>
cd sentiment_project
Install the required Python packages:
pip install -r requirements.txt # (assuming a requirements.txt is generated or packages installed as in notebook)
# or manually: pip install django textblob pyngrok
Download TextBlob corpora (if not already done):
python -m textblob.download_corpora
Run Django migrations:
python manage.py migrate
Start the Django development server:
python manage.py runserver
Accessing the Application
If running locally, navigate to http://127.0.0.1:8000 in your web browser.
If using pyngrok (as in a Colab environment), a public URL will be provided upon successful tunnel creation.
Usage
Enter text into the provided text area.
Click 'Analyze Sentiment' to get the analysis results.
The results will show the sentiment (Positive, Negative, Neutral), polarity score, subjectivity score, and other text statistics.
Recent analyses will be stored and displayed in the 'Recent Analyses' section.
Project Structure
sentiment_project/: Main Django project configuration.
analyzer/: Django app containing views, templates, and static files for the sentiment analysis functionality.
views.py: Contains the logic for sentiment analysis and rendering.
urls.py: Defines URL patterns for the analyzer app.
templates/analyzer/index.html: The main HTML template for the web interface.
static/analyzer/: Static assets like CSS/JS (though in this example, CSS/JS is embedded in HTML).
Technologies Used
Backend: Django (Python web framework)
Sentiment Analysis: TextBlob
Frontend: HTML, CSS, JavaScript
Tunneling: ngrok (for exposing local server)
License
This project is open-source and available under the MIT License.
