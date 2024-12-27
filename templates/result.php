<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Diagnosis Result</title>
</head>
<body>
    <h1>Diagnosis Results</h1>
    <p>Your scores and insights are as follows:</p>
    <ul>
        <li><strong>Depression:</strong> {{ depression_score }}
            - {{ 'Low' if depression_score <= 1 else 'Moderate' if depression_score <= 3 else 'High' }}<br>
            <em>{{ depression_insight }}</em>
        </li>
        <li><strong>Anxiety:</strong> {{ anxiety_score }}
            - {{ 'Low' if anxiety_score <= 1 else 'Moderate' if anxiety_score <= 3 else 'High' }}<br>
            <em>{{ anxiety_insight }}</em>
        </li>
        <li><strong>Stress:</strong> {{ stress_score }}
            - {{ 'Low' if stress_score <= 1 else 'Moderate' if stress_score <= 3 else 'High' }}<br>
            <em>{{ stress_insight }}</em>
        </li>
    </ul>
    <a href="/">Go Back</a>
</body>
</html>
