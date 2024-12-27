from flask import render_template, request, redirect, url_for, session
from app import app
from app.depression import calculate_depression_score
from app.anxiety import calculate_anxiety_score
from app.stress import calculate_stress_score

app.secret_key = "S3CR3T"

@app.route('/')
def home():
    return render_template('index.php')

@app.route('/depression', methods=['GET', 'POST'])
def depression():
    if request.method == 'POST':
        session['sleep_issues'] = request.form.get('sleep_issues')
        session['appetite_changes'] = request.form.get('appetite_changes')
        session['concentration'] = request.form.get('concentration')
        session['hopelessness'] = request.form.get('hopelessness')
        return redirect(url_for('anxiety'))
    return render_template('depression.php')

@app.route('/anxiety', methods=['GET', 'POST'])
def anxiety():
    if request.method == 'POST':
        session['nervousness'] = request.form.get('nervousness')
        session['restlessness'] = request.form.get('restlessness')
        session['tenseness'] = request.form.get('tenseness')
        session['palpitations'] = request.form.get('palpitations')
        return redirect(url_for('stress'))
    return render_template('anxiety.php')

@app.route('/stress', methods=['GET', 'POST'])
def stress():
    if request.method == 'POST':
        session['overwhelmed'] = request.form.get('overwhelmed')
        session['irritability'] = request.form.get('irritability')
        session['tension'] = request.form.get('tension')
        session['stress_sleep'] = request.form.get('stress_sleep')
        return redirect(url_for('result'))
    return render_template('stress.php')

@app.route('/result')
def result():
    depression_score = calculate_depression_score(session)
    anxiety_score = calculate_anxiety_score(session)
    stress_score = calculate_stress_score(session)

    def get_insight(score, disorder):
        if score <= 1:
            return f"You show minimal symptoms of {disorder}. It's likely manageable but worth monitoring."
        elif score <= 3:
            return f"You show moderate symptoms of {disorder}. Consider seeking advice if it affects daily life."
        else:
            return f"You show high symptoms of {disorder}. Professional help is recommended."

    insights = {
        'depression_insight': get_insight(depression_score, 'depression'),
        'anxiety_insight': get_insight(anxiety_score, 'anxiety'),
        'stress_insight': get_insight(stress_score, 'stress')
    }

    return render_template(
        'result.php',
        depression_score=depression_score,
        anxiety_score=anxiety_score,
        stress_score=stress_score,
        depression_insight=insights['depression_insight'],
        anxiety_insight=insights['anxiety_insight'],
        stress_insight=insights['stress_insight']
    )
