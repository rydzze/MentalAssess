from app import app
from app.depression import calculate_depression_score
from app.anxiety import calculate_anxiety_score
from app.stress import calculate_stress_score
from flask import render_template, request, redirect, url_for, session

app.secret_key = "MentalAccess"

@app.route('/')
def home():
    return render_template('index.php')

@app.route('/depression', methods=['GET', 'POST'])
def depression():
    if request.method == 'POST':
        session['sleep_issues'] = request.form.get('sleep_issues')
        session['energy'] = request.form.get('energy')
        session['appetite'] = request.form.get('appetite')
        session['concentration'] = request.form.get('concentration')
        session['behaviour'] = request.form.get('behaviour')
        session['emotion'] = request.form.get('emotion')
        return redirect(url_for('anxiety'))
    return render_template('depression.php')

@app.route('/anxiety', methods=['GET', 'POST'])
def anxiety():
    if request.method == 'POST':
        session['nervousness'] = request.form.get('nervousness')
        session['restlessness'] = request.form.get('restlessness')
        session['tenseness'] = request.form.get('tenseness')
        return redirect(url_for('stress'))
    return render_template('anxiety.php')

@app.route('/stress', methods=['GET', 'POST'])
def stress():
    if request.method == 'POST':
        session['overwhelmed'] = request.form.get('overwhelmed')
        session['irritability'] = request.form.get('irritability')
        session['tension'] = request.form.get('tension')
        session['calm'] = request.form.get('calm')
        session['forgetful'] = request.form.get('forgetful')
        session['sensitive'] = request.form.get('sensitive')
        return redirect(url_for('result'))
    return render_template('stress.php')

@app.route('/result')
def result():
    depression_level, depression_score = calculate_depression_score(session)
    anxiety_level, anxiety_score = calculate_anxiety_score(session)
    stress_level, stress_score = calculate_stress_score(session)

    return render_template(
        'result.php',
        depression_level=depression_level,
        depression_score=depression_score,
        anxiety_level=anxiety_level,
        anxiety_score=anxiety_score,
        stress_level=stress_level,
        stress_score=stress_score,
    )