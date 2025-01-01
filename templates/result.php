<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diagnosis Result</title>
</head>

<body>
    <h1>Diagnosis Results</h1>
    <p>Your scores are as follows:</p>
    
    <ul>
        <li><strong>Depression:</strong> {{ depression_score }}, {{ depression_level }}
        </li>

        <li><strong>Anxiety:</strong> {{ anxiety_score }}, {{ anxiety_level }}
        </li>
        
        <li><strong>Stress:</strong> {{ stress_score }}, {{ stress_level }}
        </li>
    </ul>

    <a href="/">Go Back</a>
</body>
</html>