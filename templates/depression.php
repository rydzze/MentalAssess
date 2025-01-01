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
        <input type="radio" name="sleep_issues" value="yes" required> Yes<br>
        <input type="radio" name="sleep_issues" value="no" required> No<br><br>

        <label>Have you experienced appetite changes?</label><br>
        <input type="radio" name="appetite_changes" value="yes" required> Yes<br>
        <input type="radio" name="appetite_changes" value="no" required> No<br><br>

        <label>Are you having trouble concentrating?</label><br>
        <input type="radio" name="concentration" value="yes" required> Yes<br>
        <input type="radio" name="concentration" value="no" required> No<br><br>

        <button type="submit">Next</button>
    </form>
</body>
</html>