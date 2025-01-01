import clips

def calculate_anxiety_score(answers):
    env = clips.Environment()
    env.reset()

    env.build("""
    (deftemplate questionnaire
       (slot nervousness)
       (slot restlessness)
       (slot tenseness)
    )
    """)

    env.build("""
    (deftemplate anxiety-value
       (slot value)
       (slot cf)
    )
    """)

    env.build("""
    (deftemplate cf-values
       (slot cf1 (default 0))
       (slot cf2 (default 0))
       (slot cf3 (default 0))
    )
    """)

    env.assert_string("(cf-values)")

    env.build("""
    (defrule check-nervousness
       (questionnaire (nervousness ?answer))
       ?cf <- (cf-values (cf1 ?cf1))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf1 0.75))
       else
          (modify ?cf (cf1 0.25))
       )
    )
    """)

    env.build("""
    (defrule check-restlessness
       (questionnaire (restlessness ?answer))
       ?cf <- (cf-values (cf2 ?cf2))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf2 0.80))
       else
          (modify ?cf (cf2 0.20))
       )
    )
    """)

    env.build("""
    (defrule check-tenseness
       (questionnaire (tenseness ?answer))
       ?cf <- (cf-values (cf3 ?cf3))
       =>
       (if (eq ?answer "yes") then
          (modify ?cf (cf3 0.95))
       else
          (modify ?cf (cf3 0.05))
       )
    )
    """)

    env.build("""
    (defrule final-check
       (cf-values (cf1 ?cf1) (cf2 ?cf2) (cf3 ?cf3))
       =>
       (bind ?total (+ ?cf1 ?cf2 ?cf3))
       (bind ?average (/ ?total 3))
       (if (<= ?average 0.25) then
          (assert (anxiety-value (cf ?average) (value "No Anxiety")))
       else
          (if (<= ?average 0.5) then
             (assert (anxiety-value (cf ?average) (value "Mild Anxiety")))
          else
             (if (<= ?average 0.75) then
                (assert (anxiety-value (cf ?average) (value "Moderate Anxiety")))
             else
                (assert (anxiety-value (cf ?average) (value "Severe Anxiety")))
             )
          )
       )
    )
    """)

    env.build("""
    (defrule final-value
       (anxiety-value (value ?level) (cf ?certainty))
       =>
       (bind ?percentage (* ?certainty 100))
       (halt)
    )
    """)

    env.assert_string(f'(questionnaire (nervousness "{answers.get("nervousness")}") (restlessness "{answers.get("restlessness")}") (tenseness "{answers.get("tenseness")}") )')

    env.run()

    for fact in env.facts():
        if fact.template.name == 'anxiety-value':
            severity_level = fact['value']
            certainty_factor = f"{(fact['cf'] * 100):.2f}%"

            return severity_level, certainty_factor