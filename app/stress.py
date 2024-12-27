def calculate_stress_score(answers):
    score = 0
    if answers.get('overwhelmed') == 'yes':
        score += 1
    if answers.get('irritability') == 'yes':
        score += 1
    if answers.get('tension') == 'yes':
        score += 1
    if answers.get('stress_sleep') == 'yes':
        score += 1
    return score
