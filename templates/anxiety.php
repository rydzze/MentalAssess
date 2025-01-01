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
        <input type="radio" name="nervousness" value="yes" required> Yes<br>
        <input type="radio" name="nervousness" value="no" required> No<br><br>

        <label>Do you feel restless or uneasy?</label><br>
        <input type="radio" name="restlessness" value="yes" required> Yes<br>
        <input type="radio" name="restlessness" value="no" required> No<br><br>

        <label>Do you feel tense or unable to relax?</label><br>
        <input type="radio" name="tenseness" value="yes" required> Yes<br>
        <input type="radio" name="tenseness" value="no" required> No<br><br>

        <button type="submit">Next</button>
    </form>
</body>
</html>