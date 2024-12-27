def calculate_depression_score(answers):
    score = 0
    if answers.get('sleep_issues') == 'yes':
        score += 1
    if answers.get('appetite_changes') == 'yes':
        score += 1
    if answers.get('concentration') == 'yes':
        score += 1
    if answers.get('hopelessness') == 'yes':
        score += 1
    return score
