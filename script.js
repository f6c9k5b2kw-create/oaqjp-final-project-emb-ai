async function analyze() {
  const text = document.getElementById('text').value;
  const output = document.getElementById('result');
  output.textContent = 'Analyzing...';
  try {
    const response = await fetch('/emotionDetector?textToAnalyze=' + encodeURIComponent(text));
    output.textContent = await response.text();
  } catch (error) {
    output.textContent = 'Unable to analyze the text. Please try again.';
  }
}
