from flask import Flask, render_template, request
from pytube import YouTube
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form['url']
    try:
        yt = YouTube(video_url)
        stream = yt.streams.get_highest_resolution()
        stream.download()
        return "Download successful!"
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
