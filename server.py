"""
server.py

This script defines a Flask application for emotion detection using an external API.
"""

import json
import requests
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("__name__")

@app.route("/")
def render_index_page():
    """
    Renders the index.html template.

    Returns:
        str: Rendered HTML content for the index page.
    """
    return render_template('index.html')

@app.route("/emotionDetector")
def emo_detector():
    """
    Handles the emotion detection endpoint.

    Retrieves text to analyze from the request arguments,
    passes it to the emotion_detector function, and formats
    the response for display.

    Returns:
        str: Formatted response containing emotion analysis results.
    """
    text_to_analyze = request.args.get('textToAnalyze')

    if not text_to_analyze.strip():
        return "Invalid text! Please try again."

    try:
        # Call emotion_detector function to get emotion analysis results
        response = emotion_detector(text_to_analyze)

        # Extract emotion scores and dominant emotion from the response
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant_emotion = response['dominant_emotion']

        # Format the response message
        formatted_response = (
            f"For the given statement, the system response is 'anger': {anger}, "
            f"'disgust': {disgust}, 'fear': {fear}, 'joy': {joy} and 'sadness': {sadness}. "
            f"The dominant emotion is {dominant_emotion}."
        )

        return formatted_response

    except requests.exceptions.RequestException as req_err:
        return f"Request error occurred: {str(req_err)}"
    
except json.JSONDecodeError as json_err:
        return f"JSON decoding error occurred: {str(json_err)}"
    except Exception as e:
        return f"Error processing request: {str(e)}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
