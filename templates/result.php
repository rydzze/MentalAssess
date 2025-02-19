<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MentalAssess | Results</title>
    <link rel="icon" href="{{ url_for('static', filename='images/mentalassess.png') }}" type="image/png">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/result.css') }}">
    <script src="https://cdn.jsdelivr.net/npm/sweetalert2@11"></script>
    <script src="{{ url_for('static', filename='js/popup.js') }}" defer></script>
</head>

<body>
    <div class="container">
        <h1>Diagnosis Results</h1>
        <p>Your scores are as follows:</p>
        
        <div class="results">
            <div class="result-item">
                <strong>Depression:</strong>
                <p>{{ depression_score }}</p>
                <p>{{ depression_level }}</p>
            </div>
            <div class="result-item">
                <strong>Anxiety:</strong>
                <p>{{ anxiety_score }}</p>
                <p>{{ anxiety_level }}</p>
            </div>
            <div class="result-item">
                <strong>Stress:</strong>
                <p>{{ stress_score }}</p>
                <p>{{ stress_level }}</p>
            </div>
        </div>

        <p class="disclaimer">Please note: The results of this self-assessment are not definitive. They may not accurately reflect your mental health status. For a comprehensive evaluation, we strongly recommend consulting a professional healthcare provider.</p>

        <form action="/send-email" method="POST" id="emailForm">
            <label for="email">Enter your email address to receive a copy of the results:</label>
            <input type="email" id="email" name="email" placeholder="your-email@example.com" required>
            <button id="send" type="submit">Send My Results</button>
        </form>

        <a href="/" class="retake-link">Retake Assessment</a>
    </div>
</body>
</html>