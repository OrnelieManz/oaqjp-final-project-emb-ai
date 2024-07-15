
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

#Initiate the flask app
app = Flask('Emotion Detector')

@app.route("/emotionDetector")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs Emotion analysis over it using emotion_detector()
        function. The output returned shows the emotions and their scores 
        along with the dominent emotion.
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)
    sadness=response['sadness']
    dominant_emotion=response['dominant_emotion']
    anger = response['anger']
    disgust = response['disgust']
    fear = response['fear']
    joy = response['joy']

    if dominant_emotion is None:
        return "Invalid input! Try again"
    return f"For the given statement, the system response is \'anger\': {anger}, \'disgust\': {disgust}, \'fear\': {fear}, \'joy\': {joy} and \'sadness\': {sadness}. The dominant emotion is {dominant_emotion}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template('index.html')

if __name__ == "__main__":
    ''' This functions executes the flask app and deploys it on localhost:5000
    '''
    app.run(host="0.0.0.0", port=5000)