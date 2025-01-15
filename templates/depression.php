<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Depression Diagnosis</title>
</head>

<body>
    <h1>Step 1: Depression</h1>

    <form action="/depression" method="post">
        <label>How often have you had trouble sleeping over the past two weeks?</label><br>
        <input type="radio" name="sleep_issues" value="0.0" required> Never<br>
        <input type="radio" name="sleep_issues" value="0.2" required> Rarely<br>
        <input type="radio" name="sleep_issues" value="0.4" required> Sometimes<br>
        <input type="radio" name="sleep_issues" value="0.6" required> Often<br>
        <input type="radio" name="sleep_issues" value="0.8" required> Very often<br>
        <input type="radio" name="sleep_issues" value="1.0" required> Always<br><br>

        <label>How much have you felt a lack of energy over the last two weeks?</label><br>
        <input type="radio" name="energy" value="0.0" required> Never<br>
        <input type="radio" name="energy" value="0.2" required> Rarely<br>
        <input type="radio" name="energy" value="0.4" required> Sometimes<br>
        <input type="radio" name="energy" value="0.6" required> Often<br>
        <input type="radio" name="energy" value="0.8" required> Very often<br>
        <input type="radio" name="energy" value="1.0" required> Always<br><br>

        <label>How much have you noticed changes in your appetite over the last two weeks?</label><br>
        <input type="radio" name="appetite" value="0.0" required> Never<br>
        <input type="radio" name="appetite" value="0.2" required> Rarely<br>
        <input type="radio" name="appetite" value="0.4" required> Sometimes<br>
        <input type="radio" name="appetite" value="0.6" required> Often<br>
        <input type="radio" name="appetite" value="0.8" required> Very often<br>
        <input type="radio" name="appetite" value="1.0" required> Always<br><br>

        <label>To what extent have you had difficulty concentrating over the last two weeks?</label><br>
        <input type="radio" name="concentration" value="0.0" required> Never<br>
        <input type="radio" name="concentration" value="0.2" required> Rarely<br>
        <input type="radio" name="concentration" value="0.4" required> Sometimes<br>
        <input type="radio" name="concentration" value="0.6" required> Often<br>
        <input type="radio" name="concentration" value="0.8" required> Very often<br>
        <input type="radio" name="concentration" value="1.0" required> Always<br><br>

        <label>How much have you felt passive or lacked motivation to engage in activities over the last two weeks?</label><br>
        <input type="radio" name="behaviour" value="0.0" required> Never<br>
        <input type="radio" name="behaviour" value="0.2" required> Rarely<br>
        <input type="radio" name="behaviour" value="0.4" required> Sometimes<br>
        <input type="radio" name="behaviour" value="0.6" required> Often<br>
        <input type="radio" name="behaviour" value="0.8" required> Very often<br>
        <input type="radio" name="behaviour" value="1.0" required> Always<br><br>

        <label>Can you rate how much you felt sad in the past two weeks?</label><br>
        <input type="radio" name="emotion" value="0.0" required> Never<br>
        <input type="radio" name="emotion" value="0.2" required> Rarely<br>
        <input type="radio" name="emotion" value="0.4" required> Sometimes<br>
        <input type="radio" name="emotion" value="0.6" required> Often<br>
        <input type="radio" name="emotion" value="0.8" required> Very often<br>
        <input type="radio" name="emotion" value="1.0" required> Always<br><br>

        <button type="submit">Next</button>
    </form>
</body>
</html>