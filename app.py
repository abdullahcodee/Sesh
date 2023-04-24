from flask import Flask, render_template, request, redirect, url_for, flash, send_from_directory
import os
import tempfile
from urllib.request import urlretrieve
from werkzeug.utils import secure_filename
from moviepy.editor import AudioFileClip
import speech_recognition as sr

app = Flask(__name__)

# Configure upload folder and allowed file extensions
app.config['UPLOAD_FOLDER'] = 'uploads'
ALLOWED_EXTENSIONS = {'mp4', 'avi', 'mov', 'mkv', 'webm', 'flv'}
app.secret_key = 'secret_key_here'


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/convert', methods=['POST'])
def convert():
    lang = request.form.get('language')  # Get selected language from form

    if 'file' not in request.files:
        flash('No file uploaded')
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        flash('No file selected')
        return redirect(request.url)

    if not allowed_file(file.filename):
        flash(f'Invalid file type, allowed file types are {ALLOWED_EXTENSIONS}')
        return redirect(request.url)

    filename = secure_filename(file.filename)
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # Extract audio from the video file
    audio = AudioFileClip(filepath)
    audio_file = os.path.join(app.config['UPLOAD_FOLDER'], f'{filename}.wav')
    audio.write_audiofile(audio_file)

    # Load the WAV file into a speech recognition engine
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio = r.record(source)

    # Use the speech recognition engine to transcribe the audio in the selected language
    try:
        text = r.recognize_google(audio, language=lang)  # Use selected language
    except sr.UnknownValueError:
        flash('Could not transcribe audio, please try again with a different file')
        return redirect(request.url)

    # Save the transcribed text to a text file
    text_file = os.path.join(app.config['UPLOAD_FOLDER'], f'{filename}.txt')
    with open(text_file, "w") as f:
        f.write(text)

    return redirect(url_for('result', filename=filename, text=text))


@app.route('/result')
def result():
    filename = request.args.get('filename')
    text = request.args.get('text')
    return render_template('result.html', filename=filename, text=text)


@app.route('/download/<filename>')
def download(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], f'{filename}.txt', as_attachment=True)


if __name__ == '__main__':
    app.secret_key = 'supersecretkey'
    app.run(debug=True)
