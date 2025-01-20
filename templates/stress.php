<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>MentalAssess | Stress</title>
    <link rel="icon" href="{{ url_for('static', filename='images/mentalassess.png') }}" type="image/png">
    <link rel="stylesheet" href="{{ url_for('static', filename='css/das.css') }}">
</head>

<body>
    <div class="container">
        <form action="/stress" method="post">
            <div class="question">
                <div class="question-title">Do you feel overwhelmed frequently?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="overwhelmed" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="overwhelmed" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="overwhelmed" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="overwhelmed" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="overwhelmed" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="overwhelmed" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Do you feel irritable or impatient often?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="irritability" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="irritability" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="irritability" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="irritability" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="irritability" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="irritability" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Do you experience headaches or physical tension?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="tension" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="tension" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="tension" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="tension" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="tension" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="tension" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Felt that you could NOT cope with all the things you had to do?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="cope" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="cope" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="cope" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="cope" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="cope" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="cope" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Do you experience memory problems or difficulty making decisions?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="forgetful" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="forgetful" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="forgetful" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="forgetful" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="forgetful" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="forgetful" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <div class="question">
                <div class="question-title">Do you find yourself sensitive to noise or distractions?</div>
                <div class="options">
                    <label>
                        <input type="radio" name="sensitive" value="0.0" required>
                        <span>Never</span>
                    </label>
                    <label>
                        <input type="radio" name="sensitive" value="0.2" required>
                        <span>Rarely</span>
                    </label>
                    <label>
                        <input type="radio" name="sensitive" value="0.4" required>
                        <span>Sometimes</span>
                    </label>
                    <label>
                        <input type="radio" name="sensitive" value="0.6" required>
                        <span>Often</span>
                    </label>
                    <label>
                        <input type="radio" name="sensitive" value="0.8" required>
                        <span>Very Often</span>
                    </label>
                    <label>
                        <input type="radio" name="sensitive" value="1.0" required>
                        <span>Always</span>
                    </label>
                </div>
            </div>

            <button type="submit">Submit</button>
        </form>
    </div>
</body>
</html>