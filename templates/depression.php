<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MentalAssess | Depression</title>
    <link rel="icon" href="{{ url_for('static', filename='images/mentalassess.png') }}" type="image/png">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/das.css') }}">
</head>

<body>
    <div class="container">
        <form action="/depression" method="post">
            <div class="question">
                <div class="question-title">How often have you had trouble sleeping over the past two weeks?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="sleep_issues" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="sleep_issues" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="sleep_issues" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="sleep_issues" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="sleep_issues" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="sleep_issues" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How much have you felt a lack of energy over the last two weeks?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="energy" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="energy" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="energy" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="energy" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="energy" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="energy" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How much have you noticed changes in your appetite over the last two weeks?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="appetite" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="appetite" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="appetite" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="appetite" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="appetite" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="appetite" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">To what extent have you had difficulty concentrating over the last two weeks?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="concentration" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="concentration" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="concentration" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="concentration" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="concentration" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="concentration" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">How much have you felt passive or lacked motivation to engage in activities over the last two weeks?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="behaviour" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="behaviour" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="behaviour" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="behaviour" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="behaviour" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="behaviour" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Can you rate how much you felt sad in the past two weeks?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="emotion" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="emotion" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="emotion" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="emotion" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="emotion" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="emotion" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <button type="submit">Next</button>
        </form>
    </div>
</body>
</html>