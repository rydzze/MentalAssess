<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MentalAssess | Anxiety</title>
    <link rel="icon" href="{{ url_for('static', filename='images/mentalassess.png') }}" type="image/png">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/das.css') }}">
</head>

<body>
    <div class="container">
        <form action="/anxiety" method="post">
            <div class="question">
                <div class="question-title">Do you feel nervous frequently?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="nervousness" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="nervousness" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="nervousness" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="nervousness" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="nervousness" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="nervousness" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Do you feel restless or uneasy?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="restlessness" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="restlessness" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="restlessness" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="restlessness" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="restlessness" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="restlessness" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Do you feel tense or unable to relax?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="tenseness" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="tenseness" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="tenseness" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="tenseness" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="tenseness" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="tenseness" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Do you experience sudden feelings of panic or fear without an obvious reason?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="panicky" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="panicky" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="panicky" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="panicky" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="panicky" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="panicky" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Do you find yourself overthinking or dwelling on things that might go wrong?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="overthinking" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="overthinking" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="overthinking" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="overthinking" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="overthinking" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="overthinking" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Have you ever experienced shortness of breath lately?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="shortbreath" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="shortbreath" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="shortbreath" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="shortbreath" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="shortbreath" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="shortbreath" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <button type="submit">Next</button>
        </form>
    </div>
</body>
</html>