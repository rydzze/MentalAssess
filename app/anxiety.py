def calculate_anxiety_score(answers):
    score = 0
    if answers.get('nervousness') == 'yes':
        score += 1
    if answers.get('restlessness') == 'yes':
        score += 1
    if answers.get('tenseness') == 'yes':
        score += 1
    if answers.get('palpitations') == 'yes':
        score += 1
    return score
