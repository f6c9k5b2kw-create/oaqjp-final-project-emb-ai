# Final project

Emotion Detection Application using Watson NLP.

This project provides a Python emotion detection function and a Flask web interface.

## Setup

```bash
python -m pip install -r requirements.txt
python -m unittest -v
python server.py
```

Open http://localhost:5000 in your browser. The NLP endpoint requires internet access.

## Code quality

```bash
pylint EmotionDetection/emotion_detection.py server.py
```

## Assignment evidence

The course requires the learner to submit their own GitHub URLs, code snippets, real terminal output and screenshots. Run the commands and capture the actual results. Tests mock the remote service; they do not prove the remote service is available.
