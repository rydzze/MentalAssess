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
        <label>Do you have sleep issues?</label><br>
        <input type="radio" name="sleep_issues" value="0.0" required> Never<br>
        <input type="radio" name="sleep_issues" value="0.2" required> Rarely<br>
        <input type="radio" name="sleep_issues" value="0.4" required> Sometimes<br>
        <input type="radio" name="sleep_issues" value="0.6" required> Often<br>
        <input type="radio" name="sleep_issues" value="0.8" required> Very often<br>
        <input type="radio" name="sleep_issues" value="1.0" required> Always<br><br>

        <label>Have you experienced appetite changes?</label><br>
        <input type="radio" name="appetite_changes" value="0.0" required> Never<br>
        <input type="radio" name="appetite_changes" value="0.2" required> Rarely<br>
        <input type="radio" name="appetite_changes" value="0.4" required> Sometimes<br>
        <input type="radio" name="appetite_changes" value="0.6" required> Often<br>
        <input type="radio" name="appetite_changes" value="0.8" required> Very often<br>
        <input type="radio" name="appetite_changes" value="1.0" required> Always<br><br>

        <label>Are you having trouble concentrating?</label><br>
        <input type="radio" name="concentration" value="0.0" required> Never<br>
        <input type="radio" name="concentration" value="0.2" required> Rarely<br>
        <input type="radio" name="concentration" value="0.4" required> Sometimes<br>
        <input type="radio" name="concentration" value="0.6" required> Often<br>
        <input type="radio" name="concentration" value="0.8" required> Very often<br>
        <input type="radio" name="concentration" value="1.0" required> Always<br><br>

        <button type="submit">Next</button>
    </form>
</body>
</html>