from flask import Flask, render_template, request, redirect, url_for, session
from flask_mail import Mail, Message
from app.depression import calculate_depression_score
from app.anxiety import calculate_anxiety_score
from app.stress import calculate_stress_score
from dotenv import load_dotenv
import os

load_dotenv()
app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")

app.config['MAIL_DEBUG'] = True
app.config['MAIL_SERVER'] = os.getenv('MAIL_SERVER')
app.config['MAIL_PORT'] = int(os.getenv('MAIL_PORT'))
app.config['MAIL_USE_TLS'] = os.getenv('MAIL_USE_TLS').lower() in ['true', '1', 'yes']
app.config['MAIL_USE_SSL'] = os.getenv('MAIL_USE_SSL').lower() in ['true', '1', 'yes']
app.config['MAIL_USERNAME'] = os.getenv('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.getenv('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = os.getenv('MAIL_DEFAULT_SENDER')

mail = Mail(app)
app.config['MAIL_DEBUG'] = True

@app.route('/')
def home():
    return render_template('index.html')

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
    return render_template('depression.html')

@app.route('/anxiety', methods=['GET', 'POST'])
def anxiety():
    if request.method == 'POST':
        session['nervousness'] = request.form.get('nervousness')
        session['restlessness'] = request.form.get('restlessness')
        session['tenseness'] = request.form.get('tenseness')
        session['panicky'] = request.form.get('panicky')
        session['overthinking'] = request.form.get('overthinking')
        session['shortbreath'] = request.form.get('shortbreath')
        return redirect(url_for('stress'))
    return render_template('anxiety.html')

@app.route('/stress', methods=['GET', 'POST'])
def stress():
    if request.method == 'POST':
        session['overwhelmed'] = request.form.get('overwhelmed')
        session['irritability'] = request.form.get('irritability')
        session['tension'] = request.form.get('tension')
        session['cope'] = request.form.get('cope')
        session['forgetful'] = request.form.get('forgetful')
        session['sensitive'] = request.form.get('sensitive')
        return redirect(url_for('result'))
    return render_template('stress.html')

@app.route('/result')
def result():
    depression_level, depression_score = calculate_depression_score(session)
    anxiety_level, anxiety_score = calculate_anxiety_score(session)
    stress_level, stress_score = calculate_stress_score(session)

    return render_template(
        'result.html',
        depression_level=depression_level,
        depression_score=depression_score,
        anxiety_level=anxiety_level,
        anxiety_score=anxiety_score,
        stress_level=stress_level,
        stress_score=stress_score,
    )

@app.route('/send-email', methods=['POST'])
def send_email():
    email = request.form['email']
    depression_level, depression_score = calculate_depression_score(session)
    anxiety_level, anxiety_score = calculate_anxiety_score(session)
    stress_level, stress_score = calculate_stress_score(session)

    subject = "Your Mental Health Assessment Results"
    body = f"""
Dear User,

Thank you for completing the MentalAssess self-test. Below are the results of your assessment:

- Depression: {depression_score} (Level: {depression_level})
- Anxiety: {anxiety_score} (Level: {anxiety_level})
- Stress: {stress_score} (Level: {stress_level})

Please note that the results from this self-test are for informational purposes only. These results should not be used as a diagnostic tool or replace professional mental health evaluation. It is highly recommended to consult with a licensed healthcare provider for a comprehensive assessment and personalized advice.

If you have concerns about your mental health or are experiencing distress, please seek professional help immediately.

Thank you for using MentalAssess. We are here to support your mental well-being!

Best regards,
MentalAssess Team

Disclaimer: This is an automated email from MentalAssess. Please do not reply to this email as it is not monitored."""

    try:
        sender_email = ("MentalAssess Team", "rydzze@gmail.com")
        msg = Message(subject, recipients=[email], body=body, sender=sender_email)
        mail.send(msg)
        return redirect(url_for('result', email_sent='success'))
    except Exception as e:
        print(f"Error sending email: {e}")
        return redirect(url_for('result', email_sent='error'))

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=988)