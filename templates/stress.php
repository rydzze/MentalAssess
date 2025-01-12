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
        <input type="radio" name="overwhelmed" value="0.0" required> Never<br>
        <input type="radio" name="overwhelmed" value="0.2" required> Rarely<br>
        <input type="radio" name="overwhelmed" value="0.4" required> Sometimes<br>
        <input type="radio" name="overwhelmed" value="0.6" required> Often<br>
        <input type="radio" name="overwhelmed" value="0.8" required> Very often<br>
        <input type="radio" name="overwhelmed" value="1.0" required> Always<br><br>

        <label>Do you feel irritable or impatient often?</label><br>
        <input type="radio" name="irritability" value="0.0" required> Never<br>
        <input type="radio" name="irritability" value="0.2" required> Rarely<br>
        <input type="radio" name="irritability" value="0.4" required> Sometimes<br>
        <input type="radio" name="irritability" value="0.6" required> Often<br>
        <input type="radio" name="irritability" value="0.8" required> Very often<br>
        <input type="radio" name="irritability" value="1.0" required> Always<br><br>

        <label>Do you experience headaches or physical tension?</label><br>
        <input type="radio" name="tension" value="0.0" required> Never<br>
        <input type="radio" name="tension" value="0.2" required> Rarely<br>
        <input type="radio" name="tension" value="0.4" required> Sometimes<br>
        <input type="radio" name="tension" value="0.6" required> Often<br>
        <input type="radio" name="tension" value="0.8" required> Very often<br>
        <input type="radio" name="tension" value="1.0" required> Always<br><br>

        <label>Do you feel lonely or isolated?</label><br>
        <input type="radio" name="lonely" value="0.0" required> Never<br>
        <input type="radio" name="lonely" value="0.2" required> Rarely<br>
        <input type="radio" name="lonely" value="0.4" required> Sometimes<br>
        <input type="radio" name="lonely" value="0.6" required> Often<br>
        <input type="radio" name="lonely" value="0.8" required> Very often<br>
        <input type="radio" name="lonely" value="1.0" required> Always<br><br>

        <label>Do you experience memory problems or difficulty making decisions?</label><br>
        <input type="radio" name="forgetful" value="0.0" required> Never<br>
        <input type="radio" name="forgetful" value="0.2" required> Rarely<br>
        <input type="radio" name="forgetful" value="0.4" required> Sometimes<br>
        <input type="radio" name="forgetful" value="0.6" required> Often<br>
        <input type="radio" name="forgetful" value="0.8" required> Very often<br>
        <input type="radio" name="forgetful" value="1.0" required> Always<br><br>

        <label>Do you engage in unhealthy coping mechanisms (e.g., excessive alcohol or drug use)?</label><br>
        <input type="radio" name="unhealthy" value="0.0" required> Never<br>
        <input type="radio" name="unhealthy" value="0.2" required> Rarely<br>
        <input type="radio" name="unhealthy" value="0.4" required> Sometimes<br>
        <input type="radio" name="unhealthy" value="0.6" required> Often<br>
        <input type="radio" name="unhealthy" value="0.8" required> Very often<br>
        <input type="radio" name="unhealthy" value="1.0" required> Always<br><br>
        
        <button type="submit">See Results</button>
    </form>
</body>
</html>