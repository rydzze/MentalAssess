<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Stress Diagnosis</title>
</head>
<body>
    <h1>Step 3: Stress</h1>
    <form action="/stress" method="post">
        <label>Do you feel overwhelmed frequently?</label><br>
        <input type="radio" name="overwhelmed" value="yes" required> Yes<br>
        <input type="radio" name="overwhelmed" value="no" required> No<br><br>

        <label>Do you feel irritable or impatient often?</label><br>
        <input type="radio" name="irritability" value="yes" required> Yes<br>
        <input type="radio" name="irritability" value="no" required> No<br><br>

        <label>Do you experience headaches or physical tension?</label><br>
        <input type="radio" name="tension" value="yes" required> Yes<br>
        <input type="radio" name="tension" value="no" required> No<br><br>

        <label>Do you have difficulty sleeping due to stress?</label><br>
        <input type="radio" name="stress_sleep" value="yes" required> Yes<br>
        <input type="radio" name="stress_sleep" value="no" required> No<br><br>

        <button type="submit">See Results</button>
    </form>
</body>
</html>
