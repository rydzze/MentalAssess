<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Anxiety Diagnosis</title>
</head>

<body>
    <h1>Step 2: Anxiety</h1>

    <form action="/anxiety" method="post">
        <label>Do you feel nervous frequently?</label><br>
        <input type="radio" name="nervousness" value="0.0" required> Never<br>
        <input type="radio" name="nervousness" value="0.2" required> Rarely<br>
        <input type="radio" name="nervousness" value="0.4" required> Sometimes<br>
        <input type="radio" name="nervousness" value="0.6" required> Often<br>
        <input type="radio" name="nervousness" value="0.8" required> Very often<br>
        <input type="radio" name="nervousness" value="1.0" required> Always<br><br>

        <label>Do you feel restless or uneasy?</label><br>
        <input type="radio" name="restlessness" value="0.0" required> Never<br>
        <input type="radio" name="restlessness" value="0.2" required> Rarely<br>
        <input type="radio" name="restlessness" value="0.4" required> Sometimes<br>
        <input type="radio" name="restlessness" value="0.6" required> Often<br>
        <input type="radio" name="restlessness" value="0.8" required> Very often<br>
        <input type="radio" name="restlessness" value="1.0" required> Always<br><br>

        <label>Do you feel tense or unable to relax?</label><br>
        <input type="radio" name="tenseness" value="0.0" required> Never<br>
        <input type="radio" name="tenseness" value="0.2" required> Rarely<br>
        <input type="radio" name="tenseness" value="0.4" required> Sometimes<br>
        <input type="radio" name="tenseness" value="0.6" required> Often<br>
        <input type="radio" name="tenseness" value="0.8" required> Very often<br>
        <input type="radio" name="tenseness" value="1.0" required> Always<br><br>

        <button type="submit">Next</button>
    </form>
</body>
</html>